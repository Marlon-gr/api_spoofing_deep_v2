import logging
import torch
from torch.autograd import Variable
from torchvision import transforms

from api_spoofing_deep_v2.utils.api_util import to_numpy_rgb
from api_spoofing_deep_v2.utils.response_error import raise_error
from api_spoofing_deep_v2.utils.api_util import environ_value

torch.backends.quantized.engine = 'qnnpack'

error_model = False
# Load model in memory
test_transforms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

try:
    model_path = "/usr/src/spoofing_model/" + str(environ_value(
        "MODEL_NAME_V2"))
    model = torch.jit.load(model_path, map_location='cpu')
    for param in model.parameters():
        param.requires_grad = False
    model.eval()
except FileNotFoundError as e:
    logging.getLogger('spoofing.service').error(f'Error {e} ')
    error_model = True
except ValueError as e:
    logging.getLogger('spoofing.service').error(f'Error {e}')
    error_model = True


class SpoofingService:

    def __init__(self):
        if error_model:
            raise_error(401)

    @staticmethod
    def is_valid_predicted(predicted):
        proba = None
        if predicted is not False:
            proba = predicted[0][1]
        return proba

    def predict(self, image):
        predicted, trust = None, None
        try:
            image_np = to_numpy_rgb(image)
            # return predicted, trust
            predicted, trust = self.predict_image(image_np)
        except ValueError:
            raise_error(403)
        return predicted, trust

    def predict_image(self, image):
        output, probabilities = None, None
        try:
            image_tensor = test_transforms(image).float()
            image_tensor = image_tensor.unsqueeze_(0)
            input_img = Variable(image_tensor)
            input_img = input_img
            output = model(input_img)
            sm = torch.nn.Softmax(dim=1)
            probabilities = sm(output)
        except TypeError:
            raise_error(405)
        return self.is_spoofing(output, probabilities)

    @staticmethod
    def is_spoofing(output, probabilities):
        value = True
        trust_1 = probabilities[0][0].item()
        trust_2 = probabilities[0][1].item()
        if trust_1 > trust_2:
            trust = trust_1
        else:
            trust = trust_2
        _, tensor = torch.max(output.data, 1)
        predict = tensor[0].item()
        if predict != 1:
            value = False
        return value, trust
