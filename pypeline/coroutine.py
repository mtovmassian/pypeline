def coroutine(func):
    """
        Decorator used to give a coroutine behavior to a generator
        by initalizing it before data sending.
    """
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper
