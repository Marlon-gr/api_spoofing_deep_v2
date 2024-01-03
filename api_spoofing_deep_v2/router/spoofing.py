import logging
from urllib import request

from fastapi import APIRouter

from api_spoofing_deep_v2.services.spoofing import \
    SpoofingService

spoofing_v2 = APIRouter()


@spoofing_v2.post('/deep-learning/v2')
def deep_learning_v2():
    """Check endpoint handler.
    """
    image = request.get_json()['base_64']
    service = SpoofingService()
    # Predict
    spoofed, trust = service.predict(image)
    # Response
    output_response = {
        'trust': round(float(abs(trust) * 100), 2),
        'is_spoofed': spoofed
    }
    logging.getLogger('spoofing.api').info(output_response)
    return jsonify(output_response), 200
