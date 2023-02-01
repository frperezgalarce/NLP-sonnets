
import numpy as np




x = np.zeros((3, 4, 5), dtype=np.bool)

i=1
for x_i in x:
	#print (i)
	print ('x_i:', x_i)
	j=1
	for x_j in x_i:
		#print (j)
		print ('x_j:', x_j)
		print ('\n')
		z=1
		for x_z in x_j:
			print (i,j,z)
			print ('x_z:', x_z)
			z+=1
		j+=1
		print ('\n')
	i+=1
	print ('\n--------\n') 


