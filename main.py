from fastapi import FastAPI
from schemas import MatchRequest
from services import get_match_scorecard

app = FastAPI(title="Match Scoreboard API")

@app.get("/")
def home():
    return {"message": "Match Scoreboard API is running"}

@app.post("/scoreboard")
def scoreboard(data: MatchRequest):
    return get_match_scorecard(data.match_id)