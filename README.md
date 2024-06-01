# 🌿 Ecosystem Simulation 🌿

This project simulates an ecosystem with various species interacting with each other and their environment over a series of iterations. The simulation accounts for seasonal changes, disasters, events, and resource availability.

## 🌟 Features

- **Species Interactions**: 🦅 Predation, 🐺 competition, and 🤝 symbiosis between species. More sophisticated interaction rules like mutualism, commensalism, and competition models.
- **Environmental Factors**: 🌞 Seasonal changes, 🌱 resource depletion, and 🎲 random events such as disasters and special occurrences. Dynamic environment conditions based on various factors like overpopulation and resource depletion.
- **Dynamic Population Changes**: Species populations adjust based on birth and death rates, influenced by the environment. Includes behaviors like migration or hibernation for specific species.
- **Resource Management**: Detailed model for resource management where different species compete for specific types of resources (e.g., water, food, shelter).
- **User Interface**: Input validation, enhanced visualization with Plotly, and user controls for dynamic adjustments.
- **Performance and Scalability**: Optimized performance for larger simulations using numpy for numerical computations. Feature to save and load simulation states.
- **Documentation and Testing**: Comprehensive docstrings for classes and methods, user manual, and unit and integration tests.
- **Additional Features**: Integration of real-world data, predefined scenarios, and advanced analytics for insights into simulation results.

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
3. Enter the initial population and birth/death rates for each species, or use the "Autofill" button to populate these values with defaults.
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
  - **Save Report**: Saves the simulation report to a file.
  - **Export Logs**: Saves the simulation logs to a JSON file.
  - **Autofill**: Fills the birth rates, death rates, and populations with predefined values and sets iterations to 8.

## 🌼 Example

1. Input the simulation parameters.
2. Click "Start Simulation".
3. Review the simulation report and population plots displayed.
4. Optionally, save the logs by entering a filename and clicking "Save Logs".

![Simulation Screenshot](https://github.com/YYN192/ecosystem-simulation/assets/110526560/3db6c967-ea2c-4dc6-a50a-ad759eef9fa7)

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
- `save_report`: Saves the simulation report to a specified file.
- `export_simulation_logs`: Saves the simulation logs to a specified file.
- `autofill`: Fills the birth rates, death rates, and populations with predefined values and sets iterations to 8.

## 🤝 Contribution

We welcome contributions to this project! If you're interested in contributing, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to get started.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
