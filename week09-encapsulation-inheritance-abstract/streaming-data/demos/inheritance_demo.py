"""Wednesday's demo. Run from the project root:  python -m demos.inheritance_demo"""

from pathlib import Path

from connectors.broken_examples import FitTrackConnector, ForgetfulConnector, QuietSpotifyConnector
from connectors.pipeline import total_hours
from connectors.sources import NetflixConnector, SpotifyConnector

DATA = Path("data")


def show(hours: dict[str, float]) -> None:
    print({source: round(value, 3) for source, value in hours.items()})


def main() -> None:
    spotify = SpotifyConnector(DATA / "spotify.json")
    netflix = NetflixConnector(DATA / "netflix.csv")
    fittrack = FitTrackConnector(DATA / "fittrack.csv")

    print("1. One function, many connectors")
    show(total_hours([spotify, netflix]))

    print("\n2. A teammate adds FitTrack. total_hours() is untouched (leverages polymorphism!) Nothing crashes.")
    show(total_hours([spotify, fittrack]))
    print("   Workouts of 25 and 32.5 minutes are ~0.96 h, not 0.016. Does that look right?")

    print("\n3. A connector that forgot to override load()")
    try:
        total_hours([spotify, ForgetfulConnector(DATA / "spotify.json")])
    except NotImplementedError as error:
        print("   Failed late, inside total_hours():", error)
    except TypeError as error:  # after Thursday's update the class cannot even be created
        print("   Failed immediately, when the object was created:", error)

    print("\n4. Same method, same signature, different behavior")
    honest, quiet = spotify.load(), QuietSpotifyConnector(DATA / "spotify.json").load()
    print(f"   SpotifyConnector: {len(honest)} sessions | QuietSpotifyConnector: {len(quiet)} sessions")
    print("   Both 'work'. Which can the pipeline trust? Hold that thought.")

if __name__ == '__main__':
    main()
