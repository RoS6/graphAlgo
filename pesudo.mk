for(i =0,i++,i<number of row in graph):
	if



size of graph = n
<> addColour(row_index):
	required_colour = find the missed colour(s)
	if required_colour = none:
		//the node has connected to at least 3 nodes with 3 colours
		return
	for every required colour **colour**:
		search all columns **col** through the row, if there is a undecided edge, and the edge can be the colour(not forbidden),
			the first undecided edge is filled with the required colour
	if required colour != empty
		increase the size of the graph (n+1) * (n+1)
		addColour(row_index)
		should be added to the last column

find the forbidden colour for each node:


