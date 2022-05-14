import uvicorn

from src.config import config


if __name__ == '__main__':
    uvicorn.run(
        "src.app:app",
        port = config.port,
        host = config.host,
        reload = config.reload
    )