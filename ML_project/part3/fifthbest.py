import numpy as np
from utils.cartesian import Cartesian
from utils.calc import calculate_path_score
from part2.viterbi import viterbi

def fifth_viterbi(transition_probability,emission_probability,obs_seq, y_distinct):
    pis, y_predict_label, y_pre = viterbi(transition_probability,emission_probability,obs_seq, y_distinct)

    y_pre = []
    pi = pis.transpose()
    
    pi_stop = pi[len(obs_seq)]
    max_stop = np.max(pi_stop)
    y_pre.append(np.where(pi_stop == max_stop)[0][0])

    for j in range(len(obs_seq) - 1):
        index = len(obs_seq) - j - 2
        pi_array = pi[index]
        pi_temp = []
        for u in range(len(pi_array)):
            y_plus_one_index = y_pre[j]
            pi_temp.append(pi_array[u] * emission_probability[index + 1][y_plus_one_index] * transition_probability[u + 1][y_plus_one_index])
        max_pi = max(pi_temp)
        y_pre.append(pi_temp.index(max_pi))
         
    y_pre.reverse()

    results = {}

    exist_path = []
    
    for i in range(len(obs_seq)):
        path_array = []
        combs = []
        for j in range(i + 1, len(obs_seq)):
            path_array.append(y_pre[j])
        for m in range(i + 1):
            possible_index = []
            possible_index.append(str(y_pre[m]))
            for j in range(len(y_distinct)):
                if emission_probability[m][j] != 0 and pis[j][m] != 0 and j != int(y_pre[m]):
                    possible_index.append(str(j))
            combs.append(possible_index)
        if len(obs_seq) > 30:
            for loc, items in enumerate(combs):
                if loc > 0 and loc < len(obs_seq) - 1:
                    x_remove = []
                    for x in range(len(items)):
                        if transition_probability[int(items[x]) + 1][y_pre[loc + 1]] == 0 or transition_probability[y_pre[loc] + 1][int(items[x])] == 0:
                            x_remove.append(items[x])
                    x_remove = list(set(x_remove))
                    if len(x_remove) != 0:
                        for remove_x in x_remove:
                            items.remove(remove_x)
        cartesian = Cartesian(combs)
        possible_com = cartesian.assemble()
        for comb in possible_com:
            temp_array = []
            for l in range(len(comb)):
                temp_array.append(comb[l])
            for n in range(len(path_array)):
                temp_array.append(path_array[n])
            key = ';'.join(str(v) for v in temp_array)
            if key not in exist_path:
                exist_path.append(key)
                path_score = calculate_path_score(transition_probability, emission_probability, temp_array, y_distinct)
                if path_score!= 0:
                    if path_score in results.values():
                        previous_key_index = list(results.values()).index(path_score)
                        previous_key = list(results.keys())[previous_key_index]
                        if previous_key != key:
                            key += ";"
                            key += previous_key
                    results[key] = path_score
            if len(results) > 5:
                break
        if len(results) > 5:
            break

    sorted_combination = sorted(results.items(), key=lambda x: x[1], reverse=True)
    if len(results) >= 5:
        ans = sorted_combination[4][0]
        result_pairs = []
        result_seq = ans.split(';')
        for l in range(int(len(result_seq) / len(obs_seq))):
            y_predict = []
            for j in range(len(obs_seq)):
                y_predict.append(y_distinct[int(result_seq[l * len(obs_seq) + j])])
            result_pairs.append(y_predict)
    else:
          result_pairs = []
    return sorted_combination,result_pairs