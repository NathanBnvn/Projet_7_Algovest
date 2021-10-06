# coding: utf-8

import csv

MAX_CAPACITY = 500

def read_dataset(MAX_CAPACITY):
    raw_interests = []
    raw_costs = []
    ACTIONS = []
    estimations = {'actions': [], 'cost': [], 'benefit': []}

    with open('dataset2_Python+P7.csv', 'r') as csv_dataset:
        csv_reader = csv.reader(csv_dataset)
        for row in csv_reader:
            ACTIONS.append(row[0])
            raw_costs.append(row[1])
            raw_interests.append(row[2])

        ACTIONS.pop(0)
        raw_costs.pop(0)
        raw_interests.pop(0)

        for x in range(len(ACTIONS)):
            estimations['actions'].append(ACTIONS[x])
            estimations['cost'].append((int(float(raw_costs[x]) * 100)))
            estimations['benefit'].append(int(float(raw_costs[x]) * 100) * int(float(raw_interests[x]) * 100) / 1000000)

        BENEFIT_LEN = len(estimations['benefit'])
        capacity = MAX_CAPACITY * 100

        print(stockPortfolio(capacity, estimations, BENEFIT_LEN))

def stockPortfolio(capacity, estimations, benefit_len):

    # création d'une matrice
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(benefit_len + 1)]

    # incrémente de 1 jusqu'au nombre d'actions
    # puis incrémente de 1 jusqu'à la charge maximale du sac
    for i in range(1, benefit_len + 1):
        for w in range(1, capacity + 1):
            if estimations['cost'][i-1] <= w:
                estimate_cost = w-estimations['cost'][i-1]
                if estimate_cost < capacity:
                    matrix[i][w] = max(estimations['benefit'][i-1] + matrix[i-1][estimate_cost], matrix[i-1][w])
                else:
                    matrix[i][w] = matrix[i-1][w]
            else:
                matrix[i][w] = matrix[i-1][w]


    selected_actions = {'action': [], 'cost': [], 'benefit': []}

    while benefit_len >= 0:
        price = 0

        action = estimations['actions'][benefit_len-1]
        cost = estimations['cost'][benefit_len-1]
        benefit = estimations['benefit'][benefit_len-1]
        estimate_cost = w-estimations['cost'][benefit_len-1]

        if estimate_cost <= capacity and estimate_cost > 0:
            if matrix[benefit_len][w] == matrix[benefit_len-1][estimate_cost] + estimations['benefit'][benefit_len-1]:
                if cost >= 0 and benefit > 0:
                    selected_actions['action'].append(action)
                    selected_actions['cost'].append(int(cost / 100))
                    selected_actions['benefit'].append(benefit)
                    total_price = sum(selected_actions['cost'])

                    w -= estimations['cost'][benefit_len-1]

        benefit_len -= 1

    for x in range(len(selected_actions['action'])):
        print(selected_actions['action'][x] + ', cost :' + str(selected_actions['cost'][x]) + '€')
 
    print('total cost: ' + str(total_price) + '€')
    print(sum(selected_actions['benefit']))
    total_benefit = 'total benefit: ' + str(matrix[-1][-1]) + '€'

    return total_benefit


if __name__ == '__main__':
    read_dataset(MAX_CAPACITY)
