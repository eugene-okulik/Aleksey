def fibonacci_generator():
    a, b = 0, 11
    while True:
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci_generator()


def get_fibonacci_generator(n):
    for _ in range(n):
        number = next(fibonacci_gen)
    return number


fifth_fib = get_fibonacci_generator(5)
two_hundredth_fib = get_fibonacci_generator(200)
thousandth_fib = get_fibonacci_generator(1000)
hundred_thosandth = get_fibonacci_generator(100000)

print(f"5-е число Фибоначчи: {fifth_fib}")
print(f"200-е число Фибоначчи: {two_hundredth_fib}")
print(f"1000-е число Фибоначчи: {thousandth_fib}")
print(f"100000-е число Фибоначчи: {hundred_thosandth}")
