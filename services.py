matches = {
    "match1": {
        "batting_team": "RCB",
        "bowling_team": "MI",
        "innings": {
            "runs": 120,
            "wickets": 3,
            "overs": 12.0,
            "batters": [
                {"name": "Virat Kohli", "runs": 55},
                {"name": "Faf du Plessis", "runs": 40}
            ],
            "bowlers": [
                {"name": "Jasprit Bumrah", "wickets": 2},
                {"name": "Mohammed Shami", "wickets": 1}
            ]
        }
    },

    "match2": {
        "batting_team": "CSK",
        "bowling_team": "GT"
    }
}


def calculate_run_rate(runs, overs):
    if overs == 0:
        return 0
    return round(runs / overs, 2)


def get_top_batter(batters):
    if not batters:
        return "N/A"
    top = max(batters, key=lambda x: x["runs"])
    return f'{top["name"]} ({top["runs"]})'


def get_top_bowler(bowlers):
    if not bowlers:
        return "N/A"
    top = max(bowlers, key=lambda x: x["wickets"])
    return f'{top["name"]} ({top["wickets"]})'


def get_match_scorecard(match_id: str):
    match = matches.get(match_id)

    if not match:
        return {"error": "Match not found"}

    if "innings" not in match:
        return {
            "message": "Match exists but innings not started",
            "batting_team": match["batting_team"],
            "bowling_team": match["bowling_team"]
        }

    innings = match["innings"]

    runs = innings["runs"]
    wickets = innings["wickets"]
    overs = innings["overs"]

    run_rate = calculate_run_rate(runs, overs)

    return {
        "match_id": match_id,
        "batting_team": match["batting_team"],
        "bowling_team": match["bowling_team"],
        "live_score": f"{runs}/{wickets}",
        "overs": overs,
        "run_rate": run_rate,
        "top_batter": get_top_batter(innings["batters"]),
        "top_bowler": get_top_bowler(innings["bowlers"])
    }