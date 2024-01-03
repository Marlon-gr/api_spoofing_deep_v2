__version__ = '1.0.0b1'

from fastapi import FastAPI
from loguru import logger

from api_spoofing_deep_v2.config import init_configuration
from api_spoofing_deep_v2.exception import init_exception
from api_spoofing_deep_v2.router import deep_v4, spoofing, start
from api_spoofing_deep_v2.utils.middleware import init_latency


def create_app():
    app = FastAPI(
        title='Spoofing Deep v2 API',
        version=__version__
    )
    # Init configuration.
    init_configuration()
    # init exception.
    app = init_exception(app)
    # init Latency.
    app = init_latency(app)
    # Add routing.
    app.include_router(spoofing.spoofing_v2, tags=[''])
    app.include_router(deep_v4.spoofing_v4, tags=['Client'])
    app.include_router(start, tags=['Metrics and Health'])
    # Return App.
    logger.info(f"[+] APPLICATION CREATED, READY TO UP.")
    return app
