def write_variables(name_table, value_table, output_file):

    convert_datatypes = {'byte' : 'db', 'word' : 'dw'}
    output_file.write('.model small\n\n.data\n')
    for identifier in name_table:
        datatype = convert_datatypes[name_table[identifier]]
        value = value_table[identifier]
        output_file.write(identifier + ' ' + datatype + ' ' + value + '\n')
    output_file.write('in dw ?\nout dw ?\n\n.code\n')

def assignment(line):
    str = ''
    if '++' in line:
        x = line.strip('++').strip(';')
        return 'inc ' + x + '\n'
    if '--' in line:
        x = line.strip('--').strip(';')
        return 'dec ' + x + '\n'

    line_split = line.split('=')
    if len(line_split) < 2:
        return ''
    left = line_split[0]
    rights = line_split[1]
    op_split = rights.split('+')
    if len(op_split) == 2:
        x, y = op_split[0], op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'add ax, bx\n'
        str += 'mov ' + left + ', ax\n'
        return str

    op_split = rights.split('-')
    if len(op_split) == 2:
        x, y = op_split[0], op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'sub ax, bx\n'
        str += 'mov ' + left + ', ax\n'
        return str

    op_split = rights.split('*')
    if len(op_split) == 2:
        x, y = op_split[0], op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov dx, 00h\n'
        str += 'mov bx, ' + y + '\n'
        str += 'mul bx\n'
        str += 'mov ' + left + ', ax\n'
        return str

    op_split = rights.split('/')
    if len(op_split) == 2:
        x, y = op_split[0], op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'div bx\n'
        str += 'mov ' + left + ', ax\n'
        return str

    op_split = rights.split('%')
    if len(op_split) == 2:
        x, y = op_split[0], op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'div bx\n'
        str += 'mov ' + left + ', dx\n'
        return str

    str += 'mov ax, ' + rights + '\n'
    str += 'mov ' + left + ', ax\n'
    return str

def get_condition(line, jump):
    str = ''
    op_split = line.split('==')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'jne ' + jump + '\n'
        return str
    op_split = line.split('!=')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'je ' + jump + '\n'
        return str
    op_split = line.split('>')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'jle ' + jump + '\n'
        return str
    op_split = line.split('>=')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'jl ' + jump + '\n'
        return str
    op_split = line.split('<')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'jge ' + jump + '\n'
        return str
    op_split = line.split('<=')
    if len(op_split) == 2:
        x = op_split[0]
        y = op_split[1]
        str += 'mov ax, ' + x + '\n'
        str += 'mov bx, ' + y + '\n'
        str += 'cmp ax, bx\n'
        str += 'jg ' + jump + '\n'
        return str

functions = {
    'input()' : 'mov ah, 01h\nint 21h\nmov in, al\n',
    'output()': 'mov dl, out\nmov ah, 02h\nint 21h\n'
}