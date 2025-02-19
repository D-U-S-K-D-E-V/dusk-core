from pydantic import BaseModel
from enums.http_status import HTTPStatusEnum

class HTTPRequestModel(BaseModel):
    status: HTTPStatusEnum
    data: str