import httpx

BASE_URL = "https://api.jolpi.ca/ergast/f1"


async def get_next_race() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/current/next.json")
        response.raise_for_status()
        data = response.json()

    race = data["MRData"]["RaceTable"]["Races"][0]
    return {
        "name": race["raceName"],
        "circuit": race["Circuit"]["circuitName"],
        "country": race["Circuit"]["Location"]["country"],
        "date": race["date"],
        "time": race.get("time", "время неизвестно"),
    }


async def get_driver_standings(top_n: int = 5) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/current/driverStandings.json")
        response.raise_for_status()
        data = response.json()

    standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    result = []
    for entry in standings[:top_n]:
        driver = entry["Driver"]
        result.append({
            "position": entry["position"],
            "name": f"{driver['givenName']} {driver['familyName']}",
            "points": entry["points"],
        })
    return result