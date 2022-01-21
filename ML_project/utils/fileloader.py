def load_data(path):
    f = open(path, 'r', encoding='utf-8')
    sequences = f.read()
    f.close()

    x = ['']
    y = ['START']

    x_distinct = []
    y_distinct = []

    for line in sequences.split('\n'):
        if line != '':
            xi, yi = line.rsplit(' ', 1)
            if xi not in x_distinct:
                x_distinct.append(xi)
            if yi not in y_distinct:
                y_distinct.append(yi)
            x.append(xi)
            y.append(yi)
        if line == '':
            x.append('')
            y.append('STOP')
            x.append('')
            y.append('START')
    if len(x) == len(y):
        length = len(x)       
        for i in range(length):
            index = length - 1 - i
            if y[index] == 'STOP':
                break
        x = x[:index + 1]
        y = y[:index + 1]
    else:
        raise Exception('The length of x is not equal to that of y')
    
    return x,y,x_distinct,y_distinct

def load_x(path):
    f = open(path, 'r', encoding='utf-8')
    sequences = f.read()
    f.close()

    x = []
    x_distinct = []
    x_sequence = []

    for line in sequences.split('\n'):
        if line != '':
            x.append(line)
            if line not in x_distinct:
                x_distinct.append(line)
        x_sequence.append(line)

    return x,x_distinct,x_sequence