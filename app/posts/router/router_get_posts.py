from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router

class GetPostsResponse(AppModel):
    posts: list

@router.get("/", response_model=GetPostsResponse)
def get_posts(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetPostsResponse:
    return GetPostsResponse(
        posts=svc.repository.get_posts()
    )
