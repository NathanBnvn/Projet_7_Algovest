costs = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
interests = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
max_capacity = 500


############################## version 1

class StockPortfolio:

	def __init__(self, costs, interests, max_capacity):
		self.max_capacity = max_capacity
		self.costs = costs
		self.interests = interests
		self.rapport = interests // costs

	def __lt__(self, other):
		return self.rapport < other.rapport


def getMaxInterest(costs, interests, max_capacity):
	sorted_array = []
	for i in range(len(costs)):
		sorted_array.append(StockPortfolio(costs[i], interests[i], i))
	#sorted_array.sort(reverse = True)

	interests_counter = 0

	for e in sorted_array:
		current_costs = int(e.costs)
		current_interests = int(e.interests)
		
		if max_capacity - current_costs >= 0:
			max_capacity -= current_costs
			interests_counter += current_interests
	return interests_counter


#max_interest = getMaxInterest(costs, interests, max_capacity)
#print('Valeur maxi du sac à dos est' + str(max_interest))

#################################### version 2

# Define a default knapsack 01 function
def knapsack01(max_capacity, costs, interests, interests_number):
	M = [ [0 for a in range (max_capacity + 1)] for a in range (interests_number + 1)]
	# Define a for loop for limit
	for b in range (interests_number + 1):
	# Nested for loop for higher limit
		for c in range (max_capacity + 1):
	# Defining if condition for maximum weight
			if b == 0 or c == 0:
				M[b][c] = 0
    # Elseif condition for maximum value in bag
			elif costs[b-1] <= c:
				M[b][c] = max (interests[b-1] + M[b-1][c-costs[b-1]], M[b-1][c])
			else:
				M[b][c] = M[b-1][c]
	return M[interests_number][max_capacity] # returning maximum value from the function

interests_number = len(interests)
# Taking maximum limit as user input

# Printing result of problem in the output
#print ("The maximum value of items we can get with the given limit: ")
#print (knapsack01(max_capacity, costs, interests, interests_number))

###################################### version 3

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



print(knapSack(max_capacity, costs, interests, interests_number))

