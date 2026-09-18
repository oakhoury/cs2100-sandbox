"""Module providing the unit testing mechanism."""
import pytest

def repeat_three_inputs() -> None:
    """Reads three inputs from the user and prints them."""
    for _ in range(3):
        user_input = input("Enter something: ")
        print(user_input)


def test_repeat_three_inputs(monkeypatch : pytest.MonkeyPatch,
                             capsys : pytest.CaptureFixture[str]) -> None:
    '''Test that repeat_three_inputs correctly reads and prints three inputs.

    Parameters
    -----------
    monkeypatch : pytest.MonkeyPatch
        a Pytest fixture used to bypass input() for testing
    capsys : pytest.CaptureFixture[str])
        a Pytest fixture used to capture system output for testing
    '''

    # A list for the values that imitate inputs by the user
    mock_inputs = ['first thing typed by user', 'second thing', 'third thing']

    # Make the list an iterable object (more on this later!!)
    responses = iter(mock_inputs)

    # Setup the monkeypatch fixture to grab the next item in the iterator (list)
    monkeypatch.setattr('builtins.input', lambda prompt="": next(responses))

    # Calls the function being tested... note it uses input() and print()
    repeat_three_inputs()

    # The output to console was captured internally by Pytest capsys and kept in memory
    # The following call takes it from memory (a buffer) so we can inspect it
    captured = capsys.readouterr()

    assert captured.out == '\n'.join(mock_inputs) + '\n'   # '\n'.join(['A', 'A', 'A']) + '\n'   
