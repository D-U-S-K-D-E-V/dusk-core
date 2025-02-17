from pydantic import BaseModel
from enums.http_status_enum import HTTPStatusEnum

class HTTPRequestModel(BaseModel):
    status: HTTPStatusEnum
    data: any