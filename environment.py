from dataclasses import dataclass, field
import random

@dataclass
class Environment:
    resources: int
    conditions: str
    season: str = 'spring'
    seasons: list = field(default_factory=lambda: ['spring', 'summer', 'autumn', 'winter'])
    season_index: int = 0
    disaster_chance: float = 0.01
    event_chance: float = 0.02
    depletion_rate: float = 0.05

    def change_conditions(self):
        self.conditions = random.choice(['good', 'bad'])

    def update_resources(self):
        self.resources += 50 if self.conditions == 'good' else -50
        self.resources = max(0, self.resources - int(self.resources * self.depletion_rate))

    def change_season(self):
        self.season_index = (self.season_index + 1) % len(self.seasons)
        self.season = self.seasons[self.season_index]

    def cause_disaster(self, species_list):
        if random.random() < self.disaster_chance:
            disaster_type = random.choice(['fire', 'flood', 'disease'])
            for species in species_list:
                if disaster_type == 'fire':
                    species.population = max(0, int(species.population * 0.9))
                elif disaster_type == 'flood':
                    species.population = max(0, int(species.population * 0.85))
                elif disaster_type == 'disease':
                    species.population = max(0, int(species.population * 0.8))
            return disaster_type
        return None

    def cause_event(self, species_list):
        if random.random() < self.event_chance:
            event_type = random.choice(['drought', 'cold_snap', 'food_abundance'])
            for species in species_list:
                if event_type == 'drought':
                    species.population = max(0, int(species.population * 0.95))
                elif event_type == 'cold_snap':
                    species.population = max(0, int(species.population * 0.9))
                elif event_type == 'food_abundance':
                    species.population += int(species.population * 0.1)
            return event_type
        return None
