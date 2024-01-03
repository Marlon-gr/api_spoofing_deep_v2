import logging

from fastapi import APIRouter

from api_spoofing_deep_v2.services.deep_v4 import \
    SpoofingDeepV4Service

spoofing_v4 = APIRouter()


@spoofing_v4.post('/deep-learning/v4')
def deep_learning_v4():
    """Check endpoint handler.
    """
    spoofing_service = SpoofingDeepV4Service()
    image_base_64_str = spoofing_service.is_valid_base_64(request)
    # Predict
    output_model = spoofing_service.predict_image(image_base_64_str)
    # Response
    output_response = {
        'output_model': output_model
    }
    logging.getLogger('spoofing.controller').info(output_response)
    return jsonify(output_response), 200
