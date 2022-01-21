import numpy as np

def training_emission_parameters(x,y,x_distinct,y_distinct):
    count_uo = np.zeros((len(x_distinct), len(y_distinct)))
    count_u = np.zeros(len(y_distinct))
    emission = np.zeros((len(x_distinct), len(y_distinct)))

    for i in range(len(x)):
        xi = x[i]
        if xi != '':
            yi = y[i]
            row = x_distinct.index(xi)
            col = y_distinct.index(yi)
            count_uo[row][col] += 1
            count_u[col] += 1

    for i in range(len(x_distinct)):
        for j in range(len(y_distinct)):
            emission[i][j] = count_uo[i][j] / count_u[j]
    
    return count_uo, count_u, emission

def k_emission_parameters(count_uo, count_u, k, train_x_distinct, test_x_distinct, y_distinct):
    k_emission = np.zeros((len(test_x_distinct), len(y_distinct)))
    for i in range(len(test_x_distinct)):
        for j in range(len(count_u)):
            if test_x_distinct[i] in train_x_distinct:
                row = train_x_distinct.index(test_x_distinct[i])
                k_emission[i][j] = count_uo[row][j] / (count_u[j] + k)
            else:
                k_emission[i][j] =  k / (count_u[j] + k)
    
    return k_emission
