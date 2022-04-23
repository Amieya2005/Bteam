import math
import numpy as np


def determinePath(waypoint):
    waypointType = waypoint["waypointType"]
    #print(len(waypoint))
    #for index in range(len(waypoint)):

    order = []
    Lat0 = float(waypoint['latitude'][0])
    Lon0 = float(waypoint['longitude'][0])
    Alt0 = float(waypoint['altitude'][0])
    #print(waypoint['latitude'][0])
    waypointH_POS = 0
    order.append(waypointH_POS)
    print(order)
    Lat1 = float(waypoint['latitude'][1])
    Lon1 = float(waypoint['longitude'][1])
    Alt1 = float(waypoint['altitude'][1])
    waypointA = [Lat1, Lon1, Alt1]
    waypointA_POS = 1

    Lat2 = float(waypoint['latitude'][2])
    Lon2 = float(waypoint['longitude'][2])
    Alt2 = float(waypoint['altitude'][2])
    waypointC = [Lat2, Lon2, Alt2]
    waypointC_POS = 2

    Lat3 = float(waypoint['latitude'][3])
    Lon3 = float(waypoint['longitude'][3])
    Alt3 = float(waypoint['altitude'][3])
    waypointB = [Lat3, Lon3, Alt3]
    waypointB_POS = 3

    Lat4 = float(waypoint['latitude'][4])
    Lon4 = float(waypoint['longitude'][4])
    Alt4 = float(waypoint['altitude'][4])
    waypointA2 = [Lat4, Lon4, Alt4]
    waypointA2_POS = 4
#-----------------------------------------------------------------------------
    #FIRST WAYPOINT
    waypointH = np.array((Lat0, Lon0, Alt0))
    waypointA = np.array((Lat1, Lon1, Alt1))
    waypointC = np.array((Lat2, Lon2, Alt2))
    waypointB = np.array((Lat3, Lon3, Alt3))
    waypointA2 = np.array((Lat4, Lon4, Alt4))

    DistanceHtoA = np.linalg.norm(waypointH-waypointA)
    DistanceHtoC = np.linalg.norm(waypointH-waypointC)
    DistanceHtoB = np.linalg.norm(waypointH-waypointB)
    DistanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [DistanceHtoA, DistanceHtoC, DistanceHtoB, DistanceHtoA2]
    minimumDistances1 = min(Distances)

    print("Minimum Distance in Distance Dictionary=",
          Distances.index(minimumDistances1))
    minimumIndex = (Distances.index(minimumDistances1))
    print("The minimum distance is being assigned to-->", minimumIndex)
    print("Distances values", Distances)
    print("Index value 0 distance=", Distances[0])

    #this tells us what point is the closest and assigns it to 1st place in  order
    print(order)
    if (minimumIndex == 0):
        order.apend(waypointA_POS)
    elif(minimumIndex == 1):
        order.append(waypointC_POS)
    elif(minimumIndex == 2):
        order.append(waypointB_POS)
    elif(minimumIndex == 3):
        order.append(waypointA2_POS)
    print(order)
    #
    LatNH = float(waypoint['latitude'][minimumIndex])
    print("Latitude of New Home", LatNH)
    LonNH = float(waypoint['longitude'][minimumIndex])
    print("longitude of New Home", LatNH)
    AltNH = float(waypoint['altitude'][minimumIndex])
    print("Altitude of New Home", LatNH)
    waypointNH = [LatNH, LonNH, AltNH]
    #P1 = waypointNH
    print("New Home", waypointNH)
#------------------------------------------------------------------------------
    #SECOND WAYPOINT
    #P1 = minimumDistances1, "DistanceHtoB"
    #print(minimumDistances1, "minimumDistances1")

    DistanceNHtoA = np.linalg.norm(waypointNH-waypointA)
    DistanceNHtoC = np.linalg.norm(waypointNH-waypointC)
    DistanceNHtoA2 = np.linalg.norm(waypointNH-waypointA2)
    Distances2 = [DistanceNHtoA, DistanceNHtoC, DistanceNHtoA2]
    minimumDistances2 = min(Distances2)

    print("Minimum Distance in Distance Dictionary=",
          Distances2.index(minimumDistances2))
    minimumIndex2 = (Distances2.index(minimumDistances2))
    print("The minimum distance is being assigned to-->", minimumIndex2)
    print("Distances values", Distances2)
    print("Index value 0 distance=", Distances2[0])
    #this tells us what point is the closest and assigns it to 1st place in  order
    print(order)
    if (minimumIndex2 == 0):
        order.append(waypointA_POS)
    elif(minimumIndex2 == 1):
        order.append(waypointC_POS)
    elif(minimumIndex2 == 2):
        order.append(waypointA2_POS)
    print(order)

    LatNH2 = float(waypoint['latitude'][minimumIndex2])
    LonNH2 = float(waypoint['longitude'][minimumIndex2])
    AltNH2 = float(waypoint['altitude'][minimumIndex2])
    waypointNH2 = [LatNH2, LonNH2, AltNH2]

    print("Second New Home", waypointNH2)
    #print("minimunDistances2", minimumDistances2)
    #P2 = minimumDistances2, "DistanceBtoA2"
    #print("DistanceBtoC", DistanceBtoC)
    #print("DistanceBtoA", DistanceBtoA)
    #print("DistanceBtoA2", DistanceBtoA2)
#-----------------------------------------------------------------------
    #THIRD WAYPOINT
    DistanceNH2toA = np.linalg.norm(waypointNH2-waypointA)
    DistanceNH2toC = np.linalg.norm(waypointNH2-waypointC)
    Distances3 = [DistanceNH2toA, DistanceNH2toC]
    minimumDistances3 = min(Distances3)

    print("Minimum distance in the distance Dictionary=",
          Distances3.index(minimumDistances3))
    minimumIndex3 = (Distances3.index(minimumDistances3))
    print("The minimum distance is being assigned to-->", minimumIndex3)
    print("Distances values", Distances3)
    print("Index value 0 distance=", Distances3[0])
    print(order)
    if (minimumIndex3 == 0):
        order.append(waypointA_POS)
    elif(minimumIndex3 == 1):
        order.append(waypointC_POS)
    print(order)
    #this tells us what point is the closest and assigns it to 1st place in  order
    print(order)
    #if (minimumIndex3 == 0):
    #order.append(1)
    #else:
    #order.append(2)

    LatNH3 = float(waypoint['latitude'][minimumIndex3])
    LonNH3 = float(waypoint['longitude'][minimumIndex3])
    AltNH3 = float(waypoint['altitude'][minimumIndex3])
    waypointNH3 = [LatNH3, LonNH3, AltNH3]
    #P1 = waypointNH
    print("Third New Home", waypointNH3)
    #print("minimunDistances3", minimumDistances3)
    #P3 = minimumDistances3, "DistanceA2toA"
    #print("DistanceA2toA", DistanceA2toA)
    #print("DistanceA2toC", DistanceA2toC)
#----------------------------------------------------------------------------
    #FOURTH WAYPOINT
    DistanceNH3toC = np.linalg.norm(waypointNH3-waypointC)
    Distances4 = [DistanceNH3toC]
    minimumDistances4 = min(Distances4)

    print("Minimum distance in the distance Dictionary=",
          Distances4.index(minimumDistances4))
    minimumIndex4 = (Distances4.index(minimumDistances4))
    print("The minimum distance is being assigned to-->", minimumIndex4)
    print("Distances values", Distances4)
    print("Index value 0 of distance value=", Distances4[0])
    print(order)
    if (minimumIndex4 == 0):
        order.append(waypointC_POS)
    print(order)

    LatNH4 = float(waypoint['latitude'][minimumIndex4])
    LonNH4 = float(waypoint['longitude'][minimumIndex4])
    AltNH4 = float(waypoint['altitude'][minimumIndex4])
    waypointNH4 = [LatNH4, LonNH4, AltNH4]
    #P1 = waypointNH
    print("Fourth New Home", waypointNH4)
    #P4 = FminimumDistances, "DistanceAtoC"

    #Path = ([P1, P2, P3, P4])
    #print(Path)

    return order