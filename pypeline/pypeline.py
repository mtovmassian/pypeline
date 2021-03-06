from .coroutine import coroutine
from typing import Tuple, List, Generator, Callable


@coroutine
def _pipe_head(target):
    """
        Initial coroutine which starts the pipeline and redirects
        the data to the first process pipe.
    """
    while True:
        data = yield
        target.send(data)


@coroutine
def _pipe_tail(sink):
    """
        Last coroutine which ends up the pipeline and collects data output
        into a sink.
    """
    while True:
        data = yield
        sink(data)


@coroutine
def _pipe(func: Callable, target: Generator):
    """
        Coroutine used to handle data processing.
    """
    while True:
        data = yield
        data_transformed = func(data)
        target.send(data_transformed)


def _init_sink() -> Callable:
    """
        Closure used to provide a sink for pipeline output storage.
    """
    collection = []

    def sink(data=None) -> List[any]:
        nonlocal collection
        if data:
            collection.append(data)
        return collection
    return sink


def create(funcs: List) -> Tuple[Generator, List]:
    """
        Initialize pipeline.
    """
    sink = _init_sink()
    call_chain = None
    funcs = reversed(funcs)
    for index, func in enumerate(funcs):
        if index == 0:
            call_chain = _pipe(func, _pipe_tail(sink))
        else:
            call_chain = _pipe(func, call_chain)
    pipeline = _pipe_head(call_chain)
    return pipeline, sink
