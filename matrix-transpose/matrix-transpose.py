import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    # A.shape
    A_array=np.array(A)
    trans_rray=A_array.T
    return trans_rray
