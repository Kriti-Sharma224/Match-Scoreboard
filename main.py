from fastapi import FastAPI
from schemas import MatchInput
from services import build_scorecard

app = FastAPI()

@app.post("/scoreboard")
def scoreboard(data: MatchInput):
    return build_scorecard(data.dict())


# simple health check
@app.get("/")
def home():
    return {"message": "Live Match Scoreboard API running"}