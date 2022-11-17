import mod1

def greeter(x):
    for i in x:
        print("Hello " + i)

if __name__ == '__main__':
    greeter(mod1.my_list)