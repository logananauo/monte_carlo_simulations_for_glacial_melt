import numpy as np
import matplotlib.pyplot as plt




def glacial_melt_simulation(
    years=50,
    simulations=100_000,
    initial_mass=1000.00,
    mean_temp=1.0,
    temp_std=1.5,
    mean_snow=120,
    snow_std=20
):
    """
    Monte Carlo simulation of glacial mass balance using NumPy.
    Returns final ice masses for length of run and plots their distribution.
    """
    
    masses = np.full(simulations, initial_mass, dtype=float)
    temps = np.random.normal(mean_temp, temp_std, size=(years, simulations))
    snowfalls = np.random.normal(mean_snow, snow_std, size=(years, simulations))

    ### calculate net annual changes for all years/simulations
    accumulations = snowfalls * 0.50
    melts = np.where(temps > 0, temps * 40.0, 0.0)
    net_balances = accumulations - melts

    for year in range(years):
        masses += net_balances[year]
        # np.clip forces any negative mass values to instantly lock to 0
        masses = np.clip(masses, 0, None)

    ### calculate summary statistics
    average_mass = np.mean(masses)
    minimum_mass = np.min(masses)
    maximum_mass = np.max(masses)
    lost_glacier = np.sum(masses == 0)
    probability_disappears = lost_glacier / simulations

    ### print results
    print(f'===== RESULTS =====')
    print(f'Simulations: {simulations:,}')
    print(f'Years simulated: {years}')
    print(f'Average final glacier mass: {average_mass:.2f}')
    print(f'Minimum final mass: {minimum_mass:.2f}')
    print(f'Maximum final mass: {maximum_mass:.2f}')
    print(f'Probability glacier disappears: {probability_disappears:.2%}\n')


    ### histogram of distribution
    plt.figure(figsize=(10, 6))
    plt.hist(masses, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f"Distribution of Final Glacier Mass After {years} Years", fontsize=14, fontweight='bold')
    plt.xlabel("Final Mass (Arbitrary Units)", fontsize=12)
    plt.ylabel("Number of Simulation Runs", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.axvline(average_mass, color='red', linestyle='dashed', linewidth=2, label=f'Average Mass: {average_mass:.1f}')
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.show()

    return masses

# Execute the code
final_mass_data = glacial_melt_simulation()
