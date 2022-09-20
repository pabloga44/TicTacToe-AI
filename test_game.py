import functions
import sys

def test_input_coordinates():
    """Test the inputation of coordinates by the user"""

    sys.stdin = open("test_inputs/test_input_coordinates.txt") # We choose the same name for organization
    i,j = functions.input_coordinates()
    assert i in [0,1,2]
    assert j in [0,1,2]

