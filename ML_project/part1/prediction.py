def predict(test_x, test_x_distinct,y_distinct,k_emission):
    y_predict = []

    for i in range(len(test_x)):
        row = test_x_distinct.index(test_x[i])
        max_e = 0
        max_e_index = 0
        for j in range(len(y_distinct)):
            if k_emission[row][j] > max_e:
                max_e = k_emission[row][j]
                max_e_index = j
        y_predict.append(y_distinct[max_e_index])

    return y_predict