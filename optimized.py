import csv

MAX_CAPACITY = 500

###################################### version 3

def read_dataset():
    raw_interests = []
    raw_costs = []
    ACTIONS = []
    estimations = {'actions': [], 'cost': [], 'benefit': []}

    select_dataset = input('Enter the dataset file name : ')

    with open(select_dataset + '.csv', 'r', encoding='utf-8') as csv_dataset:
        csv_reader = csv.reader(csv_dataset)
        for row in csv_reader:
            ACTIONS.append(row[0])
            raw_costs.append(row[1])
            raw_interests.append(row[2])

        ACTIONS.pop(0)
        raw_costs.pop(0)
        raw_interests.pop(0)

        COST = []

        for cost in raw_costs:
            try :
                y = int(cost)
                COST.append(y)
            except ValueError:
                x = float(cost) * 100
                w = int(x)
                #print(w)
                COST.append(w)


        INTEREST_RATE = []

        for interest in raw_interests:
            try :
                y = int(interest)
                INTEREST_RATE.append(y)
            except ValueError:
                x = float(interest) * 100
                w = int(x)
                #print(w)
                INTEREST_RATE.append(w)


        BENEFIT = []

        for i in range(len(COST)):
            benefit = COST[i] * INTEREST_RATE[i] / 100
            BENEFIT.append(int(benefit))

        BENEFIT_NUMBER = len(BENEFIT)

        for x in range(BENEFIT_NUMBER):
            estimations['actions'].append(ACTIONS[x])
            estimations['cost'].append(COST[x])
            estimations['benefit'].append(BENEFIT[x])

        #print(len(estimations['benefit']))
        #print(len(estimations['actions']))
        print(stockPortfolio(MAX_CAPACITY, estimations, BENEFIT_NUMBER))

def stockPortfolio(capacity, estimations, benefit_number):

    matrix = [[0 for x in range(capacity + 1)] for x in range(len(estimations['cost']) + 1)]

    for i in range(1, len(estimations['actions']) + 1):
        for w in range(1, capacity + 1):
            if estimations['cost'][i-1] <= w:
                matrix[i][w] = max(estimations['benefit'][i-1] + matrix[i-1][w-estimations['cost'][i-1]], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]

    selected_elements = []
    benefit_number = len(estimations['actions'])

    while benefit_number > 0:
        e = estimations['actions'][benefit_number-1]
        if matrix[benefit_number][w] == matrix[benefit_number-1][w-estimations['cost'][benefit_number-1]] + estimations['benefit'][benefit_number-1]:
            selected_elements.append(e)
            w -= estimations['cost'][benefit_number-1]

        benefit_number -= 1

    return matrix[-1][-1], selected_elements

def main():
    read_dataset()

if __name__ == '__main__':
    main()
