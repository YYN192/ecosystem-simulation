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
```
[
    {
        "iteration": 1,
        "season": "summer",
        "conditions": "good",
        "resources": 38048,
        "events": [],
        "Rabbits": 817,
        "Wolves": 370,
        "Deer": 382,
        "Bears": 264,
        "Eagles": 208,
        "Foxes": 351,
        "Hawks": 472
    },
    {
        "iteration": 2,
        "season": "autumn",
        "conditions": "bad",
        "resources": 36099,
        "events": [],
        "Rabbits": 570,
        "Wolves": 352,
        "Deer": 243,
        "Bears": 290,
        "Eagles": 193,
        "Foxes": 253,
        "Hawks": 424
    },
    {
        "iteration": 3,
        "season": "winter",
        "conditions": "good",
        "resources": 34342,
        "events": [],
        "Rabbits": 311,
        "Wolves": 374,
        "Deer": 163,
        "Bears": 330,
        "Eagles": 192,
        "Foxes": 190,
        "Hawks": 397
    },
    {
        "iteration": 4,
        "season": "spring",
        "conditions": "good",
        "resources": 32673,
        "events": [],
        "Rabbits": 314,
        "Wolves": 461,
        "Deer": 117,
        "Bears": 361,
        "Eagles": 189,
        "Foxes": 167,
        "Hawks": 375
    },
    {
        "iteration": 5,
        "season": "summer",
        "conditions": "good",
        "resources": 31087,
        "events": [],
        "Rabbits": 266,
        "Wolves": 411,
        "Deer": 91,
        "Bears": 400,
        "Eagles": 223,
        "Foxes": 159,
        "Hawks": 323
    },
    {
        "iteration": 6,
        "season": "autumn",
        "conditions": "good",
        "resources": 29581,
        "events": [],
        "Rabbits": 185,
        "Wolves": 447,
        "Deer": 69,
        "Bears": 358,
        "Eagles": 204,
        "Foxes": 168,
        "Hawks": 277
    },
    {
        "iteration": 7,
        "season": "winter",
        "conditions": "bad",
        "resources": 28055,
        "events": [],
        "Rabbits": 126,
        "Wolves": 373,
        "Deer": 77,
        "Bears": 357,
        "Eagles": 199,
        "Foxes": 114,
        "Hawks": 246
    },
    {
        "iteration": 8,
        "season": "spring",
        "conditions": "good",
        "resources": 26700,
        "events": [],
        "Rabbits": 110,
        "Wolves": 320,
        "Deer": 54,
        "Bears": 253,
        "Eagles": 181,
        "Foxes": 85,
        "Hawks": 214
    }
]
```
Every iteration is a season meaning this program will simulate 2 years

![github](https://github.com/YYN192/ecosystem-simulation/assets/110526560/3bddb25a-c0e7-48f3-bdc7-2d56f36d3fd5)

🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
🙏 Acknowledgments

    Inspiration and guidance from various online resources and tutorials.
