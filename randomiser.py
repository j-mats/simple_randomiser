import numpy as np

def randomiser(n, data):
    """
    Function to generate 'n' non-repeating random numbers within a given 1D dataset.

    Parameters
    ----------
    n : int
        The number of random values to be generated.
    
    data : array
        The dataset from which the random values are generated.

    Output
    ----------
    random_values_array : array 
        Output of all the randomly generated integer values in an array.

    Created by: Job M
    """

    if n > len(set(data)): 
        raise ValueError("'n' exceeds the number of unique values in dataset")
    
    if n > 0:
        random_values_array = np.zeros(n)
    elif n <= 0:
        raise ValueError("'n' should be non-zero and non-negative integer")
    
    repeat_checker = set()
    element_length = 0
    counter = 0 
    while element_length < n:
        r = np.random.randint(len(data)) #random state
        if data[r] not in repeat_checker:
            random_values_array[element_length] = data[r]
            repeat_checker.add(data[r])
            element_length += 1
        else:
            if counter > 100: raise RecursionError('Recursion limit (100 iterations) exceeded')
            counter += 1
            
    return np.int32(random_values_array)
