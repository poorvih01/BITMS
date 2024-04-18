def print_x_format(name):
    for i in range(len(name)):
        for j in range(len(name)):
            if i == j or i + j == len(name) - 1:
                print(name[i], end=' ')
            else:
                print(' ', end=' ')
        print()

name = input("Enter your name: ")
print_x_format(name)
