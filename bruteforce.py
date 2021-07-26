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


# def read_dataset():
# 	with open('dataset.numbers', 'r', encoding='latin-1') as csv_dataset:
# 		csv_reader = csv.reader(csv_dataset)
# 		for row in csv_reader:
# 			print(row[1])


def get_benefits():
	create_csv_file()

	for n in range(0, len(COST)):
		cost = COST[n]
		action = ACTIONS[n]
		interest = INTEREST_RATE[n]

		while cost < MAX_COST:
			for i in range(0, len(COST)):
				if not COST[n] == COST[i]:
					cost = cost + COST[i]
					action_set = action + ' à ' + ACTIONS[i]
					interest = interest + INTEREST_RATE[i]
					benefit = cost * interest / 100
					if cost < MAX_COST:
						estimation = {'actions': action_set, 'cost':cost, 'benefit': benefit}
						save_estimates(estimation)
	return

def create_csv_file():
	with open('estimates.csv', 'w', encoding='utf-8') as estimation_file:
		estimation_file.write("ACTIONS, COÛT, BENEFICE\n")


def save_estimates(estimation):
	with open('estimates.csv', 'a', encoding='utf-8') as estimation_file:
		estimation_file.write(estimation['actions'] + ', ' + str(estimation['cost']) + ', ' + str(estimation['benefit']) + '\n')


def main():
	#read_dataset()
	get_benefits()



if __name__ == '__main__':
	main()
