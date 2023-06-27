from typing import Any
from pydantic import Field
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router

class UpdatePostRequest(AppModel):
    city: str
    message: str

class UpdatePostResponse(AppModel):
    id: Any = Field(alias="_id")
    city: str
    message: str


@router.patch("/{id}", status_code=200)
def update_post(
    post_id: str,
    input: UpdatePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    existing_post = svc.repository.get_post_by_id(post_id)
    if not existing_post:
        return Response(status_code=404, content="Post not found")
    svc.repository.update_post(post_id, input.dict())
    return Response(status_code=204)