# 🌿 Ecosystem Simulation 🌿

This project simulates an ecosystem with various species interacting with each other and their environment over a series of iterations. The simulation accounts for seasonal changes, disasters, events, and resource availability.

## 🌟 Features

- **Species Interactions**: 🦅 Predation, 🐺 competition, and 🤝 symbiosis between species.
- **Environmental Factors**: 🌞 Seasonal changes, 🌱 resource depletion, and 🎲 random events such as disasters and special occurrences.
- **Dynamic Population Changes**: Species populations adjust based on birth and death rates, influenced by the environment.

## 🐾 Species Included

- 🐰 Rabbits
- 🐺 Wolves
- 🦌 Deer
- 🐻 Bears
- 🦅 Eagles
- 🦊 Foxes
- 🦅 Hawks

## ⚙️ Installation

1. Ensure you have Python installed.
2. Install the required packages:
    ```sh
    pip install tkinter matplotlib
    ```

## 🚀 Usage

1. Run the script to start the simulation interface:
    ```sh
    python ecosystem_simulation.py
    ```
2. Enter the number of iterations and initial resource quantity.
3. Enter the initial population and birth/death rates for each species.
4. Click "Start Simulation" to run the simulation.
5. View the simulation report and population plots.
6. Optionally, save the simulation logs to a file.

## 📊 Simulation Parameters

- **Iterations**: Number of cycles the simulation will run.
- **Resources**: Initial amount of resources available in the environment.
- **Species Parameters**:
  - **Population**: Initial number of individuals in the species.
  - **Birth Rate**: Base rate at which the species reproduces.
  - **Death Rate**: Base rate at which individuals in the species die.

## 🖥️ GUI Interface

The simulation provides a graphical user interface (GUI) built with `tkinter`. The interface allows users to input the simulation parameters and view results.

### Main Interface Elements

- **Iterations**: Number of iterations to run the simulation.
- **Resources**: Initial resources in the environment.
- **Species Parameters**: Fields for inputting population, birth rate, and death rate for each species.
- **Buttons**:
  - **Start Simulation**: Runs the simulation with the provided parameters.
  - **Save Logs**: Saves the simulation logs to a specified file.

## 🌼 Example

1. Input the simulation parameters.
2. Click "Start Simulation".
3. Review the simulation report and population plots displayed.
4. Optionally, save the logs by entering a filename and clicking "Save Logs".

![github](https://github.com/YYN192/ecosystem-simulation/assets/110526560/3db6c967-ea2c-4dc6-a50a-ad759eef9fa7)

## 📝 Code Overview

### `Species` Class

Represents a species with attributes like name, population, birth rate, and death rate. It includes methods for adjusting rates based on the season, reproducing, dying, and interacting with other species.

### `Environment` Class

Represents the environment with resources, conditions, and the current season. It includes methods for changing conditions, updating resources, changing seasons, and causing disasters or special events.

### Simulation Functions

- `run_simulation`: Runs the simulation for a specified number of iterations.
- `generate_report`: Generates a textual report of the simulation.
- `plot_populations`: Plots the populations of each species over time.
- `export_logs`: Exports the simulation logs to a JSON file.

### GUI Functions

- `start_simulation`: Starts the simulation and displays the results.
- `save_logs`: Saves the simulation logs to a specified file.

## 🤝 Contribution

We welcome contributions to this project! If you're interested in contributing, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to get started.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
