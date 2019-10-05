def countMoves(numbers):
    # Write your code here
    num_of_steps = 0
    while len(set(numbers)) != 1:
        num_of_steps += 1
        max_index = numbers.index(max(numbers))

        for i in range(len(numbers)):
            if i != max_index:
                numbers[i] += 1

    return num_of_steps