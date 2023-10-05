import dis

# Load the compiled module (hidden_4.pyc)
with open('hidden_4.pyc', 'rb') as f:
    code = f.read()

# Disassemble the bytecode to extract object names
names = []
code = dis.Bytecode(code)
for instruction in code:
    if instruction.opname == 'LOAD_GLOBAL':
        name = instruction.argval
        if not name.startswith('__'):
            names.append(name)

# Sort and print the names
names.sort()
for name in names:
    print(name)
