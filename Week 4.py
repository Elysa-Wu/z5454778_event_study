#Exercise 2.2 (Tzu-Yi, Wu (Elysa))
# Question: num are divisible by 2
num = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]

solution = [i for i in set(num) if i % 2 == 0]

solution.sort()
print(solution)

#Functions Definitions
# def func_name ( <parameter expression> ) :
#       <function body>
def qan_tic():
    tic="QAN.AX"
    print(tic)
    return tic
qan_tic()

# Define a function called `qan_tic`
def qan_tic(): # (1)
    tic = "QAN.AX" # (2)
    print(tic) # (3)
    return tic # (4)
# Call the function
res = qan_tic() # (5b)
print(res)

#Global and local variable
def qan_tic():
    tic1 = "QAN.AX" # <-- local
    print(tic)
    return tic
tic2 = "WES.AX" # <-- global

#Parameters
def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    return f'{tic_base}_stk_prc.csv'
name = mk_csv_name('QAN.AX')
print(name)

#Default parameters
def mk_csv_name(tic, show=True):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    name = f'{tic_base}_stk_prc.csv'
    if show is True:
        print(name)
    return name

name = mk_csv_name('QAN.AX')


def add(a, b):
    """ Returns the sum of two numbers """
    return a + b
help(add)






