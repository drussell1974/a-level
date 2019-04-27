from dijkstras_algorithm import Vertex, Edge, getShortestPath

nodeB = Vertex("B")
nodeC = Vertex("C")
nodeG = Vertex("G")
nodeI = Vertex("I")
nodeS = Vertex("S")
nodeT = Vertex("T")

edgeBG = Edge(17, nodeB, nodeG)
edgeBS = Edge(14, nodeB, nodeS)
edgeTG = Edge(13, nodeT, nodeG)
edgeTC = Edge(9, nodeT, nodeC)
edgeGC = Edge(9, nodeG, nodeC)
edgeCG = Edge(9, nodeC, nodeG)
edgeGB = Edge(17, nodeG, nodeB)
edgeGS = Edge(9, nodeG, nodeS)
edgeCS = Edge(14, nodeC, nodeS)
edgeCI = Edge(15, nodeC, nodeI)
edgeBS = Edge(14, nodeB, nodeS)
edgeIS = Edge(15, nodeI, nodeS)

nodeB.edges.append(edgeBG)
nodeB.edges.append(edgeBS)
nodeT.edges.append(edgeTG)
nodeT.edges.append(edgeTC)
nodeG.edges.append(edgeGC)
nodeG.edges.append(edgeGS)
nodeC.edges.append(edgeCG)
nodeC.edges.append(edgeCS)
nodeC.edges.append(edgeCI)
nodeI.edges.append(edgeIS)

vertices = {nodeB, nodeC, nodeG, nodeI, nodeS, nodeT}


route = getShortestPath(vertices, nodeT, nodeI)

print(route)