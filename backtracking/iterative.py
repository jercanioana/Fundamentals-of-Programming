operands = ["+", "-"]

def consistent(x, n):
    return len(x) < n


def is_solution(x, n):
    s = numbers[0]
    if not len(x) == n - 1:
        return False
    for i in range(n-1):
        if x[i] == 0:
            s += numbers[i+1]
        else:
            s -= numbers[i+1]
    return s > 0


def next_elem(x, n):

    if len(x) == n-1:
        return None
    if x[len(x)-1] == 0:
        return 1
    else:
        return 0

def initial_value():
    return 0

def output_solution(x):
    lst = []
    for i in x:
        lst.append(operands[i])
    print(lst)

def back_iter(n):
    x = [initial_value()]
    while len(x) > 0:
        el = next_elem(x, n)
        while el is not None:
            x[-1] = el
            if consistent(x, n):
                if is_solution(x, n):
                    output_solution(x)
                else:
                    x.append(initial_value())
                    break
            el = next_elem(x, n)
        if el is None:
            if is_solution(x,n):
                output_solution(x)
            x = x[:-1]



n = int(input("Enter a number: "))
numbers = []
for i in range(n):
    numbers.append(int(input(str(i) + ":")))

back_iter(n)