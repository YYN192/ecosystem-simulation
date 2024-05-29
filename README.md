# 🌿 Ecosystem Simulation

This project simulates an ecosystem with various species interacting within a changing environment. Users can customize parameters and visualize the population changes over time.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
  - [Species](#species)
  - [Environment](#environment)
- [User Interface](#user-interface)
- [Example Results](#example-results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or higher
- `matplotlib` for plotting graphs
- `tkinter` for the user interface

pip install matplotlib

Installing

    Clone the repository:

```

git clone https://github.com/YYN192/ecosystem-simulation
cd ecosystem-simulation
```
    Run the simulation:
```
python main.py
```
🎮 Usage

    Enter the number of iterations and initial resources.
    Set the parameters for each species (population, birth rate, death rate).
    Click "Start Simulation" to begin.
    View the simulation report and population graph.
    Save the logs if needed.

🌍 Simulation Details
Species

    Rabbits
    Wolves
    Deer
    Bears
    Eagles

Each species has customizable parameters:

    Population
    Birth Rate
    Death Rate

Environment

    Resources: The initial amount of resources available.
    Conditions: Good or bad, affecting resource updates.
    Seasons: Spring, Summer, Autumn, Winter, affecting species' birth and death rates.
    Disasters: Random events (fire, flood, disease) impacting species populations.

🖥️ User Interface

The UI is built using tkinter and allows users to input parameters, run the simulation, and view results.

📊 Example Results

Simulation Report Example:

Simulation Report
=================
Iteration 1
  Season: Spring
  Resources: 950
  Conditions: Good
  Rabbits Population: 500
  Wolves Population: 100
  Deer Population: 300
  Bears Population: 50
  Eagles Population: 30

🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
🙏 Acknowledgments

    Inspiration and guidance from various online resources and tutorials.
