Ecosystem Simulation

This project simulates an ecosystem with various species interacting with each other and the environment over multiple iterations. The simulation includes birth and death rates influenced by seasons, interspecies interactions, resource availability, and environmental disasters.
Classes
Species

Represents a species in the ecosystem with the following attributes and methods:

    Attributes:
        name: The name of the species.
        population: The initial population of the species.
        base_birth_rate: The base birth rate of the species.
        base_death_rate: The base death rate of the species.
        birth_rate: The adjusted birth rate based on the season.
        death_rate: The adjusted death rate based on the season.
    Methods:
        adjust_rates_for_season(season): Adjusts the birth and death rates based on the current season.
        reproduce(): Increases the population based on the birth rate.
        die(): Decreases the population based on the death rate.
        interact(other_species): Defines interactions with another species, such as predation, competition, and symbiosis.
        prey_on_rabbits(rabbits): Eagles prey on rabbits.
        prey_on_deer(deer): Wolves prey on deer.
        prey_on_smaller_animals(prey): Bears prey on smaller animals.
        competition_for_food(other_species): Competition between deer and rabbits for food.
        competition(other_species): General competition between species.
        symbiosis(other_species): Symbiotic relationship between species.

Environment

Represents the environment in which the species live with the following attributes and methods:

    Attributes:
        resources: The amount of resources available in the environment.
        conditions: The current condition of the environment ('good' or 'bad').
        season: The current season ('spring', 'summer', 'autumn', 'winter').
        seasons: List of seasons to cycle through.
        season_index: Index to keep track of the current season.
        disaster_chance: The probability of a disaster occurring each iteration (10%).
        depletion_rate: The rate at which resources deplete each iteration (5%).
    Methods:
        change_conditions(): Randomly changes the environmental conditions.
        update_resources(): Updates the resources based on the current conditions and depletion rate.
        change_season(): Cycles to the next season.
        cause_disaster(species_list): Potentially causes a disaster affecting the species populations.

Functions
run_simulation(species_list, environment, iterations)

Runs the simulation over a specified number of iterations.

    Parameters:
        species_list: A list of Species objects.
        environment: An Environment object.
        iterations: The number of iterations to run the simulation.
    Returns:
        populations: A dictionary containing the population history of each species.

plot_populations(populations, iterations)

Plots the populations of the species over the iterations.

    Parameters:
        populations: A dictionary containing the population history of each species.
        iterations: The number of iterations the simulation was run.

User Interface (UI)

Implemented a user interface using tkinter to allow users to dynamically control simulation parameters and interact with the simulation.

    Implemented Functionality:
        Control Simulation Parameters: Users can specify parameters such as iterations, resources, species populations, birth rates, and death rates through input fields.
        Start Simulation: Users can start the simulation with the specified parameters by clicking a button.
        Display Simulation Report: After the simulation completes, a report summarizing each iteration is displayed in a message box.
        Plot Population Dynamics: The population dynamics of each species are plotted over the iterations for visual analysis.

Export Logs

Added the ability to export simulation logs and reports to a file for further analysis.

    Implemented Functionality:
        Save Logs: Users can specify a filename and save the simulation logs and report to a JSON file by clicking a button.
        Exported Data: The exported file contains detailed information about each iteration, including season, conditions, resources, events, and population of each species.
        Ease of Analysis: Exporting logs allows users to analyze simulation data using external tools or perform custom analysis beyond the capabilities of the built-in report display.

This project is licensed under the MIT License. See the LICENSE file for details.




https://github.com/YYN192/ecosystem-simulation/assets/110526560/bedc93dc-b9a6-4ace-b61b-15a6f6c849db

