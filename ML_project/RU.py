from part1.emission import training_emission_parameters, k_emission_parameters
from part1.prediction import predict
from part2.transition import training_transition_parameter
from utils.fileloader import load_data, load_x
from utils.output import write_output_from_emission, write_output_from_viterbi, write_fifth_best_output
from part4.refine import re_k_emission_parameters
print('[Part 1] Gnerating emssion matrix for RU train set')
x,y,x_distinct,y_distinct = load_data('data/RU/train')
count_uo, count_u, emission = training_emission_parameters(x,y,x_distinct,y_distinct)
print(emission)
print('[Part 1] Gnerating emssion matrix for RU dev.in')
test_x,test_x_distinct,test_x_sequence = load_x('data/RU/dev.in')
k_emission = k_emission_parameters(count_uo, count_u, 1, x_distinct, test_x_distinct, y_distinct)
print(k_emission)
print('[Part 1] Find the y to maximize e(x|y)')
y_predict = predict(test_x, test_x_distinct,y_distinct,k_emission)
write_output_from_emission(test_x, y_predict, 'result/RU/dev.p1.out', test_x_sequence)
print('[Part 2] Gnerating transition matrix for RU train set')
count_vu, count_v, transition = training_transition_parameter(y, y_distinct)
print(transition)
print('[Part 2] Find the best label sequence by viterbi algorithm')
write_output_from_viterbi('result/RU/dev.p2.out', transition, k_emission, test_x_distinct, test_x_sequence, y_distinct)
print('[Part 3] Find the 5th best label sequence by improved viterbi algorithm')
write_fifth_best_output('result/RU/dev.p3.out', transition, k_emission, test_x_distinct, test_x_sequence, y_distinct)
print('[Part 4] Find the best label sequence by improved viterbi algorithm')
re_k_emission = re_k_emission_parameters(x, y, test_x, x_distinct, test_x_distinct, y_distinct)
write_output_from_viterbi('result/RU/dev.p4.out', transition, re_k_emission, test_x_distinct, test_x_sequence, y_distinct)
print('[Part 4] Find the best label sequence by improved viterbi algorithm for the test set')
new_test_x,new_test_x_distinct,new_test_x_sequence = load_x('data/RU/test.in')
test_k_emission = re_k_emission_parameters(x, y, new_test_x, x_distinct, new_test_x_distinct, y_distinct)
write_output_from_viterbi('result/RU/test.p4.out', transition, test_k_emission, new_test_x_distinct, new_test_x_sequence, y_distinct)