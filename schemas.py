from pydantic import BaseModel
from typing import List

class BallEvent(BaseModel):
    runs: int
    wicket: bool = False

class Batter(BaseModel):
    name: str
    runs: int

class Bowler(BaseModel):
    name: str
    wickets: int

class MatchInput(BaseModel):
    total_runs: int
    total_wickets: int
    overs: float

    batters: List[Batter] = []
    bowlers: List[Bowler] = []

    # NEW: ball-by-ball events
    ball_events: List[BallEvent] = []