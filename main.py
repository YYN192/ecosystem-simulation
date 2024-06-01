import tkinter as tk
from tkinter import ttk, messagebox
from species import Species
from environment import Environment
from simulation import run_simulation, generate_report, plot_populations, export_logs

# Global variable to store logs
logs = []

def start_simulation():
    global logs
    try:
        iterations = int(iterations_entry.get())
        resources = int(resources_entry.get())

        species_list = [
            Species(name='Rabbits', population=int(rabbits_population_entry.get()),
                    base_birth_rate=float(rabbits_birth_rate_entry.get()),
                    base_death_rate=float(rabbits_death_rate_entry.get())),
            Species(name='Deer', population=int(deer_population_entry.get()),
                    base_birth_rate=float(deer_birth_rate_entry.get()),
                    base_death_rate=float(deer_death_rate_entry.get())),
            Species(name='Eagles', population=int(eagles_population_entry.get()),
                    base_birth_rate=float(eagles_birth_rate_entry.get()),
                    base_death_rate=float(eagles_death_rate_entry.get())),
            Species(name='Wolves', population=int(wolves_population_entry.get()),
                    base_birth_rate=float(wolves_birth_rate_entry.get()),
                    base_death_rate=float(wolves_death_rate_entry.get())),
            Species(name='Bears', population=int(bears_population_entry.get()),
                    base_birth_rate=float(bears_birth_rate_entry.get()),
                    base_death_rate=float(bears_death_rate_entry.get())),
            Species(name='Foxes', population=int(foxes_population_entry.get()),
                    base_birth_rate=float(foxes_birth_rate_entry.get()),
                    base_death_rate=float(foxes_death_rate_entry.get())),
            Species(name='Hawks', population=int(hawks_population_entry.get()),
                    base_birth_rate=float(hawks_birth_rate_entry.get()),
                    base_death_rate=float(hawks_death_rate_entry.get()))
        ]

        environment = Environment(resources=resources, conditions='good')

        populations, logs = run_simulation(species_list, environment, iterations)
        plot_populations(populations, iterations)

        messagebox.showinfo("Success", "Simulation completed successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for populations, rates, resources, and iterations.")

def save_report():
    global logs
    if not logs:
        messagebox.showerror("Error", "No simulation data available to save.")
        return

    filename = 'simulation_report.txt'
    report = generate_report(logs)
    with open(filename, 'w') as f:
        f.write(report)
    messagebox.showinfo("Success", f"Report saved as {filename}.")

def export_simulation_logs():
    global logs
    if not logs:
        messagebox.showerror("Error", "No simulation data available to export.")
        return

    filename = 'simulation_logs.json'
    export_logs(logs, filename)
    messagebox.showinfo("Success", f"Logs exported as {filename}.")

def autofill():
    iterations_entry.delete(0, tk.END)
    iterations_entry.insert(0, "8")

    resources_entry.delete(0, tk.END)
    resources_entry.insert(0, "1000")

    species_data = {
        'Rabbits': (800, 0.5, 0.01),
        'Deer': (400, 0.03, 0.03),
        'Eagles': (600, 0.03, 0.03),
        'Wolves': (300, 0.04, 0.01),
        'Bears': (300, 0.04, 0.01),
        'Foxes': (400, 0.059, 0.04),
        'Hawks': (300, 0.06, 0.05)
    }

    for name, (pop, birth_rate, death_rate) in species_data.items():
        for entry in species_entries:
            if entry[0] == name:
                entry[1].delete(0, tk.END)
                entry[1].insert(0, str(pop))
                entry[2].delete(0, tk.END)
                entry[2].insert(0, str(birth_rate))
                entry[3].delete(0, tk.END)
                entry[3].insert(0, str(death_rate))

root = tk.Tk()
root.title("Ecosystem Simulation")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields for simulation parameters
iterations_label = ttk.Label(mainframe, text="Iterations:")
iterations_label.grid(row=0, column=0, sticky=tk.W)
iterations_entry = ttk.Entry(mainframe)
iterations_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

resources_label = ttk.Label(mainframe, text="Resources:")
resources_label.grid(row=1, column=0, sticky=tk.W)
resources_entry = ttk.Entry(mainframe)
resources_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

species_entries = []

def create_species_entry(row, name):
    label = ttk.Label(mainframe, text=f"{name} Population:")
    label.grid(row=row, column=0, sticky=tk.W)
    population_entry = ttk.Entry(mainframe)
    population_entry.grid(row=row, column=1, sticky=(tk.W, tk.E))

    birth_rate_label = ttk.Label(mainframe, text=f"{name} Birth Rate:")
    birth_rate_label.grid(row=row+1, column=0, sticky=tk.W)
    birth_rate_entry = ttk.Entry(mainframe)
    birth_rate_entry.grid(row=row+1, column=1, sticky=(tk.W, tk.E))

    death_rate_label = ttk.Label(mainframe, text=f"{name} Death Rate:")
    death_rate_label.grid(row=row+2, column=0, sticky=tk.W)
    death_rate_entry = ttk.Entry(mainframe)
    death_rate_entry.grid(row=row+2, column=1, sticky=(tk.W, tk.E))

    species_entries.append((name, population_entry, birth_rate_entry, death_rate_entry))
    return population_entry, birth_rate_entry, death_rate_entry

rabbits_population_entry, rabbits_birth_rate_entry, rabbits_death_rate_entry = create_species_entry(2, 'Rabbits')
deer_population_entry, deer_birth_rate_entry, deer_death_rate_entry = create_species_entry(5, 'Deer')
eagles_population_entry, eagles_birth_rate_entry, eagles_death_rate_entry = create_species_entry(8, 'Eagles')
wolves_population_entry, wolves_birth_rate_entry, wolves_death_rate_entry = create_species_entry(11, 'Wolves')
bears_population_entry, bears_birth_rate_entry, bears_death_rate_entry = create_species_entry(14, 'Bears')
foxes_population_entry, foxes_birth_rate_entry, foxes_death_rate_entry = create_species_entry(17, 'Foxes')
hawks_population_entry, hawks_birth_rate_entry, hawks_death_rate_entry = create_species_entry(20, 'Hawks')

# Buttons for starting simulation, saving report, exporting logs, and autofill
start_button = ttk.Button(mainframe, text="Start Simulation", command=start_simulation)
start_button.grid(row=23, column=0, columnspan=2, pady=10)

save_report_button = ttk.Button(mainframe, text="Save Report", command=save_report)
save_report_button.grid(row=24, column=0, columnspan=2, pady=10)

export_logs_button = ttk.Button(mainframe, text="Export Logs", command=export_simulation_logs)
export_logs_button.grid(row=25, column=0, columnspan=2, pady=10)

autofill_button = ttk.Button(mainframe, text="Autofill", command=autofill)
autofill_button.grid(row=26, column=0, columnspan=2, pady=10)

root.mainloop()
