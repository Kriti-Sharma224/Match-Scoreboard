def calculate_run_rate(total_runs: int, overs: float):
    if overs == 0:
        return 0
    return round(total_runs / overs, 2)


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


# NEW: process ball events
def process_ball_events(data):
    runs = data["total_runs"]
    wickets = data["total_wickets"]

    for ball in data.get("ball_events", []):
        runs += ball["runs"]
        if ball["wicket"]:
            wickets += 1

    return runs, wickets


def build_scorecard(data):
    updated_runs, updated_wickets = process_ball_events(data)

    run_rate = calculate_run_rate(updated_runs, data["overs"])

    return {
        "live_score": f"{updated_runs}/{updated_wickets}",
        "run_rate": run_rate,
        "top_batter": get_top_batter(data.get("batters", [])),
        "top_bowler": get_top_bowler(data.get("bowlers", [])),
        "balls_processed": len(data.get("ball_events", []))
    }