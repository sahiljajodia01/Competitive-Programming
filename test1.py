def get_perm(nums, k):
    if k == 1 :
        for n in nums:
            yield [n]
    else:
        for i,n in enumerate(nums):
        	print("i: ", i)
        	for x in get_perm(nums[i+1:],k-1):
	        	print("Ans: ", [n] + x)
	        	yield [n] + x

def main(nums,k):
    if len(nums) < k:
        return []
    return list(get_perm(nums,k))

a = main([1,2,3,4,5], 3)
print(a)



Define an N-shape array as an array with a strictly increasing subarray followed by a strictly decreasing subarray followed by a strictly increasing subarray. Given an array, return whether or not it's N-shaped.

Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.

[1, 2, 3, 2, 1, 3, 4, 5, 4]


def n_arr(arr):
	if len(arr) < 6:
		return False
	
	prev = arr[0]
	flag1, flag2 = 0, 0
	for i in range(1, len(arr)):
		if flag1 == 0 and flag2 == 0 and arr[i] > prev :
			continue
		elif flag1 == 1 and arr[i] < prev:
			continue
		elif flag2 == 1 and arr[i] > prev:
			continue
		elif flag1 == 1 and arr[i] >= prev:
			flag2 = 1
			flag1 = 0
		elif flag2 == 1 and arr[i] <= prev:
			return False
		else:
			flag1 = 1
		
		prev = arr[i]

	return True





80 Red marbles, 19 Blue marbles, 1 Green

‘red’, ‘blue’ or ‘green’


from random import randint

def get_marble(num_of_marbles):
	random_int = randint(0, num_of_marbles)

	if random_int >= 0 and random_int < 800:
		return ‘red’
	elif random_int >= 800 and random_int < 990:
		return ‘blue’
	else:
		return ‘green’

{
‘red’: 800
‘blue’: 190
‘green’: 10
‘yellow’: 2
}

from random import randint

def get_marble(num_of_marbles):
	total_marbles = 0
	
	for i in num_of_marbles.keys():
		total_marbles += num_of_marbles[i]

	
	random_int = randint(0, total_marbles

	sorted_map = sorted(num_of_marbles.items(), reverse=True, key=lambda k: k[1])
	sum_ = 0
	for key, value in sorted_map:
		sum_ += value
		if sum_ > random_int:
			return key
		



Q2
Remove every alternate node
1 -> 2 -> 3 -> 4 -> 1 : 1 -> 3 -> 1
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 1 : 1 -> 3 -> 5 -> 1