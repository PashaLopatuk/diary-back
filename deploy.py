import uvicorn


PORT = 8000
HOST = '0.0.0.0'

if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=PORT)
