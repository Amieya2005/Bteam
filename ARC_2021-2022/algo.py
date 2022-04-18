import math
import numpy as np


def determinePath(waypoint):
	# COMPLETE HERE
	#42.27690 N -83.73063 E 10 H
	#42.33905 N -83.06404 E 10 A
	#42.63678 N -83.29613 E 10 C
	#42.29201 N -83.71624 E 10 B
	#42.29198 N -83.71561 E 10 A'

    waypointH = np.array((42.27690, -83.73063, 10))
    waypointA = np.array((42.33905, -83.06404, 10))
    waypointC = np.array((42.63678, -83.29613, 10))
    waypointB = np.array((42.29201, -83.71624, 10))
    waypointA2 = np.array((42.29198, -83.71561, 10))

    distanceHtoA = np.linalg.norm(waypointH-waypointA)
    distanceHtoC = np.linalg.norm(waypointH-waypointC)
    distanceHtoB = np.linalg.norm(waypointH-waypointB)
    distanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [distanceHtoA, distanceHtoC, distanceHtoB, distanceHtoA2]
    minimumDistance = min(Distances)
    closestWaypoint = Distances.index(minimumDistance)
    #Path = Path.append(closestWaypoint)

    print("distanceHtoA: ", distanceHtoA)
    print("distanceHtoC: ", distanceHtoC)
    print("distanceHtoB: ", distanceHtoB)
    print("distanceHtoA2: ", distanceHtoA2)
    print(minimumDistance)


#PLACEHOLDER, just send out current list2
order = [0, 1, 2, 3, 4]

#print(order)
#for inx1 in range(0, len(order)):

#	small_Num = order[idx1]
#	print(small_Num)

#	for idx2 in range(idx1+1, len(order)):

#		if (order[idx2] < order[idx1]):
#			tmp = order[idx1]
#			order[idx1] = order[idx2]
#			order[idx2] = tmp

#order.sort(reversed=False)


#print(order)


#return order
#if __name__ == '__main__':
#	main()
