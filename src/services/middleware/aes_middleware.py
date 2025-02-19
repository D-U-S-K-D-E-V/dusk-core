from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from services.api import API
from AesEverywhere import aes256
import json

class AESMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: API):
        super().__init__(app)
        self.key_store = app.key_store

    async def dispatch(self, request: Request, call_next):
        try:
            secret_key = self.key_store.get_key()
            body = await request.body()
            if body:
                decrypted_data = aes256.decrypt(body, secret_key)
                request_data = json.loads(decrypted_data)
                request._body = json.dumps(request_data).encode('utf-8')
                
        except Exception as e:
            return Response(content=str(e), status_code=400)

        response = await call_next(request)

        try:
            response_body = [section async for section in response.body_iterator]
            response_body = b''.join(response_body)
            encrypted_data = aes256.encrypt(response_body, secret_key)
            response.body_iterator = iter([encrypted_data])
            response.headers['Content-Length'] = str(len(encrypted_data))
        except Exception as e:
            return Response(content=str(e), status_code=500)

        return response
        
