import logging

import torch
from torchvision import transforms

from api_spoofing_deep_v2.utils.api_util import environ_value, is_base64
from api_spoofing_deep_v2.utils.base64_decoder import Base64Decoder
from api_spoofing_deep_v2.utils.response_error import raise_error

error_model = False
# Load model in memory
transforms = transforms.Compose([
    Base64Decoder(),
    transforms.ToPILImage(),
    transforms.Resize(255),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),raise_error
])

try:
    model_path = "/usr/src/spoofing_model/" + str(environ_value(
        "MODEL_NAME_V4"))
    model = torch.jit.load(model_path, map_location='cpu')
    model.eval()
except FileNotFoundError as e:
    logging.getLogger('spoofing.service').error(f'Error {e} ')
    error_model = True
except ValueError as e:
    logging.getLogger('spoofing.service').error(f'Error {e}')
    error_model = True


class SpoofingDeepV4Service:

    def __init__(self):
        if error_model:
            raise_error(401)

    @staticmethod
    def is_valid_base_64(request) -> bool:
        if not request.is_json:
            raise_error(400)
        result = request.get_json()
        # The request contains the correct parameters?
        if 'base_64' not in result:
            raise_error(403)
        # str represents base64?
        is_base64(result['base_64'])
        return result['base_64']

    @staticmethod
    def predict_image(image_str) -> list:
        output_model = []
        try:
            with torch.no_grad():
                image = transforms(image_str)
                image = image.unsqueeze_(0)
                output = model(image)
                output_model = [
                    output[0][0].item(),
                    output[0][1].item(),
                    output[0][2].item(),
                    output[0][3].item()
                ]
        except TypeError:
            raise_error(405)
        return output_model
