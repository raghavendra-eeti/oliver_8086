def remove_comments(input_file, output_file):

    for line in input_file:
        line_split = line.split('//')
        if line_split[0] != '':
            output_file.write(line_split[0])

def get_tables(source):
    name_table = dict()
    value_table = dict()
    for line in source:
        line_split = line.split()
        if len(line_split) < 2:
            continue
        if line_split[0] == 'byte' or line_split[0] == 'word':
            data_type = line_split[0]
            for i in range(1, len(line_split)):
                str = line_split[i].strip(';')
                if str[0] >= 'A' and str[0] <= 'z':
                    name_table[str] = data_type
                    if i < len(line_split) - 1 and line_split[i + 1] == '=':
                            value_table[str] = line_split[i + 2].strip(', ').strip(';')
                    else:
                        value_table[str] = '?'
    return name_table, value_table

def get_blocks(source):
    stack = []
    label_count = 0
    labels = dict()
    blocks = dict()
    for i in range(len(source)):
        line = source[i]
        if '{' in line:
            labels[i] = 'l' + str(label_count)
            label_count += 1
            stack.append(i)
        if '}'in line:
            start = stack.pop()
            blocks[start] = i
            labels[i] = 'l' + str(label_count)
            label_count += 1

    return labels, blocks