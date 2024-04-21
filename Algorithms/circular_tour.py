def tour(petrol, distance):
    start = 0
    curr_petrol = 0
    required_petrol = 0

    for i in range(len(petrol)+1):
        curr_petrol += petrol[i] - distance[i]

        if curr_petrol < 0:
            start = i + 1
            required_petrol += curr_petrol
            curr_petrol = 0

    if start == -1:
        return curr_petrol + required_petrol >= 0
