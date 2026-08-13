## Exploring Glacial Melt Using Monte Carlo Methods
------------------------------------------
### General Simulation Logic:
1. Start with a glacier mass of n units.
2. Simulate n number of years from present.
3. For each year, the for-loop:
     - Draws a random temperature from a normal distribution.
     - Draws a random snowfall amount from a normal distribution.
     - Adds snow to the glacier.
     - Melts ice if the temperature is above 0 degree C.
     - Updates the glacier's mass.
5. Record the glacier's final mass.

At the end, the simulations estimate quantities such as:
* Average glacier mass after 50 years.
* Minimum and maximum outcomes.
* Probability the glacier completely disappears
------------------------------------------
## Environmental factors that can make the simulation more accurate:

### Replace the simple temperature*40 melt equation with a positive degree-day model
- Assumes an empirical relationship between rate of glacial melt and air temperature
- There is an abundance of air temperature data publicly available
- General Model: $M = K_{I}PDD + K_{S}PDD$

### Introduce seasonality into the simulation
- Glaciers retreat in the summer, losing their mass, and accumulate in the winter, gaining mass

### Involve solar radiation interacting with the glacier surface
- Let darker ice absorb more solar energy, increasing melt after snow cover is lost.

### Increase the average temperature slightly each year to simulate long-term atmospheric warming
- Use real atmospheric $CO_{2}$ data and train a model to predict concentrations n number of years into the future and correlate it to rate of annual atmospheric temperature rise

### Variably adjust snowfall over time to reflect real-world factors such as cold winters or droughts etc. making the available snowfall temperature and weather dependent.
- Occasionally simulate heat waves or exceptionally snowy winters.

### Reduce melt at higher elevations using a lapse rate.
- Environmental Lapse Rate (LPR) is the measured change of temperature with height in the stationary atmosphere at a certain time and location. The global average is approximately $6.5^\circ\text{C}$ per kilometer.


