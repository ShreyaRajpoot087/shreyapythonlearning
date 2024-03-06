
def factorial(number):
    factorial = 1
    for x in range(1,number+1):
        factorial *= x
    return factorial
print(factorial(6))

#using recursion
def fact_recursion(number):
  if number<= 1:
      return 1
  return number*fact_recursion(number-1)
print(fact_recursion(6))


def first(x):
    return x ** x


def second(x):
    return first(x) * first(x)


print(second(2))


def func(x, y):
    return x * x


print(func(2, 5))


def func(a):
    global b
    b = a + a
    return b
b = 10
print(func(13))
print(b)


def func(x):
    if x == 0:
        return 0
    return x + func(x - 1)
print(func(3))


def func(x):
    x += 1
    return x


x = 5
y = func(x + 2)
print(x, y)


def numerical():
    for i in range(10):
        yield i % 2


for x in numerical():
    print(x, end='-')


    def my_fun(x):
        try:
            return x / x
        except:
            print('ex')


    my_fun(1)
    my_fun(0)