from sys import argv

print(argv)
print(type(argv))

for posicao_arg, arg in enumerate(argv):
    print(posicao_arg)
    print(arg)
    print(type(arg))
