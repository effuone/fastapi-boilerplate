from typing import Any
from pydantic import Field
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router

@router.delete("/{id}")
def delete_post(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
)-> dict[str, str, str]:
    existing_post = svc.repository.get_post_by_id(post_id)
    if not existing_post:
        return Response(status_code=404)
    svc.repository.delete_post(post_id)
    return Response(status_code=204)