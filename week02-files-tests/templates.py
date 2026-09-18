
# Generatl templates for function definitions
# including Pytest test functions

def good_function_name(
        param1_name : param1_type, 
        param2_name : param2_type, ... etc) -> return_type:
    """Concise description of the purpose of the function.

    Parameters
    ----------
    param1_name : param1_type
        description of param1
    param2_name : param2_type
        description of param1

    Returns
    -------
    Option[return_type]
        description of return value

    Raises
    ------
    ValueError (or whatever exception is raised)
        description....
    """
    pass



# Template for a Pytest test function

def test_good_function_name_describing_test() -> None:
    """brief description"""
    # determine the arguments (inputs) to the function
    result = ... # call the function, saving its return value
    expected = ... # determine the expected result

    assert result == expected

def test_exception_is_raised() -> None:
    """Make sure it raises a ValueError on ..."""
    with pytest.raises(ValueError):
        ... # call to function being tested
