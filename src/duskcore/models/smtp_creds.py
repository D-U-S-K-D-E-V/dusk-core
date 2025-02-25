from pydantic import BaseModel

class SmtpCredsModel(BaseModel):
    address: str
    password: str
    smtp_port: int
    smtp_server: str