import pre_process
import compile
import sys

input_file_name = input('input file name : ')
output_file_name = input('output file name : ')

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

source = input_file.readlines()

nametab, valtab = pre_process.get_tables(source)
labels, blocks = pre_process.get_blocks(source)
compile.write_variables(nametab, valtab, output_file)



for_stack = []
if_stack = []
for i in range(len(source)):

    line = source[i]
    string = ''
    if line[:4] == 'byte' or line[:4] == 'word':
        continue

    if '()' in line:
        string = compile.functions[line[:-1]]
        output_file.write(string)
        continue

    #end for
    if len(for_stack) > 0 and for_stack[-1][0] == i:
        _, start_label, updation = for_stack.pop()
        string += updation
        string += 'jmp ' + start_label + '\n'
        string += labels[i] + ':\n'

    if len(if_stack) > 0 and if_stack[-1] == i:
        string = labels[i] + ':\n'

    #check if
    if line[:2] == 'if':
        end = blocks[i + 1]
        string += compile.get_condition(line[3:-1], labels[end])
        if_stack.append(end)

    #check for
    elif line[:3] == 'for':
        end = blocks[i + 1]
        line_split = line[4:-2].split(';')
        initialization = line_split[0]
        condition = line_split[1]
        updation = line_split[2]
        string += compile.assignment(initialization)
        string += str(labels[i + 1]) + ':\n' + compile.get_condition(condition, labels[end])
        for_stack.append([end, labels[i + 1], compile.assignment(updation)])

    #check assignment
    else:
        string += compile.assignment(line)
    output_file.write(string)

output_file.write('\nmov ah, 4ch\nint 21h\n\nend\n')