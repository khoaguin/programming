# Input: The first line contains an integer d (the distance between 2 cities). 
#        The second line contains an integer m (the maximum miles a car can travel on a full tank). 
#        The third line specifies an integer n (the number of gas stops between 2 cities). 
#        Finally, the last line contains integers stop_1, stop_2, ..., stop_n (distances along the way).
# Output: The minimum number of refills needed. 
#         We assume that the car starts with a full tank. 
#         If it is not possible to reach the destination, output −1.


# Iterative solution
def compute_min_refills(distance, tank, stops):
    num_refills, current_stop, limit = 0, 0, tank
    n = len(stops)
    while limit < distance:
        # check cases when we cannot reach the destination
        if current_stop >= n or stops[current_stop] > limit:
            return -1
        # find the furthest reachable station
        while current_stop < n - 1 and stops[current_stop+1] <= limit:
            current_stop += 1
        
        limit = stops[current_stop] + tank
        current_stop += 1
        num_refills += 1

    return num_refills


if __name__ == '__main__':
    d = int(input())  # distance between 2 cities
    m = int(input())  # the maximum distance the car can travel with a full tank
    n = int(input())  # the number of stops
    stops = list(map(int, input().split()))
    # print()
    print(compute_min_refills(d, m, stops))