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

[
    {
        "iteration": 1,
        "season": "summer",
        "conditions": "good",
        "resources": 998,
        "events": [],
        "Rabbits": 87,
        "Wolves": 54,
        "Deer": 68,
        "Bears": 27,
        "Eagles": 37
    },
    {
        "iteration": 2,
        "season": "autumn",
        "conditions": "bad",
        "resources": 901,
        "events": [],
        "Rabbits": 66,
        "Wolves": 57,
        "Deer": 53,
        "Bears": 32,
        "Eagles": 46
    },
    {
        "iteration": 3,
        "season": "winter",
        "conditions": "good",
        "resources": 904,
        "events": [
            "Disaster occurred: disease"
        ],
        "Rabbits": 37,
        "Wolves": 40,
        "Deer": 31,
        "Bears": 23,
        "Eagles": 37
    },
    {
        "iteration": 4,
        "season": "spring",
        "conditions": "bad",
        "resources": 812,
        "events": [],
        "Rabbits": 30,
        "Wolves": 37,
        "Deer": 27,
        "Bears": 23,
        "Eagles": 38
    },
    {
        "iteration": 5,
        "season": "summer",
        "conditions": "bad",
        "resources": 724,
        "events": [],
        "Rabbits": 23,
        "Wolves": 38,
        "Deer": 21,
        "Bears": 21,
        "Eagles": 38
    },
    {
        "iteration": 6,
        "season": "autumn",
        "conditions": "good",
        "resources": 736,
        "events": [],
        "Rabbits": 18,
        "Wolves": 36,
        "Deer": 19,
        "Bears": 19,
        "Eagles": 36
    },
    {
        "iteration": 7,
        "season": "winter",
        "conditions": "bad",
        "resources": 652,
        "events": [],
        "Rabbits": 15,
        "Wolves": 35,
        "Deer": 17,
        "Bears": 19,
        "Eagles": 34
    },
    {
        "iteration": 8,
        "season": "spring",
        "conditions": "good",
        "resources": 667,
        "events": [],
        "Rabbits": 14,
        "Wolves": 33,
        "Deer": 17,
        "Bears": 19,
        "Eagles": 34
    },
    {
        "iteration": 9,
        "season": "summer",
        "conditions": "bad",
        "resources": 587,
        "events": [],
        "Rabbits": 13,
        "Wolves": 33,
        "Deer": 17,
        "Bears": 19,
        "Eagles": 30
    },
    {
        "iteration": 10,
        "season": "autumn",
        "conditions": "bad",
        "resources": 511,
        "events": [],
        "Rabbits": 12,
        "Wolves": 30,
        "Deer": 17,
        "Bears": 19,
        "Eagles": 30
    },
    {
        "iteration": 11,
        "season": "winter",
        "conditions": "bad",
        "resources": 438,
        "events": [
            "Disaster occurred: flood"
        ],
        "Rabbits": 9,
        "Wolves": 25,
        "Deer": 13,
        "Bears": 16,
        "Eagles": 23
    },
    {
        "iteration": 12,
        "season": "spring",
        "conditions": "bad",
        "resources": 369,
        "events": [
            "Disaster occurred: disease"
        ],
        "Rabbits": 6,
        "Wolves": 19,
        "Deer": 10,
        "Bears": 12,
        "Eagles": 18
    },
    {
        "iteration": 13,
        "season": "summer",
        "conditions": "good",
        "resources": 399,
        "events": [
            "Disaster occurred: fire"
        ],
        "Rabbits": 5,
        "Wolves": 17,
        "Deer": 9,
        "Bears": 10,
        "Eagles": 16
    },
    {
        "iteration": 14,
        "season": "autumn",
        "conditions": "good",
        "resources": 427,
        "events": [],
        "Rabbits": 5,
        "Wolves": 17,
        "Deer": 9,
        "Bears": 10,
        "Eagles": 16
    },
    {
        "iteration": 15,
        "season": "winter",
        "conditions": "bad",
        "resources": 359,
        "events": [
            "Disaster occurred: fire"
        ],
        "Rabbits": 4,
        "Wolves": 15,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 16,
        "season": "spring",
        "conditions": "bad",
        "resources": 294,
        "events": [],
        "Rabbits": 4,
        "Wolves": 16,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 17,
        "season": "summer",
        "conditions": "bad",
        "resources": 232,
        "events": [],
        "Rabbits": 4,
        "Wolves": 16,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 18,
        "season": "autumn",
        "conditions": "good",
        "resources": 268,
        "events": [],
        "Rabbits": 4,
        "Wolves": 16,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 19,
        "season": "winter",
        "conditions": "bad",
        "resources": 208,
        "events": [],
        "Rabbits": 4,
        "Wolves": 16,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 20,
        "season": "spring",
        "conditions": "good",
        "resources": 246,
        "events": [],
        "Rabbits": 4,
        "Wolves": 17,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 21,
        "season": "summer",
        "conditions": "good",
        "resources": 282,
        "events": [],
        "Rabbits": 4,
        "Wolves": 17,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 22,
        "season": "autumn",
        "conditions": "good",
        "resources": 316,
        "events": [],
        "Rabbits": 4,
        "Wolves": 17,
        "Deer": 8,
        "Bears": 9,
        "Eagles": 14
    },
    {
        "iteration": 23,
        "season": "winter",
        "conditions": "bad",
        "resources": 253,
        "events": [
            "Disaster occurred: disease"
        ],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 24,
        "season": "spring",
        "conditions": "good",
        "resources": 288,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 25,
        "season": "summer",
        "conditions": "bad",
        "resources": 227,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 26,
        "season": "autumn",
        "conditions": "bad",
        "resources": 169,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 27,
        "season": "winter",
        "conditions": "bad",
        "resources": 114,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 28,
        "season": "spring",
        "conditions": "good",
        "resources": 156,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 29,
        "season": "summer",
        "conditions": "bad",
        "resources": 101,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 30,
        "season": "autumn",
        "conditions": "bad",
        "resources": 49,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 31,
        "season": "winter",
        "conditions": "good",
        "resources": 95,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 32,
        "season": "spring",
        "conditions": "bad",
        "resources": 43,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 33,
        "season": "summer",
        "conditions": "good",
        "resources": 89,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 34,
        "season": "autumn",
        "conditions": "bad",
        "resources": 38,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 35,
        "season": "winter",
        "conditions": "good",
        "resources": 84,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 36,
        "season": "spring",
        "conditions": "good",
        "resources": 128,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 37,
        "season": "summer",
        "conditions": "bad",
        "resources": 75,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 38,
        "season": "autumn",
        "conditions": "bad",
        "resources": 24,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 39,
        "season": "winter",
        "conditions": "good",
        "resources": 71,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 40,
        "season": "spring",
        "conditions": "good",
        "resources": 115,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 41,
        "season": "summer",
        "conditions": "bad",
        "resources": 62,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 42,
        "season": "autumn",
        "conditions": "bad",
        "resources": 12,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 43,
        "season": "winter",
        "conditions": "bad",
        "resources": 0,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 44,
        "season": "spring",
        "conditions": "bad",
        "resources": 0,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 45,
        "season": "summer",
        "conditions": "bad",
        "resources": 0,
        "events": [],
        "Rabbits": 3,
        "Wolves": 13,
        "Deer": 6,
        "Bears": 7,
        "Eagles": 11
    },
    {
        "iteration": 46,
        "season": "autumn",
        "conditions": "bad",
        "resources": 0,
        "events": [
            "Disaster occurred: flood"
        ],
        "Rabbits": 2,
        "Wolves": 11,
        "Deer": 5,
        "Bears": 5,
        "Eagles": 9
    },
    {
        "iteration": 47,
        "season": "winter",
        "conditions": "bad",
        "resources": 0,
        "events": [
            "Disaster occurred: disease"
        ],
        "Rabbits": 1,
        "Wolves": 8,
        "Deer": 4,
        "Bears": 4,
        "Eagles": 7
    },
    {
        "iteration": 48,
        "season": "spring",
        "conditions": "bad",
        "resources": 0,
        "events": [],
        "Rabbits": 1,
        "Wolves": 8,
        "Deer": 4,
        "Bears": 4,
        "Eagles": 7
    },
    {
        "iteration": 49,
        "season": "summer",
        "conditions": "good",
        "resources": 48,
        "events": [],
        "Rabbits": 1,
        "Wolves": 8,
        "Deer": 4,
        "Bears": 4,
        "Eagles": 7
    },
    {
        "iteration": 50,
        "season": "autumn",
        "conditions": "good",
        "resources": 94,
        "events": [],
        "Rabbits": 1,
        "Wolves": 8,
        "Deer": 4,
        "Bears": 4,
        "Eagles": 7
    }
]

Every iteration is a season meaning this program will simulate 2 years
![github](https://github.com/YYN192/ecosystem-simulation/assets/110526560/3bddb25a-c0e7-48f3-bdc7-2d56f36d3fd5)

🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
🙏 Acknowledgments

    Inspiration and guidance from various online resources and tutorials.
