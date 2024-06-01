import random

class Species:
    def __init__(self, name, population, base_birth_rate, base_death_rate, predation_rate=0.1):
        self.name = name
        self.population = population
        self.base_birth_rate = base_birth_rate
        self.base_death_rate = base_death_rate
        self.birth_rate = base_birth_rate
        self.death_rate = base_death_rate
        self.predation_rate = predation_rate

    def adjust_rates_for_season(self, season):
        if season == 'spring':
            self.birth_rate = self.base_birth_rate * 1.2
            self.death_rate = self.base_death_rate * 0.9
        elif season == 'summer':
            self.birth_rate = self.base_birth_rate
            self.death_rate = self.base_death_rate
        elif season == 'autumn':
            self.birth_rate = self.base_birth_rate * 0.8
            self.death_rate = self.base_death_rate * 1.1
        elif season == 'winter':
            self.birth_rate = self.base_birth_rate * 0.6
            self.death_rate = self.base_death_rate * 1.3

    def reproduce(self):
        births = int(self.population * self.birth_rate)
        self.population += births

    def die(self):
        deaths = int(self.population * self.death_rate)
        self.population -= deaths

    def interact(self, other_species):
        if self.name == 'Eagles' and other_species.name == 'Rabbits':
            self.prey_on(other_species)
        elif self.name == 'Wolves' and other_species.name in ['Deer', 'Rabbits']:
            self.prey_on(other_species)
        elif self.name == 'Bears' and other_species.name in ['Deer', 'Rabbits']:
            self.prey_on(other_species)
        elif self.name == 'Foxes' and other_species.name == 'Rabbits':
            self.prey_on(other_species)
        elif self.name == 'Hawks' and other_species.name in ['Rabbits', 'Foxes']:
            self.prey_on(other_species)
        elif self.name == 'Deer' and other_species.name == 'Rabbits':
            self.competition_for_food(other_species)
        else:
            interaction_type = random.choice(['competition', 'symbiosis'])
            if interaction_type == 'competition':
                self.competition(other_species)
            elif interaction_type == 'symbiosis':
                self.symbiosis(other_species)

    def prey_on(self, prey):
        prey_loss = int(prey.population * self.predation_rate)
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
