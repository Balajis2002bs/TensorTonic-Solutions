import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x_array,y_array=np.array(x),np.array(y)
    sub_array=np.abs(x_array-y_array)
    sum_array=np.sum(sub_array)
    return float(sum_array)