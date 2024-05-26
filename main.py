import random
import matplotlib.pyplot as plt

class Species:
    def __init__(self, name, population, base_birth_rate, base_death_rate):
        self.name = name
        self.population = population
        self.base_birth_rate = base_birth_rate
        self.base_death_rate = base_death_rate
        self.birth_rate = base_birth_rate
        self.death_rate = base_death_rate

    def adjust_rates_for_season(self, season):
        if season == 'spring':
            self.birth_rate = self.base_birth_rate * 1.5
            self.death_rate = self.base_death_rate * 0.8
        elif season == 'summer':
            self.birth_rate = self.base_birth_rate
            self.death_rate = self.base_death_rate
        elif season == 'autumn':
            self.birth_rate = self.base_birth_rate * 0.8
            self.death_rate = self.base_death_rate * 1.2
        elif season == 'winter':
            self.birth_rate = self.base_birth_rate * 0.5
            self.death_rate = self.base_death_rate * 1.5

    def reproduce(self):
        births = self.population * self.birth_rate
        self.population += int(births)

    def die(self):
        deaths = self.population * self.death_rate
        self.population -= int(deaths)

    def interact(self, other_species):
        if self.name == 'Eagles' and other_species.name == 'Rabbits':
            self.prey_on_rabbits(other_species)
        elif self.name == 'Wolves' and other_species.name == 'Deer':
            self.prey_on_deer(other_species)
        elif self.name == 'Bears' and other_species.name in ['Rabbits', 'Deer']:
            self.prey_on_smaller_animals(other_species)
        elif self.name == 'Deer' and other_species.name == 'Rabbits':
            self.competition_for_food(other_species)
        else:
            interaction_type = random.choice(['competition', 'symbiosis'])
            if interaction_type == 'competition':
                self.competition(other_species)
            elif interaction_type == 'symbiosis':
                self.symbiosis(other_species)

    def prey_on_rabbits(self, rabbits):
        predation_rate = 0.15
        prey_loss = int(rabbits.population * predation_rate)
        prey_loss = min(prey_loss, self.population)
        rabbits.population -= prey_loss
        self.population += prey_loss

    def prey_on_deer(self, deer):
        predation_rate = 0.1
        prey_loss = int(deer.population * predation_rate)
        prey_loss = min(prey_loss, self.population)
        deer.population -= prey_loss
        self.population += prey_loss

    def prey_on_smaller_animals(self, prey):
        predation_rate = 0.05
        prey_loss = int(prey.population * predation_rate)
        prey_loss = min(prey_loss, self.population)
        prey.population -= prey_loss
        self.population += prey_loss

    def competition_for_food(self, other_species):
        competition_rate = 0.03
        self_loss = int(self.population * competition_rate)
        other_loss = int(other_species.population * competition_rate)
        self.population -= self_loss
        other_species.population -= other_loss

    def competition(self, other_species):
        competition_rate = 0.05
        self_loss = int(self.population * competition_rate)
        other_loss = int(other_species.population * competition_rate)
        self.population -= self_loss
        other_species.population -= other_loss

    def symbiosis(self, other_species):
        symbiosis_rate = 0.02
        self_gain = int(other_species.population * symbiosis_rate)
        other_gain = int(self.population * symbiosis_rate)
        self.population += self_gain
        other_species.population += other_gain

class Environment:
    def __init__(self, resources, conditions, season='spring'):
        self.resources = resources
        self.conditions = conditions
        self.season = season
        self.seasons = ['spring', 'summer', 'autumn', 'winter']
        self.season_index = 0
        self.disaster_chance = 0.1  # 10% chance of a disaster each iteration
        self.depletion_rate = 0.05  # 5% resource depletion each iteration

    def change_conditions(self):
        self.conditions = random.choice(['good', 'bad'])

    def update_resources(self):
        if self.conditions == 'good':
            self.resources += 50
        elif self.conditions == 'bad':
            self.resources -= 50
        self.resources = max(0, self.resources - int(self.resources * self.depletion_rate))

    def change_season(self):
        self.season_index = (self.season_index + 1) % len(self.seasons)
        self.season = self.seasons[self.season_index]

    def cause_disaster(self, species_list):
        if random.random() < self.disaster_chance:
            disaster_type = random.choice(['fire', 'flood', 'disease'])
            print(f"Disaster: {disaster_type}")
            for species in species_list:
                if disaster_type == 'fire':
                    species.population = max(0, int(species.population * 0.9))
                elif disaster_type == 'flood':
                    species.population = max(0, int(species.population * 0.85))
                elif disaster_type == 'disease':
                    species.population = max(0, int(species.population * 0.8))

def run_simulation(species_list, environment, iterations):
    populations = {species.name: [] for species in species_list}

    for i in range(iterations):
        print(f"Iteration {i + 1}")
        environment.change_conditions()
        environment.update_resources()
        environment.change_season()
        environment.cause_disaster(species_list)
        print(f"Season = {environment.season}")
        for species in species_list:
            species.adjust_rates_for_season(environment.season)
            species.reproduce()
            species.die()
            for other_species in species_list:
                if species != other_species:
                    species.interact(other_species)
            print(f"{species.name}: Population = {species.population}")
            populations[species.name].append(species.population)
        print(f"Resources = {environment.resources}, Conditions = {environment.conditions}\n")

    return populations

def plot_populations(populations, iterations):
    plt.figure(figsize=(10, 6))
    for species, population in populations.items():
        plt.plot(range(iterations), population, label=species)
    plt.xlabel('Iterations')
    plt.ylabel('Population')
    plt.title('Ecosystem Simulation')
    plt.legend()
    plt.show()

# Example usage with more species
species1 = Species(name='Rabbits', population=100, base_birth_rate=0.1, base_death_rate=0.05)
species2 = Species(name='Wolves', population=50, base_birth_rate=0.05, base_death_rate=0.02)
species3 = Species(name='Deer', population=80, base_birth_rate=0.08, base_death_rate=0.04)
species4 = Species(name='Bears', population=20, base_birth_rate=0.02, base_death_rate=0.01)
species5 = Species(name='Eagles', population=30, base_birth_rate=0.03, base_death_rate=0.02)

species_list = [species1, species2, species3, species4, species5]
environment = Environment(resources=500, conditions='good')

iterations = 50
populations = run_simulation(species_list, environment, iterations)
plot_populations(populations, iterations)
