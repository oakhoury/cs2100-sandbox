import pytest


def get_area_of_rectangle(width: int, height: int) -> int:
    """Returns the area of a rectangle.

    Parameters
    ----------
    width : int
        The width of the rectangle
    height : int
        The height of the rectangle

    Returns
    -------
    int
        The area of the rectangle

    Raises
    ------
    ValueError
        If width or height is negative
    """
    if width < 0 or height < 0:
        raise ValueError("Rectangle dimensions cannot be negative")
    return width * height


def test_3_by_4() -> None:
    """3 by 4 rectangle"""
    assert get_area_of_rectangle(3, 4) == 12


def test_negative_area() -> None:
    """Make sure it raises a ValueError for a negative width"""
    with pytest.raises(ValueError):
        get_area_of_rectangle(-1, 4)


if __name__ == '__main__':
    pytest.main(["rectangle_area.py"]) # or just run `pytest` from the command line


