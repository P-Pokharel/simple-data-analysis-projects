import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    num_array = np.array(list).reshape(3, 3)

    calculations = {
        "mean": [
            num_array.mean(axis=0).tolist(),
            num_array.mean(axis=1).tolist(),
            num_array.mean().tolist(),
        ],

        "variance": [
            num_array.var(axis=0).tolist(),
            num_array.var(axis=1).tolist(),
            num_array.var().tolist(),
        ],

        "standard deviation": [
            num_array.std(axis=0).tolist(),
            num_array.std(axis=1).tolist(),
            num_array.std().tolist(),
        ],

        "max": [
            num_array.max(axis=0).tolist(),
            num_array.max(axis=1).tolist(),
            num_array.max().tolist(),
        ],

        "min": [
            num_array.min(axis=0).tolist(),
            num_array.min(axis=1).tolist(),
            num_array.min().tolist(),
        ],

        "sum": [
            num_array.sum(axis=0).tolist(),
            num_array.sum(axis=1).tolist(),
            num_array.sum().tolist(),
        ],
    }

    return calculations