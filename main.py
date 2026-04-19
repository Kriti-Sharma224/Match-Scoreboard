from fastapi import FastAPI
from schemas import MatchInput
from services import build_scorecard

app = FastAPI(title="Match Scoreboard API")

@app.post("/scoreboard")
def scoreboard(data: dict):
    return build_scorecard(data)


# simple health check
@app.get("/")
def home():
    return {"message": "Live Match Scoreboard API running"}