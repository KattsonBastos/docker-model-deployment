import pickle

def load_pickle(file_pkl):
    """Receives a path of a pickle file and loads it.
    :param file_pkl: str referencing a .pkl file
    :returns: the object loaded"""
    
    with open(file_pkl,'rb') as open_file:

        object = pickle.load(open_file)
        
    return object