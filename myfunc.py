def myfunc(arr: list[float]) -> float:
    """
    Computes the largest contiguos sum of subarray

    Args:
        arr (list[int]): A python list containining numbers (array)

    Returns:
        float: The largest contiguos sum of subArray
    """

    cur_sum = arr[0]
    max_sum = arr[0]

    # Impelementing Kadane's Algorithm
    for num in arr[1:]:
        cur_sum = max(num, cur_sum+num)
        max_sum = max(max_sum, cur_sum)

    return max_sum
