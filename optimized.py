import csv

MAX_CAPACITY = 500

###################################### version 3

def read_dataset():
    raw_interests = []
    raw_costs = []
    ACTIONS = []
    estimations = {'actions': [], 'cost': [], 'benefit': []}

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
        BENEFIT = []

        for i in range(20):
            benefit = COST[i] * INTEREST_RATE[i] / 100
            BENEFIT.append(benefit)

        BENEFIT_NUMBER = len(BENEFIT)
        for x in range(BENEFIT_NUMBER):
            estimations['actions'].append(ACTIONS[x])
            estimations['cost'].append(COST[x])
            estimations['benefit'].append(BENEFIT[x])

        print(knapSack(MAX_CAPACITY, estimations, BENEFIT_NUMBER))

def knapSack(capacity, estimations, o):

    matrix = [[0 for x in range(capacity + 1)] for x in range(len(estimations['actions']) + 1)]

    for i in range(1, len(estimations['actions']) + 1):
        for w in range(1, capacity + 1):
            if estimations['cost'][i-1] <= w:
                matrix[i][w] = max(estimations['benefit'][i-1] + matrix[i-1][w-estimations['cost'][i-1]], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]

    selected_elements = []
    o = len(estimations['actions'])

    while o > 0:
        e = estimations['actions'][o-1]
        print(e)
        if matrix[o][w] == matrix[o-1][w-estimations['cost'][o-1]] + estimations['benefit'][o-1]:
            selected_elements.append(e)
            w -= estimations['cost'][o-1]

        o -= 1

    return matrix[-1][-1], selected_elements

def main():
    read_dataset()

if __name__ == '__main__':
    main()
