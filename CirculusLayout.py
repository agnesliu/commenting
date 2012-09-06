pi = 3.1415926
radius = 100

groupArray = groupBy(grp)

num_group = len(groupArray)
group_delta_theta = (2*pi)/(2*num_group)

theta = 0
for i in groupArray:
		num_node = len(i)
		member_delta_theta = group_delta_theta / num_node
		for j in i: 
			j.x = radius*math.sin(theta)
			j.y = radius*math.cos(theta)
			theta = theta + member_delta_theta
		theta = theta + group_delta_theta 	
		
center
		