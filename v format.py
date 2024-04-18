def print_v_format(name):
    n=len(name)
    for i in range(n):
        for j in range(n*2):
            if  j == i or  j == n*2-1-i:
                print(name[i], end=' ')
            else:
                print(' ', end=' ')
        print()

name = input("Enter your name: ")
print_v_format(name)

