from fastapi import Request, Response
from loguru import logger

from api_spoofing_deep_v2.utils import time_second, time_count


def init_latency(app):
    @app.middleware("http")
    async def instrumentation(request: Request, call_next):
        _time = time_second()
        content = b''
        response = await call_next(request)

        async for chunk in response.body_iterator:
            content += chunk
        logger.log("RESPONSE", f'[*] {str(content, encoding="utf-8")}')
        logger.log("LATENCY", f'[*] {time_count(_time)} s')

        return Response(
            content=content,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
    return app