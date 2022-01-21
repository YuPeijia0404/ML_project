import numpy as np

def re_k_emission_parameters(train_x, train_y, test_x, train_x_distinct, test_x_distinct, y_distinct):
    count_uo = np.zeros((len(test_x_distinct), len(y_distinct)))
    count_u = np.zeros(len(y_distinct))
    k_emission = np.zeros((len(test_x_distinct), len(y_distinct)))

    for i in range(len(train_x)):
        xi = train_x[i]
        if xi != '' and xi in test_x_distinct:
            yi = train_y[i]
            row = test_x_distinct.index(xi)
            col = y_distinct.index(yi)
            count_uo[row][col] += 1
            count_u[col] += 1
    for i in range (len(test_x)):
        xi = test_x[i]
        if xi != '' and xi not in train_x_distinct:
            row = test_x_distinct.index(xi)
            for j in range(len(y_distinct)):
                count_uo[row][j] += 1 / len(y_distinct)
                count_u[j] += 1 / len(y_distinct)

    for i in range(len(test_x_distinct)):
        for j in range(len(y_distinct)):
            k_emission[i][j] = count_uo[i][j] / count_u[j]
    
    return k_emission
