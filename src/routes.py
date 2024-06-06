from fastapi.routing import APIRouter
from src.api.files.handlers import files_router


# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance

main_api_router.include_router(files_router, prefix="/v1/files", tags=["files"])
