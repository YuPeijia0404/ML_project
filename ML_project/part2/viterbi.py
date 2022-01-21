import numpy as np

def build_emission_probability_matrix(k_emission, x_distinct, ob_sequence, y_length):
    row_length = len(ob_sequence)
    KE = np.zeros((row_length, y_length))
    for i in range(row_length):
        xi = ob_sequence[i]
        row = x_distinct.index(xi)
        KE[i] = k_emission[row]
    return KE

def viterbi(transition_probability,emission_probability,obs_seq, y_distinct):
    rows = ['START']
    columns = []
    for i in range(len(y_distinct)):
        rows.append(y_distinct[i])
        columns.append(y_distinct[i])
    columns.append('STOP')

    pis = np.zeros((len(y_distinct), len(obs_seq) + 1))
    
    for u in range(len(y_distinct)):
        pis[u][0] = 1 * emission_probability[0][u] * transition_probability[0][u] * 1000

    for j in range(2, len(obs_seq) + 1):
        pi_matrix = np.zeros((len(y_distinct), len(y_distinct)))
        for v in range(len(y_distinct)):
            for u in range(len(y_distinct)):
                pi_matrix[v][u] = pis[v][j - 2] * emission_probability[j - 1][u] * transition_probability[v + 1][u] * 1000
        uv_matrix = pi_matrix.transpose()
        for u in range(len(y_distinct)):
            pi_array = uv_matrix[u]
            max_pi = np.max(pi_array)
            pis[u][j - 1] = max_pi

    for u in range(len(y_distinct)):
        pis[u][len(obs_seq)] = pis[u][len(obs_seq) - 1] * transition_probability[u + 1][len(y_distinct)] * 1000

    y_pre = []
    pi = pis.transpose()
    
    pi_stop = pi[len(obs_seq)]
    max_stop = np.max(pi_stop)
    y_pre.append(np.where(pi_stop == max_stop)[0][0])

    for index in range(len(obs_seq) - 1):
        col = len(obs_seq) - index - 2
        pi_array = pi[col]
        pi_temp = []
        for u in range(len(pi_array)):
            y_n_plus_one = y_pre[index]
            pi_temp.append(pi_array[u] * emission_probability[col + 1][y_n_plus_one] * transition_probability[u + 1][y_n_plus_one])
        max_pi = max(pi_temp)
        y_pre.append(pi_temp.index(max_pi))

    y_pre.reverse()

    y_predict = []
    for i in range(len(obs_seq)):
        y_predict.append(y_distinct[y_pre[i]])

    return pis, y_predict, y_pre