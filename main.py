import random
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import json


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


class Environment:
    def __init__(self, resources, conditions, season='spring'):
        self.resources = resources
        self.conditions = conditions
        self.season = season
        self.seasons = ['spring', 'summer', 'autumn', 'winter']
        self.season_index = 0
        self.disaster_chance = 0.01  # 10% chance of a disaster each iteration
        self.event_chance = 0.02  # 20% chance of a special event each iteration
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


def run_simulation(species_list, environment, iterations):
    populations = {species.name: [] for species in species_list}
    logs = []

    for i in range(iterations):
        log_entry = {
            "iteration": i + 1,
            "season": environment.season,
            "conditions": environment.conditions,
            "resources": environment.resources,
            "events": []
        }

        environment.change_conditions()
        environment.update_resources()
        environment.change_season()

        disaster_occurred = environment.cause_disaster(species_list)
        if disaster_occurred:
            log_entry["events"].append(f"Disaster occurred: {disaster_occurred}")

        event_occurred = environment.cause_event(species_list)
        if event_occurred:
            log_entry["events"].append(f"Event occurred: {event_occurred}")

        log_entry["season"] = environment.season
        log_entry["resources"] = environment.resources
        log_entry["conditions"] = environment.conditions

        for species in species_list:
            species.adjust_rates_for_season(environment.season)
            species.reproduce()
            species.die()
            for other_species in species_list:
                if species != other_species:
                    species.interact(other_species)
            log_entry[species.name] = species.population
            populations[species.name].append(species.population)

        logs.append(log_entry)

    return populations, logs


def generate_report(logs):
    report_lines = []
    report_lines.append("Simulation Report")
    report_lines.append("=================")
    for log in logs:
        report_lines.append(f"Iteration {log['iteration']}")
        report_lines.append(f"  Season: {log['season']}")
        report_lines.append(f"  Resources: {log['resources']}")
        report_lines.append(f"  Conditions: {log['conditions']}")
        for event in log.get("events", []):
            report_lines.append(f"  Event: {event}")
        for species_name, population in log.items():
            if species_name not in ['iteration', 'season', 'conditions', 'resources', 'events']:
                report_lines.append(f"  {species_name} Population: {population}")
        report_lines.append("")
    return "\n".join(report_lines)


def plot_populations(populations, iterations):
    plt.figure(figsize=(10, 6))
    for species, population in populations.items():
        plt.plot(range(iterations), population, label=species)
    plt.xlabel('Iterations')
    plt.ylabel('Population')
    plt.title('Ecosystem Simulation')
    plt.legend()
    plt.show()


def export_logs(logs, filename):
    with open(filename, 'w') as f:
        json.dump(logs, f, indent=4)


# Global variable to store logs
logs = []

def start_simulation():
    global logs  # Declare logs as global to modify it
    try:
        iterations = int(iterations_entry.get())
        resources = int(resources_entry.get())

        species_list = [
            Species(name='Rabbits', population=int(rabbits_population_entry.get()),
                    base_birth_rate=float(rabbits_birth_rate_entry.get()),
                    base_death_rate=float(rabbits_death_rate_entry.get())),
            Species(name='Wolves', population=int(wolves_population_entry.get()),
                    base_birth_rate=float(wolves_birth_rate_entry.get()),
                    base_death_rate=float(wolves_death_rate_entry.get())),
            Species(name='Deer', population=int(deer_population_entry.get()),
                    base_birth_rate=float(deer_birth_rate_entry.get()),
                    base_death_rate=float(deer_death_rate_entry.get())),
            Species(name='Bears', population=int(bears_population_entry.get()),
                    base_birth_rate=float(bears_birth_rate_entry.get()),
                    base_death_rate=float(bears_death_rate_entry.get())),
            Species(name='Eagles', population=int(eagles_population_entry.get()),
                    base_birth_rate=float(eagles_birth_rate_entry.get()),
                    base_death_rate=float(eagles_death_rate_entry.get())),
            Species(name='Foxes', population=int(foxes_population_entry.get()),
                    base_birth_rate=float(foxes_birth_rate_entry.get()),
                    base_death_rate=float(foxes_death_rate_entry.get())),
            Species(name='Hawks', population=int(hawks_population_entry.get()),
                    base_birth_rate=float(hawks_birth_rate_entry.get()),
                    base_death_rate=float(hawks_death_rate_entry.get()))
        ]

        environment = Environment(resources=resources, conditions='good')
        populations, logs = run_simulation(species_list, environment, iterations)
        report = generate_report(logs)
        messagebox.showinfo("Simulation Report", report)
        plot_populations(populations, iterations)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")


def save_logs():
    filename = filename_entry.get()
    if filename:
        export_logs(logs, filename)
        messagebox.showinfo("Save Logs", f"Logs saved to {filename}")
    else:
        messagebox.showerror("Input Error", "Please enter a filename")


# Create the UI using tkinter
root = tk.Tk()
root.title("Ecosystem Simulation")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Iterations:").grid(row=0, column=0, sticky=tk.W)
iterations_entry = ttk.Entry(mainframe)
iterations_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Resources:").grid(row=1, column=0, sticky=tk.W)
resources_entry = ttk.Entry(mainframe)
resources_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

species_frame = ttk.LabelFrame(mainframe, text="Species Parameters", padding="10 10 20 20")
species_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Rabbits Population:").grid(row=0, column=0, sticky=tk.W)
rabbits_population_entry = ttk.Entry(species_frame)
rabbits_population_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Rabbits Birth Rate:").grid(row=1, column=0, sticky=tk.W)
rabbits_birth_rate_entry = ttk.Entry(species_frame)
rabbits_birth_rate_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Rabbits Death Rate:").grid(row=2, column=0, sticky=tk.W)
rabbits_death_rate_entry = ttk.Entry(species_frame)
rabbits_death_rate_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Wolves Population:").grid(row=3, column=0, sticky=tk.W)
wolves_population_entry = ttk.Entry(species_frame)
wolves_population_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Wolves Birth Rate:").grid(row=4, column=0, sticky=tk.W)
wolves_birth_rate_entry = ttk.Entry(species_frame)
wolves_birth_rate_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Wolves Death Rate:").grid(row=5, column=0, sticky=tk.W)
wolves_death_rate_entry = ttk.Entry(species_frame)
wolves_death_rate_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Deer Population:").grid(row=6, column=0, sticky=tk.W)
deer_population_entry = ttk.Entry(species_frame)
deer_population_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Deer Birth Rate:").grid(row=7, column=0, sticky=tk.W)
deer_birth_rate_entry = ttk.Entry(species_frame)
deer_birth_rate_entry.grid(row=7, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Deer Death Rate:").grid(row=8, column=0, sticky=tk.W)
deer_death_rate_entry = ttk.Entry(species_frame)
deer_death_rate_entry.grid(row=8, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Bears Population:").grid(row=9, column=0, sticky=tk.W)
bears_population_entry = ttk.Entry(species_frame)
bears_population_entry.grid(row=9, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Bears Birth Rate:").grid(row=10, column=0, sticky=tk.W)
bears_birth_rate_entry = ttk.Entry(species_frame)
bears_birth_rate_entry.grid(row=10, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Bears Death Rate:").grid(row=11, column=0, sticky=tk.W)
bears_death_rate_entry = ttk.Entry(species_frame)
bears_death_rate_entry.grid(row=11, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Eagles Population:").grid(row=12, column=0, sticky=tk.W)
eagles_population_entry = ttk.Entry(species_frame)
eagles_population_entry.grid(row=12, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Eagles Birth Rate:").grid(row=13, column=0, sticky=tk.W)
eagles_birth_rate_entry = ttk.Entry(species_frame)
eagles_birth_rate_entry.grid(row=13, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Eagles Death Rate:").grid(row=14, column=0, sticky=tk.W)
eagles_death_rate_entry = ttk.Entry(species_frame)
eagles_death_rate_entry.grid(row=14, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Foxes Population:").grid(row=15, column=0, sticky=tk.W)
foxes_population_entry = ttk.Entry(species_frame)
foxes_population_entry.grid(row=15, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Foxes Birth Rate:").grid(row=16, column=0, sticky=tk.W)
foxes_birth_rate_entry = ttk.Entry(species_frame)
foxes_birth_rate_entry.grid(row=16, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Foxes Death Rate:").grid(row=17, column=0, sticky=tk.W)
foxes_death_rate_entry = ttk.Entry(species_frame)
foxes_death_rate_entry.grid(row=17, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Hawks Population:").grid(row=18, column=0, sticky=tk.W)
hawks_population_entry = ttk.Entry(species_frame)
hawks_population_entry.grid(row=18, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Hawks Birth Rate:").grid(row=19, column=0, sticky=tk.W)
hawks_birth_rate_entry = ttk.Entry(species_frame)
hawks_birth_rate_entry.grid(row=19, column=1, sticky=(tk.W, tk.E))

ttk.Label(species_frame, text="Hawks Death Rate:").grid(row=20, column=0, sticky=tk.W)
hawks_death_rate_entry = ttk.Entry(species_frame)
hawks_death_rate_entry.grid(row=20, column=1, sticky=(tk.W, tk.E))

ttk.Button(mainframe, text="Start Simulation", command=start_simulation).grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Save Logs", command=save_logs).grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Filename:").grid(row=5, column=0, sticky=tk.W)
filename_entry = ttk.Entry(mainframe)
filename_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

root.mainloop()
