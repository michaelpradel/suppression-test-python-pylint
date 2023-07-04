# a very useful comment

def fun_above():
    pass

def another_fun(x):
    # pylint: disable=all
    return x + 1

def some_fun(a, b):  # pylint: disable=invalid-name
    return a + b