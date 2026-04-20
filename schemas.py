from pydantic import BaseModel

class MatchRequest(BaseModel):
    match_id: str