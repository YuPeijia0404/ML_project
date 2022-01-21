import numpy as np

def training_transition_parameter(y, y_distinct):
    length = len(y_distinct) + 1
    count_vu = np.zeros((length, length))
    count_v = np.zeros(length)
    transition = np.zeros((length, length))

    rows = ['START']
    columns = []
    for i in range(len(y_distinct)):
        rows.append(y_distinct[i])
        columns.append(y_distinct[i])
    columns.append('STOP')

    for i in range (len(y)):
        yi = y[i]
        if yi != 'STOP':
            row = rows.index(yi)
            yi_plus_one = y[i + 1]
            column = columns.index(yi_plus_one)
            count_vu[row][column] += 1
            count_v[row] += 1

    for i in range(length):
        for j in range(length):
            transition[i][j] = count_vu[i][j] / count_v[i]

    return count_vu,count_v,transition