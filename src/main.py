from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pages.router import router as pages_router
from search_drv.router import router as search_drv_router

app = FastAPI(
    title="Graphical interface"
)

app.include_router(pages_router)
app.include_router(search_drv_router)

app.mount('/static', StaticFiles(directory='pages/static'), name='static')

@app.get('/ping')
def ping():
    response = 'pong'
    return {"response": response, "code": 200}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

