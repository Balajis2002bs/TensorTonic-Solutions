import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    x_array,y_array=np.array(x),np.array(y)
    dot_prod_array=x_array * y_array
    sum=np.sum(dot_prod_array)
    
    return float(sum)