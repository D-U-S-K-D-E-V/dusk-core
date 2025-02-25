from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from security.key_store import KeyStore

class API():
    def __init__(self, origins: list[str], routers: list[APIRouter], secure_mode=True):
        self.key_store = KeyStore()
        self.origins = origins
        self.routers = routers
        self._app = None
        self.key_store = None
        self.secure_mode = secure_mode

    def set_app(self):
        if self._app == None:
            app = FastAPI()
            app.add_middleware(
                CORSMiddleware,
                allow_origins=self.origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            )

            for route in self.routers:
                app.include_router(route)

            self.app = app
        else:
            raise 

    def get_app(self):
        return self._app