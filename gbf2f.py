from sys import argv

code = []
for char in open(argv[1], 'r').read():
    code.append(char.strip())

ncode = []

nfile = open(argv[2], 'w')

ncode.append('PROGRAM code\n')
ncode.append('IMPLICIT none\n')
ncode.append('INTEGER, DIMENSION(3000) :: s\n')
ncode.append('INTEGER :: i\n')
ncode.append('i = 1500\n')
for char in code:
    if char == '>':
        ncode.append('i = i + 1\n')
    if char == '<':
        ncode.append('i = i - 1\n')
    if char == '+':
        ncode.append('s(i) = s(i) + 1\n')
    if char == '-':
        ncode.append('s(i) = s(i) - 1\n')
    if char == '.':
        ncode.append('PRINT*, s(i)\n')
    if char == ',':
        ncode.append('READ*, s(i)\n')
    if char == '[':
        ncode.append('DO WHILE (s(i) .ne. 0)\n')
    if char == ']':
        ncode.append('END DO\n')

ncode.append('END PROGRAM code\n')
ncode = ''.join(ncode)

nfile.write(ncode)
nfile.close()

print('=========================')
print('COMPILED {} TO {}'.format(argv[1], argv[2]))
print('=========================')
