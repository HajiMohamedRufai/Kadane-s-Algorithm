# Kadane's Algorithm
Lets take a time to appreciate Kadane's Algorithm.
It is used to solve largest contiguos sum of an array, which may be a subarray or the entire array.

We know if an array consists of all positive integers and zeros, the largest contiguos sum is the sum of the entire array elements

Example:
arr1 = [2, 9, 7, 1]
The largest contiguos sum of the array is the sum of the entire array elements
2 + 9 + 7 + 1 = 19

What if given an array that consists of negative numbers?
Eg [0, 1, -3, 2, 5, -2, 0, 0,1, -9]
If you try and err and note the above the largest contiguos sum is given by this contiguos subarray [2, 5, -2, 0, 0, 1 ], 
sum(subArray) = 2 + 5 + -2 + 0 + 0 + 1 = 6

Ok, lets try to get our brains and hands dirty:
Lets write the algorithm code(any langugae of your choice but python is much simpler) to give us the largest contiguos sum subarray of an array

Take 5-25 minutes: 
I guess you are trying to come with all possible which may deteriote both  time and space complexity or you are still lazy yet, 

But still no problem (haha, if the latter). Kadane Algorithm with the next 3 lines of code solve this problem which by the way has many applications which is another discussion of another day.

  cur_sum = arr[0]
    max_sum = arr[0]

    # Impelementing Kadane's Algorithm
    for num in arr[1:]:
        cur_sum = max(num, cur_sum+num)
        max_sum = max(max_sum, cur_sum)


© Haji Rufai

