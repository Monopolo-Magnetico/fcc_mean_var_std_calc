import numpy as np

def calculate(test_list: list):
    
    if len(test_list) < 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.zeros((0, 3))  # Inicialize an empty array of dimensions 0x3
    for i in range(0, len(test_list), 3):
        dum = np.array(test_list[i:i+3]).reshape(1, 3)  # Reshape dum to 1x3
        arr = np.concatenate((arr, dum), axis=0)  # Concatenate on first dimension (rows)

    flat_arr = arr.flatten()

    mean = []
    var = []
    std = []
    max_list = []
    min_list = []
    sum_list = []

    calculations = {}

    flat_arr_mean = np.mean(flat_arr)
    flat_arr_var = np.var(flat_arr)
    flat_arr_std = np.std(flat_arr)
    flat_arr_max = np.max(flat_arr)
    flat_arr_min = np.min(flat_arr)
    flat_arr_sum = np.sum(flat_arr)

    mean_drow = []
    mean_dcol = []
    var_drow = []
    var_dcol = []
    std_drow = []
    std_dcol = []
    max_drow = []
    max_dcol = []
    min_drow = []
    min_dcol = []
    sum_drow = []
    sum_dcol = []

    for c in range(0, 3):
        mean_row = np.mean(arr[c, :])
        mean_col = np.mean(arr[:, c])
        var_row = np.var(arr[c, :])
        var_col = np.var(arr[:, c])
        std_row = np.std(arr[c, :])
        std_col = np.std(arr[:, c])
        max_row = np.max(arr[c, :])
        max_col = np.max(arr[:, c])
        min_row = np.min(arr[c, :])
        min_col = np.min(arr[:, c])
        sum_row = np.sum(arr[c, :])
        sum_col = np.sum(arr[:, c])
        
        mean_drow.append(mean_row)
        mean_dcol.append(mean_col)
        var_drow.append(var_row)
        var_dcol.append(var_col)
        std_drow.append(std_row)
        std_dcol.append(std_col)
        max_drow.append(max_row)
        max_dcol.append(max_col)
        min_drow.append(min_row)
        min_dcol.append(min_col)
        sum_drow.append(sum_row)
        sum_dcol.append(sum_col)

    mean.append(mean_dcol)
    mean.append(mean_drow)
    mean.append(flat_arr_mean)
    var.append(var_dcol)
    var.append(var_drow)
    var.append(flat_arr_var)
    std.append(std_dcol)
    std.append(std_drow)
    std.append(flat_arr_std)
    max_list.append(max_dcol)
    max_list.append(max_drow)
    max_list.append(flat_arr_max)
    min_list.append(min_dcol)
    min_list.append(min_drow)
    min_list.append(flat_arr_min)
    sum_list.append(sum_dcol)
    sum_list.append(sum_drow)
    sum_list.append(flat_arr_sum)

    calculations['mean'] = mean
    calculations['variance'] = var
    calculations['standard deviation'] = std
    calculations['max'] = max_list
    calculations['min'] = min_list
    calculations['sum'] = sum_list

    return calculations