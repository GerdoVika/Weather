
def average(arr: list) -> float:
    return round(sum(arr)/(len(arr)), 1)


def median(arr: list) -> float:
    n = len(arr)
    if n == 1:
        return round(arr[0], 1)
    arr.sort()
    if n % 2:
        median = round(arr[n // 2], 1)
    else:
        median = sum(arr[n//2 - 1 : n//2 + 1])/2
    return round(median, 1)