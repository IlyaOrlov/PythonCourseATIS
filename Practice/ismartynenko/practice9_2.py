from multiprocessing import Pool


def func(*args):
    res = None
    if type(args[0][0]) == int:
        res = 0
    elif type(args[0][0]) == str:
        res = ''
    elif type(args[0][0]) == list:
        res = []
    else:
        print("Incorrect input. Exit")
        exit()

    for i in args[0]:
        res += i
    return res


if __name__ == "__main__":
    with Pool(processes=3) as pool:
        result = pool.map(func, [(1, 2, 3, 4, 5), ("1", "2", "3", "4", "5"), (["1", "2", "3"], ["4", "5"])])
        print(result)
