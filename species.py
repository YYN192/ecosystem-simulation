from dataclasses import dataclass, field
import random

@dataclass
class Species:
    name: str
    population: int
    base_birth_rate: float
    base_death_rate: float
    predation_rate: float = 0.1
    birth_rate: float = field(init=False)
    death_rate: float = field(init=False)

    def __post_init__(self):
        self.birth_rate = self.base_birth_rate
        self.death_rate = self.base_death_rate

    def adjust_rates_for_season(self, season):
        rates = {
            'spring': (1.2, 0.9),
            'summer': (1.0, 1.0),
            'autumn': (0.8, 1.1),
            'winter': (0.6, 1.3)
        }
        self.birth_rate = self.base_birth_rate * rates[season][0]
        self.death_rate = self.base_death_rate * rates[season][1]

    def reproduce(self):
        self.population += int(self.population * self.birth_rate)

    def die(self):
        self.population -= int(self.population * self.death_rate)

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
            self.random_interaction(other_species)

    def prey_on(self, prey):
        prey_loss = min(int(prey.population * self.predation_rate), self.population)
        prey.population -= prey_loss
        self.population += prey_loss

    def competition_for_food(self, other_species):
        competition_rate = 0.03
        self.population -= int(self.population * competition_rate)
        other_species.population -= int(other_species.population * competition_rate)

    def random_interaction(self, other_species):
        interaction_type = random.choice(['competition', 'symbiosis'])
        if interaction_type == 'competition':
            self.competition(other_species)
        else:
            self.symbiosis(other_species)

    def competition(self, other_species):
        competition_rate = 0.05
        self.population -= int(self.population * competition_rate)
        other_species.population -= int(other_species.population * competition_rate)

    def symbiosis(self, other_species):
        symbiosis_rate = 0.02
        self.population += int(other_species.population * symbiosis_rate)
        other_species.population += int(self.population * symbiosis_rate)
