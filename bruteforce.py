# coding: utf-8

import csv

MAX_COST = 500

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

 		element = []
 		COST = [int(cost) for cost in raw_costs]
 		INTEREST_RATE = [int(interest) for interest in raw_interests]
 		for x in range(len(COST)):
 			benefit = COST[x] * INTEREST_RATE[x] / 100
 			element.append((ACTIONS[x], COST[x], benefit))

 		print(knapsack(MAX_COST, element))
 		#get_benefits(ACTIONS, COST, INTEREST_RATE)

#def get_benefits(ACTIONS, COST, INTEREST_RATE):

	for n in range(0, len(COST)):
		cost = COST[n]
		action = ACTIONS[n]
		interest = INTEREST_RATE[n]
		benefit = cost * interest / 100
		actions = []

		while cost < MAX_COST:
			current_action = action + ':'
			actions.insert(0, current_action)

			for i in range(0, len(COST)):
				if not COST[n] == COST[i]:
					cost = cost + COST[i]
					benefit = COST[i] * INTEREST_RATE[i] / 100 + benefit
					actions.append(ACTIONS[i])

					#if cost <= MAX_COST:
					estimations['actions'].append(actions.copy())
					estimations['cost'].append(cost)
					estimations['benefit'].append(benefit)

					print(estimations)

	#get_max_value(estimations)

#def get_max_value(estimations):
	max_value = max(estimations['benefit'])
	max_value_index = estimations['benefit'].index(max_value)
	actions = estimations['actions'][max_value_index]
	costs = estimations['cost'][max_value_index]
	print('actions:' + str(actions) + ',  coût:' + str(costs) + ',  bénéfice:' + str(max_value))

# def create_csv_file():
# 	with open('estimates.csv', 'w', encoding='utf-8') as estimation_file:
# 		estimation_file.write("ACTIONS, COÛT\n")

# def save_estimates(estimation):
# 	with open('estimates.csv', 'a', encoding='utf-8') as estimation_file:
# 		estimation_file.write(str(estimation['actions']) + str(estimation['cost']) + '\n')



def knapsack(capacity, element, selected_actions = []):
	if element:
		action1, actionList1 = knapsack(capacity, element[1:], selected_actions)
		action = element[0]
		if action[1] <= capacity:
			action2, actionList2 = knapsack(capacity - action[1], element[1:], selected_actions + [action])
			if action1 < action2:
				return action2, actionList2

		return action1, actionList1
	else:
		return sum([i[2] for i in selected_actions]), selected_actions

def main():
	read_dataset()

if __name__ == '__main__':
	main()
