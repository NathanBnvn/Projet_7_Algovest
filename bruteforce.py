# coding: utf-8

import csv
import itertools as it


MAX_COST = 500
y = []

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
 		get_benefits(ACTIONS, COST, INTEREST_RATE)


def get_benefits(ACTIONS, COST, INTEREST_RATE):
	estimations = {'actions': [], 'cost': [], 'benefit': []}
	#create_csv_file()

	for n in range(0, len(COST)):
		cost = COST[n]
		action = ACTIONS[n]
		interest = INTEREST_RATE[n]
		benefit = cost * interest / 100
		actions = []

		while cost < MAX_COST:
			for i in range(0, len(COST)):
				if not COST[n] == COST[i]:
					cost = cost + COST[i]
					benefit = COST[i] * INTEREST_RATE[i] / 100 + benefit
					actions.append(action + ': ' + ACTIONS[i])

					if cost < MAX_COST:
						estimations['actions'].append(actions)
						estimations['cost'].append(cost)
						estimations['benefit'].append(benefit)

	get_max_value(estimations)



def get_max_value(estimations):
	max_value = max(estimations['benefit'])
	max_value_index = estimations['benefit'].index(max_value)
	actions = estimations['actions'][max_value_index]
	costs = estimations['cost'][max_value_index]
	print('actions:' + str(actions) + ',  coût:' + str(costs) + ',  bénéfice:' + str(max_value))

def create_csv_file():
	with open('estimates.csv', 'w', encoding='utf-8') as estimation_file:
		estimation_file.write("ACTIONS, COÛT\n")

def save_estimates(estimation):
	with open('estimates.csv', 'a', encoding='utf-8') as estimation_file:
		estimation_file.write(str(estimation['actions']) + str(estimation['cost']) + '\n')

def main():
	read_dataset()


if __name__ == '__main__':
	main()
