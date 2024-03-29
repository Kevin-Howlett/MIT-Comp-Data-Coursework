#Program defines functions that help determine how to transport cows of
#varying weights, given a weight limit for each shipment.
#A greedy algorithm and a brute force algorithm were written.



# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for the brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]



#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    transportList = []
    sortedCows = []
    import operator
    sortedTuple = sorted(cows.items(), key=operator.itemgetter(1), reverse=True)
    for i in sortedTuple:
        sortedCows.append(i[0])

    while sortedCows != []:
        shipment = []
        limit1 = limit
        sortedCopy = sortedCows[:]
        for i in sortedCopy:
            if limit1 - cows[i] >= 0:
                limit1 -= cows[i]
                shipment.append(i)
                sortedCows.remove(i)
        transportList.append(shipment)
    return transportList


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    transport_list = []
    cows_list = []
    for i in cows:
        cows_list.append(i)
    for item in get_partitions(cows_list):
        count = 0
        for sub_list in item:
            weight = 0
            for cow in sub_list:
                weight += cows[cow]
            if weight > limit:
                count += 1
        if count == 0:
            transport_list.append(item)
    return transport_list
        



cows = load_cows("ps1_cow_data.txt")
limit=100

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


