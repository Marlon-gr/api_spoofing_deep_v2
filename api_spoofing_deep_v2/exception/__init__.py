
import traceback

from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from loguru import logger


class APiException(Exception):
    def __init__(self, stacktrace: str, code: int = 404,
                 message: str = "OPERATION ERROR"):
        self.code = code
        self.message = message
        self.stacktrace = stacktrace
        logger.log("EXCEPTION", f'[-] {message}, STATUS: {code}')


def init_exception(app):
    @app.exception_handler(APiException)
    def invalid_data_exception(request: Request, exception: APiException):
        return JSONResponse(
            status_code=exception.code,
            content={
                "message": exception.message,
                "stacktrace": exception.stacktrace
            }
        )

    @app.exception_handler(HTTPException)
    def http_exception(request: Request, exception: HTTPException):
        message = {404: "Address not found", 405: "Method not allowed"}
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "message": message[exception.status_code],
                "stacktrace": traceback.format_exc()
            }
        )

    @app.exception_handler(RequestValidationError)
    def validation_exception(request, exception):
        return JSONResponse(
            status_code=422,
            content={
                "message": "Error mapping response object",
                "stacktrace": str(exception)
            }
        )
    return app
