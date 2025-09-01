# Fully Autonomous Urban Traffic Management System

## Overview
The **Traffic Management System (TMS)** is an autonomous simulation framework for **urban traffic optimization**.  
It integrates **machine learning, graph theory, and heuristic rules** to manage intersections, optimize traffic light timings, predict congestion, and reroute vehicles dynamically.

This project demonstrates how AI-powered systems can be applied to **smart city infrastructure** to reduce congestion and improve traffic flow in real time.

---

## Features
- **Urban Road Network Simulation**  
  - Generates a grid-based network of intersections using **NetworkX**.
- **Traffic Data Collection**  
  - Simulates IoT-based sensors for vehicle flow and accident reports.
- **Traffic Light Optimization**  
  - Adjusts light durations dynamically based on real-time flow and accidents.
- **Machine Learning Congestion Prediction**  
  - Uses a **Random Forest Regressor** to estimate future congestion levels.
- **Dynamic Rerouting**  
  - Applies **shortest path algorithms** to reroute traffic around congested intersections.
- **Scalable Framework**  
  - Can be extended with real-world IoT, traffic cameras, and connected vehicle data.

---

## Installation

### Requirements
- Python 3.8+
- NumPy
- Scikit-learn
- NetworkX

### Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/traffic-management-system.git
cd traffic-management-system
pip install -r requirements.txt
```

`requirements.txt` should include:
```
numpy
scikit-learn
networkx
```

---

## Usage

### Running the Simulation
Execute the main script:
```bash
python traffic_management_system.py
```

### Example Output
```
Collected traffic data: {
 (0, 0): {'traffic_flow': 450, 'accidents': 0},
 (0, 1): {'traffic_flow': 220, 'accidents': 1},
 ...
}

Optimized traffic light durations: {
 (0, 0): {'traffic_flow': 450, 'accidents': 0, 'optimized_light_duration': 60},
 (0, 1): {'traffic_flow': 220, 'accidents': 1, 'optimized_light_duration': 0},
 ...
}

Predicted congestion scores: {
 (0, 0): 402.15,
 (0, 1): 190.73,
 ...
}

Rerouted paths for high-congestion areas: {
 (0, 0): { ... shortest path reroutes ... }
}
```

---

## Project Structure
```
traffic_management_system.py   # Core implementation
requirements.txt               # Dependencies
README.md                      # Documentation
```

---

## Roadmap
- [ ] Integrate **real-time IoT traffic sensor APIs**.  
- [ ] Extend routing with **reinforcement learning**.  
- [ ] Add visualization of traffic flows and congestion hotspots.  
- [ ] Deploy as a **Flask/FastAPI microservice** for smart city dashboards.  

