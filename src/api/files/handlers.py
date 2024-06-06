from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse


from src.modules.file_saver.handler import file_save
from src.modules.path_worker.handler import PathWorker
from src.utils.verify import verify_file, verify_token


files_router = APIRouter()


@files_router.post("/image/{user_id}", dependencies=[Depends(verify_token)])
async def image_download(user_id: str, file: UploadFile = Depends(verify_file)):
    save_path = PathWorker.generate_path(
        user_id=str(user_id), folder="images", file=file
    )
    await file_save(file=file, save_path=save_path)
    return {"filename": save_path.name, "path": str(save_path)}


@files_router.delete("/", dependencies=[Depends(verify_token)])
async def delete_file(path: str):
    check_path = PathWorker.check_path(save_path=path)
    print(21312312)
    print(path)
    if check_path:
        PathWorker.delete_path(save_path=path)
        return {"message": "File deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="File not found")


@files_router.get("/")
async def get_file(path: str):
    file = Path(path)
    if file.exists() and file.is_file():
        return FileResponse(path=file, filename=file.name)
    else:
        raise HTTPException(status_code=404, detail="File not found")
