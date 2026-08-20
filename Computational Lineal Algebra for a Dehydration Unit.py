import numpy as np

#The operation conditions are stablished:
flow_compositions = np.array([
    [0.95, 0.01, 0.00, 0.04],
    [0.05, 0.90, 0.00, 0.05],
    [0.01, 0.05, 0.94, 0.00],
    [0.10, 0.15, 0.05, 0.70]   
])

feed = np.array([5000.0, 1200.0, 8500.0, 600.0])

flows = ["Dry Gas", "Acid Water", "Rich Glycol", "Tail Gas"]

#check if the system has a solution by calculating the determinate of the matrix
#if a solution exists the solution is calculated
if np.linalg.det(flow_compositions) != 0:
	flow_compositions_T = flow_compositions.T
	x = np.linalg.solve(flow_compositions_T, feed)

	#verification of the result
	check_x = flow_compositions_T@x
	for i in np.arange(len(flows)):
		print(f"{flows[i]} flow: {x[i]:.2f}kg/s")

	print(f"\nReal feed: {feed} \nChecked feed: {check_x}")
#otherwise an alert will be printed
else:
	print("The system doesnt have an unique solution")
