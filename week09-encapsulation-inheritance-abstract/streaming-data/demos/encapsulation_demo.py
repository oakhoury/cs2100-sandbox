"""Demo. Run from the project root:  python -m demos.encapsulation_demo"""

from connectors.streaming import StreamingSession, utc_from_iso
from solutions.client import StreamingClient

def main() -> None:
    client = StreamingClient("ana", "s3cr3t-token-123")
    print('\n\n' + '#' * 20 + '  DEMO ' + '#' * 20)
    print(f"\nStreamingClient is a class; example object: \n{client}")
    print("Note how the string masks the token (sensitive information)")
    print("However... \n")

    print("vars(client): ", vars(client), " <-- Python does not enforce privacy!")
    print("\nCONCLUSION: Encapsulation protects code from MISTAKES, not secrets from people who can read the object.")

    # Immutability: a StreamingSession is a tuple, so raw records cannot be edited in place.
    session = StreamingSession(utc_from_iso("2024-09-02T13:00:00Z"), "Neon Harbor", 180.0, "spotify")

    print('\n\nDEMO: named tuple is a tuple')
    print(f"\nA StreamingSession is immutable as it's a named tuple:\nsession = {session}")

    print("\nAttempting to mutate session.seconds...")
    try:
        session.seconds = 5.0  # type: ignore[misc]
    except AttributeError as error:
        print(f"ERROR: session.seconds = 5.0 -> {error}")

    # We can create a copy of StreamingSession with a change to the original's value
    #
    fixed = session._replace(seconds=185.0)  # derive a NEW record instead
    print("original:", session.seconds, "| derived copy:", fixed.seconds)

if __name__ == '__main__':
    main()
