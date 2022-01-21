def calculate_path_score(trainsition_probability, emission_probability, path, y_distinct):
    path_score = 1 * emission_probability[0][path[0]] * trainsition_probability[0][path[0]] * 1000
    for i in range(1, len(path) - 1):
        path_score *= emission_probability[i][path[i]] * trainsition_probability[path[i - 1] + 1][path[i]] * 1000
    path_score *= trainsition_probability[path[len(path) - 1] + 1][len(y_distinct)] * 1000
    return path_score