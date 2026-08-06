
import random
import numpy as np


#-----------------------#
# Simulation Parameters #
#-----------------------#

# years to simulate
Years = 50

# number of runs
simulations = 100_000

# units of glacial ice mass (arbitrary)
initial_mass = 1000.00

# climate assumptions
mean_temp = 1.0 # deg C
temp_std = 1.5

mean_snow = 120 # cm/year
snow_std = 20



### each run, mass is recalculated and stored in this list
final_masses = []


# -----------------------#
# Monte Carlo Simulation #
# -----------------------#

for i in range(simulations):
    
    mass = initial_mass
    
    for year in range(Years):
        
        
        # random yearly climate
        temperature = random.gauss(mean_temp, temp_std)
        snowfall= random.gauss(mean_snow, snow_std)
         
        # snow accumulation
        accumulation = snowfall * 0.50
         
        # ice melt
        if temperature > 0:
            melt = temperature * 40
        else:
            
            melt = 0
         
        # annual mass balance
        mass += accumulation - melt
        
        # glacier cannot have negative mass
        if mass < 0:
            mass = 0
            break
    
    final_masses.append(mass)
    

#---------------------#
#       Results       #
#---------------------#

average_mass = np.mean(final_masses)
minimum_mass = min(final_masses)
maximum_mass = max(final_masses)

lost_glacier = sum(m == 0 for m in final_masses)
probability_disappears = lost_glacier / simulations

print(f"Simulations: {simulations}")
print(f"Years simulated: {Years}")
print(f"Average final glacier mass: {average_mass:.2f}")
print(f"Minimum final mass: {minimum_mass:.2f}")
print(f"Maximum final mass: {maximum_mass:.2f}")
print(f"Probability glacier disappears: {probability_disappears:.2%}")























