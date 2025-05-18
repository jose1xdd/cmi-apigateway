import uvicorn

from app.utils.enviroment import enviroment


def start_server():
    port = int(enviroment.get('PORT'))
    uvicorn.run("app:create_app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__":
    start_server()