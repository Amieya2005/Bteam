import math
import numpy as np
waypoint = []


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
    destinations = (["waypointH = np.array((42.27690, -83.73063, 10))", "waypointA = np.array((42.33905, -83.06404, 10))",
                     "waypointC = np.array((42.63678, -83.29613, 10))", "waypointB = np.array((42.29201, -83.71624, 10))", "waypointA2 = np.array((42.29198, -83.71561, 10))])"])

    H = "waypointH"
    A = "waypointA"
    C = "waypointC"
    B = "waypointB"
    A2 = "waypointA2"
#-----------------------------------------------------------------------------
    #FIRST POINT
    distanceHtoA = np.linalg.norm(waypointH-waypointA)
    distanceHtoC = np.linalg.norm(waypointH-waypointC)
    distanceHtoB = np.linalg.norm(waypointH-waypointB)
    distanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [distanceHtoA, distanceHtoC, distanceHtoB, distanceHtoA2]
    UminimumDistance = min(Distances)
    P1 = "distanceHtoB: ", UminimumDistance
    print("distanceHtoA: ", distanceHtoA)
    print("distanceHtoC: ", distanceHtoC)
    print("distanceHtoB: ", distanceHtoB)
    print("distanceHtoA2: ", distanceHtoA2)
    print("HtoB", UminimumDistance)

    W1 = B

    #U=latin for 1
    #Arranged = np.array([[distanceHtoA, distanceHtoC,distanceHtoB, distanceHtoA2]])
    #print(np.sort(Arranged))
    #------------------------------------------------------------------------
    #SECOND POINT
    distanceBtoA = np.linalg.norm(waypointB-waypointA)
    distanceBtoC = np.linalg.norm(waypointB-waypointC)
    distanceBtoA2 = np.linalg.norm(waypointB-waypointA2)
    Distances2 = [distanceBtoA, distanceBtoC, distanceBtoA2]
    SminimumDistance = min(Distances2)
    P2 = SminimumDistance

    print("distanceBtoA: ", distanceBtoA)
    print("distanceBtoC: ", distanceBtoC)
    print("distanceBtoA2: ", distanceBtoA2)

    print("distanceBtoA2", SminimumDistance)

    W2 = A2
    #------------------------------------------------------------------------
    #THIRD POINT
    distanceA2toA = np.linalg.norm(waypointA2-waypointA)
    distanceA2toC = np.linalg.norm(waypointA2-waypointC)
    Distances3 = [distanceA2toA, distanceA2toC]
    TminimumDistance = min(Distances3)
    P3 = TminimumDistance
    print("distanceA2toA: ", distanceA2toA)
    print("distanceA2toC: ", distanceA2toC)

    print("distanceA2toC", TminimumDistance)

    W3 = C
    #------------------------------------------------------------------------
    #FOURTH waypoint
    distanceCtoA = np.linalg.norm(waypointC-waypointA)
    Distances4 = [distanceCtoA]
    FminimumDistance = Distances4
    P4 = FminimumDistance
    print("distanceCtoA: ", distanceCtoA)

    print("distanceCtoA", FminimumDistance)

    W4 = A
    #-------------------------------------------------------------------------
    Path = ([W1, W2, W3, W4])
    print(Path)
    print("this is the waypoint order")
    return Path

    #closestWaypoint = Distances.index(minimumDistance)
    #Path = Path.append(closestWaypoint)


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


#return Path
#if __name__ == '__main__':
#	main()
