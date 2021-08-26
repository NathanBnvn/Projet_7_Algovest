import csv

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
        #INTEREST_NUMBER = len(INTEREST_RATE)
        
        BENEFIT = []

        for i in range(20):
            benefit = COST[i] * INTEREST_RATE[i] / 100
            BENEFIT.append(benefit)

        BENEFIT_NUMBER = len(BENEFIT)
        print(knapSack(MAX_CAPACITY, COST, BENEFIT, BENEFIT_NUMBER))

def knapSack(max_capacity, costs, interests, interest_number):
    # Base Case
    if interest_number == 0 or max_capacity == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (costs[interest_number-1] > max_capacity):
        return knapSack(max_capacity, costs, interests, interest_number-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            interests[interest_number - 1] + knapSack(
                max_capacity-costs[interest_number-1], costs, interests, interest_number-1),
            knapSack(max_capacity, costs, interests, interest_number-1))


def main():
    read_dataset()

if __name__ == '__main__':
    main()
