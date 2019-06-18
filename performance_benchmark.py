import time

BIG = 20000000

def f(k):
    return 2*k

def list_a():
    list_a = []
    for i in range(BIG):
        list_a.append(f(i))

def list_b():
    list_b = [f(i) for i in range(BIG)]

def list_a_filtered():
    list_a = []
    for i in range(BIG):
        if i%2==0:
            list_a.append(f(i))

def list_b_filtered():
    list_b = [f(i) for i in range(BIG) if i%2==0]

def benchmark(function, function_name):
    start = time.time()
    function()
    end = time.time()
    print("{0} seconds for {1}".format((end - start), function_name))

benchmark(list_a, "list a")
benchmark(list_b, "list b")
benchmark(list_a_filtered, "filtered list a")
benchmark(list_b_filtered, "filtered list b")
