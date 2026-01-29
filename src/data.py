import numpy as np
import os

PATH_DATA = 'data'

# This file should contain code related to working with the data and nothing else

def make_data (n: int = 100, low: int = 0, high: int = 24) -> np.array:
    '''
    Return an nx2 array of random integers between low and high (inclusive)
    '''
    return np.random.randomint(low = low, high = high, size = (n, 2))

def save_data (data: np.array, filename: str):
    '''
    Save a numpy array to the default output folder,
    ensuring that the folder exists.
    '''
    full_filename = os.path.join (PATH_DATA, filename)

    # Ensure the output directory exists
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)

    if type(data) != np.ndarray:
        raise TypeError (f'data should be a numpy array, but a {type(data)} was provided.')
    
    # Don't ovewrite an existing file
    if os.path.exists (full_filename):
        raise FileExistsError(f'file {full_filename} already exists.')
    
    # Save the array as a .npy file
    np.save(full_filename, data)
    return None

def load_data(filename: str) -> np.ndarray:
    '''
    Loads data from an .npy file located in the default data directory.
    '''
    return np.load(os.path.join(PATH_DATA, filename))