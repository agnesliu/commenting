reci_counter = 0.0
max_reci = 0.0
reci = 0.0

g.edges.visible = 0

for i in g.nodes:
	for j in (i->g.nodes):
		reci_counter = 0
		for k in (j.node2->i):
			if (k.week == j.week):
				k.visible = 1
				k.color = red
				j.visible = 1
				j.color = red
				reci_counter = reci_counter + 1
				#print reci_counter
		
		#Since some nodes don't comment on other nodes, we need to set their reci to be 0
		if (j.node2).outdegree == 0:
			reci = 0
		else:
			reci = reci_counter / float((j.node2).outdegree)
		
		#Output for R
		#print reci
		#print ','
		
		#only see the nodes has higher than 2 reci
		if reci_counter >= 2:
			print (j.node2, i)
			print reci_counter 
			