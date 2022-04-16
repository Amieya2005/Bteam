import math
import numpy as np

def determinePath(waypoint):
	# COMPLETE HERE

	#PLACEHOLDER, just send out current list2
	order = [0,1,2,3,4]

print(order)
for inx1 in range(0, len(order)):

	small_Num = order[idx1]
	print(small_Num)

	for idx2 in range(idx1+1, len(order)):

		if (order[idx2] < order[idx1]):
			tmp = order[idx1]
			order[idx1] = order[idx2]
			order[idx2] = tmp

order.sort(reversed=False)


print(order)





return order
if __name__ == '__main__':
	main()
