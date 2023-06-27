from typing import Any
from pydantic import Field
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router


class GetPostResponse(AppModel):
    id: Any = Field(alias="_id")
    city: str
    message: str


@router.get("/{id}", response_model=GetPostResponse)
def get_post_by_id(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
)-> dict[str, str, str]:
    post = svc.repository.get_post_by_id(post_id)
    return post