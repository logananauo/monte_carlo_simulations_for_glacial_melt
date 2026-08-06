# Exploring Glacial Melt Using Monte Carlo Methods

## general_simulation pseudocode:
1. Start with a glacier mass of n units.
2. Simulate n years.
3. Each year:
   * Draw a random temperature from a normal distribution.
   * Draw a random snowfall amount from a normal distribution.
   * Add snow to the glacier.
   * Melt ice if the temperature is above 0 degree C.
   * Update the glacier's mass.
4. Record the glacier's final mass.

At the end, we estimate quantities such as:
* Average glacier mass after 50 years.
* Minimum and maximum outcomes.
* Probability the glacier completely disappears

## Goals for making the simulation more accurate:
* Increase the average temperature slightly each year to simulate long-term atmospheric warming.
* Decrease average snowfall over time or make it temperature-dependent
* Reduce melt at higher elevations using a lapse rate.
* Let darker ice absorb more solar energy, increasing melt after snow cover is lost.
* Replace the simple temperture*40 melt equation with a positive degree-day model commonly used in glacier studies
* Occasionally simulate heat waves or exceptionally snowy winters.
