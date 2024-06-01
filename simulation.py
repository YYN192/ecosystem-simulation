import matplotlib.pyplot as plt
import json

from species import Species
from environment import Environment

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
