from pydantic import BaseModel

class MailModel(BaseModel):
    firstname: str
    lastname: str
    subject: str
    company: str
    email: str
    message: str