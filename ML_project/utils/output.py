from part2.viterbi import build_emission_probability_matrix, viterbi
from part3.fifthbest import fifth_viterbi

def write_output_from_emission(test_x, y_predict, output_path, x_sequence):
    f = open(output_path, 'w')
    result = ''
    append_index = 0
    if len(test_x) == len(y_predict):
        for i in range(len(x_sequence)):
            if x_sequence[i] == '':
              result += '\n'
            else:
              result += test_x[append_index] + ' ' + y_predict[append_index] + '\n'
              append_index += 1
            f.write(result)
            result = ''
    else:
        raise Exception('The length of x is not equal to that of predict_y')
    f.close()

def write_output_from_viterbi(output_path, transition, k_emission, x_distinct, x_sequence, y_distinct):

    f = open(output_path, 'w')
    obs_seq = []
    result = ''
    for i in range(len(x_sequence)):
        if(x_sequence[i] == '' and i != 0 and i != (len(x_sequence) - 1)):
            emission_probability = build_emission_probability_matrix(k_emission, x_distinct, obs_seq, len(y_distinct))
            pis, y_predict, y_pre = viterbi(transition,emission_probability,obs_seq, y_distinct)
            for j in range(len(obs_seq)):
                if(len(obs_seq) == len(y_predict)):
                    result += obs_seq[j] + ' ' + y_predict[j] + '\n'
                else:
                    raise Exception('length of y_predict and observed sequence is not match')
                f.write(result)
                result = ''
            f.write('\n')
            obs_seq = []
        else:
            obs_seq.append(x_sequence[i])

    f.close()

def write_fifth_best_output(output_path, transition, k_emission, x_distinct, x_sequence, y_distinct):

    f = open(output_path, 'w')
    obs_seq = []
    result = ''
    for i in range(len(x_sequence)):
        if(x_sequence[i] == '' and i != 0 and i != (len(x_sequence) - 1)):
            emission_probability = build_emission_probability_matrix(k_emission, x_distinct, obs_seq, len(y_distinct))
            sorted_combination, y_predict = fifth_viterbi(transition,emission_probability,obs_seq, y_distinct)
            for j in range(len(obs_seq)):
                if len(y_predict) != 0:
                    for l in range(len(y_predict)):
                        if(len(obs_seq) == len(y_predict[l])):
                            result += obs_seq[j] + ' ' + y_predict[l][j] + '\n'
                        else:
                            raise Exception('length of y_predict and observed sequence is not match')
                f.write(result)
                result = ''
            f.write('\n')
            obs_seq = []
        else:
            obs_seq.append(x_sequence[i])

    f.close()