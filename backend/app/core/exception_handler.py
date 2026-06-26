from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        f"Unhandled exception on {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
        },
    )