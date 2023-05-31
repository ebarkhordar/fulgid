# """
# Erosion by the ocean:
# 1. Wind creates waves in the ocean.
# 2. The waves wash onto the beaches.
# 3. The waves hit rocks on the beach.
# 4. Tiny parts of the rock break off.
# 5. The rocks become smaller.
# """
#
#
# # Create a new variable called waves_w
# waves_w = np.zeros(len(beaches))
#
# # Wave1 = 0.1 m/s and waves_w[0] = 0.2 m/s.
# for i in range(len(beaches)):
#     waves_w[i] = (np.exp(-(beaches[i]/60.0)*0.1*np.array(beaches[i]).T) - np.exp(-(beaches[i]/60.0)*0.2*np.array(beaches[i]).T))
#
# # Calculate the rock break off
# r_w = np.sum(waves_w**2)/len(beaches)
#
# # Calculate the rock break off
# r_w = np.sum(r_w**2)/len(beaches)
#
# print(r_w)
#
# """
# The rock break off is a very small number, so it's not a problem.
# The rock break off is a small number, so it's not a problem.
# The rock break