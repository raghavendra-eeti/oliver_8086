import sys

removed_single_line_comments_count = 0
removed_multi_line_comments_count = 0

def remove_single_line_comment(line):
    split_line = line.split('//')
    if len(split_line) == 1:
        return False
    return split_line[0]

def remove_multi_line_comment_start(line):
    split_line = line.split('/*')
    if len(split_line) == 1:
        return False
    return split_line[0]

def remove_multi_line_comment_end(line):
    split_line = line.split('*/')
    if len(split_line) == 1:
        return False
    return_string = ''
    for i in range(1, len(split_line)):
        return_string += split_line[i]
    return return_string


#Read input file from shell arguments
input_file_name = sys.argv[1]
print('Successfully read file : ' + input_file_name)
output_file_name = input_file_name[:len(input_file_name) - 2] + '_no_comments.c'
print('Successfully created file : ' + output_file_name)

#Initialize INPUT and OUTPUT file pointers
with open(input_file_name, 'r') as input_file_pointer:
    input_file_lines = input_file_pointer.readlines()
    output_file_lines = []

    #Remove commented lines
    open_multi_line_comment = False
    for line in input_file_lines:

        if open_multi_line_comment:
            result = remove_multi_line_comment_end(line)
            if result != False:
                open_multi_line_comment = False
                removed_multi_line_comments_count += 1
                result = remove_single_line_comment(result)
                if result != False:
                    output_file_lines.append(result)
            continue

        result = remove_multi_line_comment_start(line)
        if result != False:
            output_file_lines.append(result)
            open_multi_line_comment = True
            continue

        single_line_comment = remove_single_line_comment(line)
        if single_line_comment != False:
            removed_single_line_comments_count += 1
            output_file_lines.append(single_line_comment)
        else:
            output_file_lines.append(line)

print('Successfully deleted all comments')
#Save output file
with open(output_file_name, 'w') as output_file_pointer:
    for line in output_file_lines:
        if line != '\n':
            output_file_pointer.write(line)
    print('Successfully wrote to file : ' + output_file_name)
    output_file_pointer.close()
    input_file_pointer.close()

print('Execution completed : remove_comments.py')
print('Number of comments removed : \n')
print('Single line comments : ' + str(removed_single_line_comments_count))
print('Multi line comments : ' + str(removed_multi_line_comments_count))