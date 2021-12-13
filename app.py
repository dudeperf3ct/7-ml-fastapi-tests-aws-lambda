from fastapi import FastAPI
from mangum import Mangum

import classifier_router

app = FastAPI()
app.include_router(classifier_router.router)

handler = Mangum(app)

@app.get("/")
async def root():
    return "Sentiment Classifier (0 -> Negative and 1 -> Positive)"


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "dummy check! Classifier is all ready to go!"
