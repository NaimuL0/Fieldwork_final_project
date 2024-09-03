from fastapi import FastAPI
import uvicorn

from app.routers import news, summary

app = FastAPI()

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "The Dailystar News Summary API Assignment"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8011, reload=True)