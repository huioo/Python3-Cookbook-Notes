from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args
        
        
def apply_async(func, args, *, callback):
    # compute the result
    result = func(*args)
    
    # Invoke the callback with the result
    callback(result)


def inline_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        print('Before `while` statement', f)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
            else:
                print('During `while` statement', f)
                print(' '*5, 'result:', result, ',', 'result_queue:', result_queue, ',', 'result_queue.queue:', result_queue.queue)
                print(' '*5, 'a:', a, ',', 'a.func:', a.func, ',', 'a.args:', a.args)
                
    return wrapper


def add(x, y):
    return x + y


@inline_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    
    r = yield Async(add, ('hello', 'world'))
    print(r)

    # for i in range(10):
    #     r = yield Async(add, (i, i))
    #     print(r)

    return 'Goodbye'


if __name__ == '__main__':
    test()


