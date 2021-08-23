import csv

#costs = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
#interests = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
MAX_CAPACITY = 500

###################################### version 3

def read_dataset():
    raw_interests = []
    raw_costs = []
    ACTIONS = [] 

    with open('dataset.csv', 'r', encoding='utf-8') as csv_dataset:
        csv_reader = csv.reader(csv_dataset)
        for row in csv_reader:
            ACTIONS.append(row[0])
            raw_costs.append(row[1])
            raw_interests.append(row[2])

        ACTIONS.pop(0)
        raw_costs.pop(0)
        raw_interests.pop(0)

        COST = [int(cost) for cost in raw_costs]
        INTEREST_RATE = [int(interest) for interest in raw_interests]
        INTEREST_NUMBER = len(INTEREST_RATE)
        knapSack(MAX_CAPACITY, COST, INTEREST_RATE, INTEREST_NUMBER)

def knapSack(max_capacity, costs, interests, interests_number):
 
    # Base Case
    if interests_number == 0 or max_capacity == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (costs[interests_number-1] > max_capacity):
        return knapSack(max_capacity, costs, interests, interests_number-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            interests[interests_number-1] + knapSack(
                max_capacity-costs[interests_number-1], costs, interests, interests_number-1),
            knapSack(max_capacity, costs, interests, interests_number-1))



def main():
    read_dataset()

if __name__ == '__main__':
    main()
