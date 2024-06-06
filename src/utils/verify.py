from fastapi import (
    File,
    Request,
    HTTPException,
    UploadFile,
    status,
    HTTPException,
)

from src.settings import SERVICE_TOKEN

from functools import wraps


async def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token"
        )


def handle_dal_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if isinstance(result, dict) and "error" in result:
            status = result.get("status", 500)
            raise HTTPException(status_code=status, detail=result.get("error"))
        return result

    return wrapper


async def verify_file_size(file: UploadFile):
    MAX_FILE_SIZE = 800 * 1024
    content = await file.read()
    file.file.seek(0)
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 800KB limit")
    return file


async def verify_file_format(file: UploadFile):
    allowed_formats = {"image/svg+xml", "image/png", "image/jpeg"}
    if file.content_type not in allowed_formats:
        raise HTTPException(status_code=400, detail="Invalid file format")
    return file


async def verify_file_format(file: UploadFile):
    allowed_formats = {"image/svg+xml", "image/png", "image/jpeg"}
    if file.content_type not in allowed_formats:
        raise HTTPException(status_code=400, detail="Invalid file format")
    return file


async def verify_file(file: UploadFile = File(...)):
    file = await verify_file_format(file)
    file = await verify_file_size(file)
    return file
