import numpy as np

def calculations(list_inputs):
    if len(list_inputs) != 9:
        raise ValueError("list don't contain 9 digits")
    
    matrix = np.array(list_inputs).reshape(3,3)


    calculate = {"mean" :[ np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(matrix).item()],
                 "variance":[np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix).item()],
                 "std":[np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix).item()],
                 "max":[np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix).item()],
                 "min":[np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix).item()]}
    
    return calculate




