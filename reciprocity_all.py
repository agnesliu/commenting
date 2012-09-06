reci_counter = 0.0
max_reci = 0.0
reci = 0.0
g.edges.visible = 0
g.edges.color = orange

for i in g.nodes:
	for j in (i->g.nodes):
		reci = len( i->j.node2) + len(j.node2->i)
		(i->j.node2).visible = 1
		(j.node2->i).visible = 1
		
		if reci >= 6:
			reci_edge = (i, j.node2)
			print reci_edge
			print reci

			