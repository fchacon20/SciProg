def from2to3(line, cell):   
    ip = get_ipython()
    filename = '_temp.py'
    
    lineByLine = cell.split('\n')
    with open(filename, 'w') as f:
        for line in lineByLine:
            if 'print' in line:
                line = line.replace("print ","print(")
                line += ")"
            if 'raw' in line:
                line = line.replace("raw_","")
            line += "\n"
            f.write(line)
    output = ip.getoutput('ipython ' + filename)
    print('\n'.join(output))

def load_ipython_extension(ipython):
       ipython.register_magic_function(from2to3, 'cell')