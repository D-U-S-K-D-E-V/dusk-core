from src.services.api import API
from src.models.http_request import HTTPRequestModel
from src.enums.http_status import HTTPStatusEnum
from fastapi import Request
from starlette.responses import JSONResponse
import secrets

def mock_api():
    api = API(
        initial_key = secrets.token_bytes(32),
        origins=["*"], 
        routers=[]
    )
    api.set_app()
    
    return api

async def mock_call_next(request: Request):
    response_data = HTTPRequestModel(
        status=HTTPStatusEnum.SUCCESS,
        data={
            "message": "successful decryption"
        }
    )
    return JSONResponse(response_data)

def mock_get_request():
    return mock_base_request("get")

def mock_post_request(body):
    return mock_base_request("post", body)

def mock_base_request(method: str, body: any = None):
    if body != None:
        return Request(
            {"type": "http", "method": method, "path": "/test-path"},
            receive=lambda: {"body": body},
        )
    else:
        return Request(
            {"type": "http", "method": method, "path": "/test-path"},
            receive=lambda: {},
        )

def mock_response():
    pass