def season_active(history):

    if len(history) < 5:
        return True

    recent = history[-5:]

    active_days = 0

    for day in recent:
        for r in day["resorts"]:
            if r["lifts_open"] > 0:
                active_days += 1
                break

    return active_days > 0
