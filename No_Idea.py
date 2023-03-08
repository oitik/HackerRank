if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    setA = set([int(x) for x in input().split()])
    setB = set([int(x) for x in input().split()])
    # Here you must use set because it is operation in set is faster than list.
    count = 0
    for val in arr:
        if val in setA:
            count += 1
        elif val in setB:
            count -= 1
    print(count)
