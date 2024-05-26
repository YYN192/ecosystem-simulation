The simulation models the interactions between different species in an ecosystem over time, considering factors such as environmental conditions, seasonal variations, and random disasters. It provides insights into how species populations change and interact within the ecosystem.


    Species Class:
        Represents a species in the ecosystem with attributes such as name, population, base birth rate, and base death rate.
        Can adjust birth and death rates based on the current season.
        Implements methods for reproduction, death, and interactions with other species (e.g., predation, competition, symbiosis).

    Environment Class:
        Represents the environment in which the species live, with attributes such as resources and conditions.
        Can change conditions (good or bad), update resources, and simulate seasonal changes.
        Can cause disasters (e.g., fire, flood, disease) that affect species populations.

    run_simulation Function:
        Runs the simulation for a specified number of iterations.
        During each iteration:
            Changes environmental conditions.
            Updates resources based on conditions.
            Changes the season.
            Possibly causes a disaster.
            Adjusts species birth and death rates based on the season.
            Simulates reproduction, death, and interactions among species.
            Records population data for each species.

    plot_populations Function:
        Plots the population dynamics of each species over the iterations.

    Example Usage:
        Creates instances of different species with initial populations and base birth/death rates.
        Creates an environment with initial resources and conditions.
        Runs the simulation for a specified number of iterations.
        Plots the population dynamics of each species over the iterations.
