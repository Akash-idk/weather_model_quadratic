# weather_model_quadratic
An project on Software Engineering 


# 🌦 Weather Modeling using Quadratic Equation & SDLC Models

This project demonstrates **Software Engineering models (Waterfall, Iterative, Agile)** through a simple **weather prediction system**.  
The prediction is based on a quadratic equation:

\[
T(t) = a \cdot t^2 + b \cdot t + c
\]

where:
- `a`, `b`, `c` → coefficients (assumed from environmental data)
- `t` → time (in hours or days)
- `T` → predicted temperature (°C)

---

## 📂 Project Structure

Weathermodel_SE/
│── version1_hardcoded.py          # Hard-coded values
│── version2_keyboard_input.py     # Keyboard input
│── version3_file_input_single.py  # Single set from file
│── version4_file_input_multiple.py# Multiple sets from file
│── models.py                      # Waterfall, Iterative, Agile modes + plots
│── inputs_single.txt              # Example: single input set
│── inputs_multiple.txt            # Example: multiple input sets
│── README.md                      # Documentation
│── requirements.txt               # Dependencies


---

## 🚀 Features
- **Stage-wise Development**
  1. Hardcoded values
  2. User keyboard input
  3. File input (single set)
  4. File input (multiple sets)
- **Software Models Simulation**
  - Waterfall → One full cycle
  - Iterative → Multiple partial cycles
  - Agile → Quick sprints with frequent feedback
- **Visualization with Matplotlib**
  - Graphs for Waterfall, Iterative, Agile approaches

---

## ⚙️ Installation

1. Clone this repository or download the files.  
2. (Recommended) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
