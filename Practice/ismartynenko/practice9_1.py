import time
import threading
import multiprocessing
from math import sqrt


'''В случае с потоками и процессами без метода start функция не начнет выполняться
С методом join() обстоит иначе, в потоках начинается некорректная работа, то два из 3-ех отработает, то один.
Процессы же не замечают если забыть указать join.

One thread: 1.3745658
=========================
join() Threads: 1.5786332
w/o join() Threads: 0.111361
=========================
join() Processes: 0.8879530999999999
w/o join() Processes: 0.06469780000000001

Полагаю что процессы/потоки медленнее с join() потому что уходит время на их завершение.'''


def find_primes(end, start=3):
    simple_nums = []
    while start <= end:
        i = 2
        j = 0
        n = sqrt(start)
        while i <= n:
            if start % i == 0:
                j = 1
                break
            else:
                i += 1
        if j != 1:
            simple_nums.append(start)
        start += 1
    print(simple_nums)


if __name__ == '__main__':
    print("One thread:", end=' ')
    t_start = time.perf_counter()
    find_primes(100000)
    find_primes(200000, 100001)
    find_primes(300000, 200001)
    print(time.perf_counter() - t_start)

    args = ((100000,), (200000, 100001), (300000, 200001))

    print("Threads:", end=' ')
    t_start = time.perf_counter()
    threads = []
    for k in args:
        thr = threading.Thread(target=find_primes, args=k)
        thr.start()
        threads.append(thr)
    for thr in threads:
        thr.join()
    print(time.perf_counter() - t_start)

    print("Processes:", end=' ')
    t_start = time.perf_counter()
    processes = []
    for k in args:
        mp = multiprocessing.Process(target=find_primes, args=k)
        mp.start()
        processes.append(mp)
    for mp in processes:
        mp.join()
    print(time.perf_counter() - t_start)
