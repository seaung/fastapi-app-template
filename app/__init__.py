from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    register_db(app)

    register_cors(app)

    register_router(app)

    return app


def register_cors(app: FastAPI) -> None:
    """注册跨域"""
    app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
    )


def register_db(app: FastAPI) -> None:
    """注册数据库"""
    pass


def register_router(app: FastAPI) -> None:
    """注册路由"""
    pass

