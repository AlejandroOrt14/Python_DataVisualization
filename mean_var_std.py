import numpy as np

'''
    Dictionay type 
{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
}
'''

# Mean calculation
def calculate_mean(_list, matriz):
    cols = list(np.mean(matriz, axis=0))
    rows = list(np.mean(matriz, axis=1))
    return [ cols, rows, _list.mean() ]

# Variance calculation
def calculate_variance(_list, matriz):
    cols = list(np.var(matriz, axis=0))
    rows = list(np.var(matriz, axis=1))
    return [ cols, rows, _list.var() ]

# Standard deviation calculation
def calculate_standard_deviation(_list, matriz):
    cols = list(np.std(matriz, axis=0))
    rows = list(np.std(matriz, axis=1))
    return [ cols, rows, _list.std() ]

# Max calculation
def calculate_max(_list, matriz):
    cols = list(np.max(matriz, axis=0))
    rows = list(np.max(matriz, axis=1))
    return [ cols, rows, _list.max() ]

# Min calculation
def calculate_min(_list, matriz):
    cols = list(np.min(matriz,axis=0))
    rows = list(np.min(matriz,axis=1))    
    return [ cols, rows, _list.min() ]

# Sum calculation
def calculate_sum(_list, matriz):
    cols = list(np.sum(matriz,axis=0))
    rows = list(np.sum(matriz,axis=1))
    return [cols, rows, _list.sum()]

# Main Function
def calculate(*args):
    _list = np.array(args[0])
    matriz = _list.reshape(3,3)

    if len(_list) < 9:
        print(len(_list))
        raise ValueError("List must contain nine numbers.")
    else:
        _mean = calculate_mean(_list, matriz)
        _variance = calculate_variance(_list, matriz)
        _standard_deviation = calculate_standard_deviation(_list, matriz)
        _max = calculate_max(_list, matriz)
        _min = calculate_min(_list, matriz)
        _sum = calculate_sum(_list, matriz)
        dictionary = {
                        'mean': _mean, 
                        'variance': _variance, 
                        'standard deviation': _standard_deviation, 
                        'max': _max, 
                        'min': _min, 
                        'sum': _sum
                     }
        print(dictionary)

calculate([0,1,2,3,4,5,6,7,8])