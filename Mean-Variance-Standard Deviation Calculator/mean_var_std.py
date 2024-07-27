import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError(
            "List must contain nine numbers."
        )
    
    calculations = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
        }
    
    nparray = np.array(list, dtype=int).reshape(3,3)
    print("\n",nparray)

    calculations['mean'].append(nparray.mean(axis=0).tolist())
    calculations['mean'].append(nparray.mean(axis=1).tolist())
    calculations['mean'].append(nparray.mean().tolist())
                
    calculations['variance'].append(nparray.var(axis=0).tolist())
    calculations['variance'].append(nparray.var(axis=1).tolist())
    calculations['variance'].append(nparray.var().tolist())
            
    calculations['standard deviation'].append(nparray.std(axis=0).tolist())
    calculations['standard deviation'].append(nparray.std(axis=1).tolist())
    calculations['standard deviation'].append(nparray.std().tolist())

    calculations['max'].append(nparray.max(axis=0).tolist())
    calculations['max'].append(nparray.max(axis=1).tolist())
    calculations['max'].append(nparray.max().tolist())

    calculations['min'].append(nparray.min(axis=0).tolist())
    calculations['min'].append(nparray.min(axis=1).tolist())
    calculations['min'].append(nparray.min().tolist())

    calculations['sum'].append(nparray.sum(axis=0).tolist())
    calculations['sum'].append(nparray.sum(axis=1).tolist())
    calculations['sum'].append(nparray.sum().tolist())

    
    print("\n",calculations)


    return calculations
