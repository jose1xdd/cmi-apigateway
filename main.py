import os
import uvicorn

from app.utils.config_loader.config_loader import ConfigLoader, MissingEnvVarError


def start_server():
    loader = ConfigLoader()
    port = int(loader.get('PORT'))
    uvicorn.run("app:create_app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__":
    start_server()