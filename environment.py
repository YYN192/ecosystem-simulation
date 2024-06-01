import random

class Environment:
    def __init__(self, resources, conditions, season='spring'):
        self.resources = resources
        self.conditions = conditions
        self.season = season
        self.seasons = ['spring', 'summer', 'autumn', 'winter']
        self.season_index = 0
        self.disaster_chance = 0.01  # 1% chance of a disaster each iteration
        self.event_chance = 0.02  # 2% chance of a special event each iteration
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
