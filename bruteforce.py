# coding: utf-8

import csv

ACTIONS = [
"Action-1",
"Action-2",
"Action-3",
"Action-4",
"Action-5",
"Action-6",
"Action-7",
"Action-8",
"Action-9",
"Action-10",
"Action-11",
"Action-12",
"Action-13",
"Action-14",
"Action-15",
"Action-16",
"Action-17",
"Action-18",
"Action-19",
"Action-20",
]

COST = [
	20,
	30,
	50,
	70,
	60,
	80,
	22,
	26,
	48,
	34,
	42,
	110,
	38,
	14,
	18,
	8,
	4,
	10,
	24,
	114,
]


INTEREST_RATE = [
	5,
	10,
	15,
	20,
	17,
	25,
	7,
	11,
	13,
	27,
	17,
	9,
	23,
	1,
	3,
	8,
	12,
	14,
	21,
	18,
]

MAX_COST = 500

# Algo forcebrute - pseudo code
# 
#
# Tant que le cout est inférieur
#
#

def get_benefits():
	#benefits = [COST[i] * INTEREST_RATE[i] / 100 for i in range(20)]

	# with open('dataset.numbers', 'r', encoding='latin-1') as csv_dataset:
	# 	csv_reader = csv.reader(csv_dataset)
	# 	fields = next(csv_reader)

############################################
	a = {}

	for n in range(0, len(COST)):
		cost = COST[n]
		action = ACTIONS[n]
		interest = INTEREST_RATE[n]
		print(action)
		while cost < MAX_COST:
			for i in range(0, len(COST)):
				if not COST[n] == COST[i]:
					cost = cost + COST[i]
					action_1 = action + ', ' + ACTIONS[i]
					interest = interest + INTEREST_RATE[i]
					benefit = cost * interest / 100
					if cost < MAX_COST:
						#a[cost] = interest
						print(benefit)

#############################################


# Tant que le cout est inférieur à 500
# acheter une action

	# cost = COST[0]
	# i = 1
	# while cost < 99:
	# 	cost = cost + COST[i]
	# 	i += 1
	# 	print(cost)

def main():
	benef = get_benefits()
	#print(benef)

if __name__ == '__main__':
	main()

