def repeat_me(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
