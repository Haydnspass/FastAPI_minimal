from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # entrypoint for apprunner, because gunicorn directly does not work
    # since apprunner requires synchronous
    # workaround:
    # gunicorn api:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
