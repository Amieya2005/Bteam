import math
import numpy as np

order = [0, 1, 2, 3, 4]
O


def determinePath(waypoint):
    Lat0 = float(waypoint['latitude'][0])
    Lon0 = float(waypoint['longitude'][0])
    Alt0 = float(waypoint['altitude'][0])
    #print(waypoint['latitude'][0])
    W0 = [Lat0, Lon0, Alt0]

    Lat1 = float(waypoint['latitude'][1])
    Lon1 = float(waypoint['longitude'][1])
    Alt1 = float(waypoint['altitude'][1])
    W1 = [Lat1, Lon1, Alt1]

    Lat2 = float(waypoint['latitude'][2])
    Lon2 = float(waypoint['longitude'][2])
    Alt2 = float(waypoint['altitude'][2])
    waypointC = [Lat2, Lon2, Alt2]

    Lat3 = float(waypoint['latitude'][3])
    Lon3 = float(waypoint['longitude'][3])
    Alt3 = float(waypoint['altitude'][3])
    waypointB = [Lat3, Lon3, Alt3]

    Lat4 = float(waypoint['latitude'][4])
    Lon4 = float(waypoint['longitude'][4])
    Alt4 = float(waypoint['altitude'][4])
    waypointA2 = [Lat4, Lon4, Alt4]

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

    print(Distances.index(minimumDistances1))
    minimumIndex = (Distances.index(minimumDistances1))+1

    LatNH = float(waypoint['latitude'][minimumIndex])
    LonNH = float(waypoint['longitude'][minimumIndex])
    AltNH = float(waypoint['altitude'][minimumIndex])
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
    print(Distances2.index(minimumDistances2))
    minimumIndex2 = (Distances2.index(minimumDistances2))+2

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

    print("index Minimum distance 3", Distances3.index(minimumDistances3))
    minimumIndex3 = (Distances3.index(minimumDistances3))+3

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

    print("index Minimum distance 4", Distances4.index(minimumDistances4))
    minimumIndex4 = (Distances4.index(minimumDistances4))+4

    LatNH4 = float(waypoint['latitude'][minimumIndex4])
    LonNH4 = float(waypoint['longitude'][minimumIndex4])
    AltNH4 = float(waypoint['altitude'][minimumIndex4])
    waypointNH4 = [LatNH4, LonNH4, AltNH4]
    #P1 = waypointNH
    print("Fourth New Home", waypointNH4)
    #P4 = FminimumDistances, "DistanceAtoC"

    #Path = ([P1, P2, P3, P4])
    #print(Path)
    order = [0, 1, 2, 3, 4]
    return order
