# Steps to run the code
* Make sure that you run the code on macOS or Ubuntu System. DO NOT use Windows system, because it cannot read the text properly with any en-coding.
* cd `/ML_project`
* Replace the path in `load_data(path_of_train)` and `load_x(path_of_dev.in)` in `ES.py` and `RU.py`
* Replace the path in `write_output_from_emission()` to be `'path_of_dev.p1.out'`, `write_output_from_viterbi()` to be `'path_of_dev.p2.out', 'path_of_dev.p4.out', 'path_of_test.p4.out'`, and `write_fifth_best_output()` to be `'path_of_dev.p3.out'` in `ES.py` and `RU.py` 
* Type `python3 ES.py` in the command line to get all the output for language `ES`, and type `python3 RU.py` in the command line for language `RU`
* Currently, the results are under `ML_project/result/ES` and `ML_project/result/RU`