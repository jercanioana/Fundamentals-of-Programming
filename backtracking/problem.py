
operands = ["+", "-"]

def first(x):
    return operands[0]


def consistent(x, n):
    return len(x) < n


def is_solution(x, n):
    s = numbers[0]
    if not len(x) == n - 1:
        return False
    for i in range(n-1):
        if x[i] == "+":
            s += numbers[i+1]
        else:
            s -= numbers[i+1]
    return s > 0


def output_solution(x):
    print(x)

def next_elem(x, n):

    if len(x) == n-1:
        return None
    if x[len(x)-1] == "+":
        return "-"
    else:
        return "+"

def back_rec(x,n):
    el = first(x)
    for el in operands:
        x.append(el)
        if consistent(x,n):
            if is_solution(x,n):
                output_solution(x)
            else:
                back_rec(x,n)
        x.pop()



n = int(input("Enter a number: "))
numbers = []
for i in range(n):
    numbers.append(int(input(str(i) + ":")))


back_rec([], n)
