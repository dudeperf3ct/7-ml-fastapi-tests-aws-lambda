from fastapi import FastAPI

import classifier_router

app = FastAPI()
app.include_router(classifier_router.router)


@app.get("/")
async def root():
    return "Sentiment Classifier (0 -> Negative and 1 -> Positive)"


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "dummy check! Classifier is all ready to go!"
