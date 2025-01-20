from fastapi import FastAPI

from app.router import routers


class InitializeRouter:
    def __init__(self, app: FastAPI):
        self.app = app

        for prefix, router in routers.items():
            self.app.include_router(router=router, prefix="/api/v1", tags=[prefix])
