def attemp(
        n=5
        ):
    def decorator(
            func
    ):
        def wraps(
                *args,
                **kwargs
                ):
            print('-------')
            print(n)
            func(*args, **kwargs)
            print('-------')
            return

        return wraps
    return decorator


@attemp(n=5)
def my_print(
        name
        ):
    print(f'ejhfjkefr, {name}')


my_print(name='Ivan')
