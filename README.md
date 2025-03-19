# ERIVN-ISM Simulation

This repository contains a Python-based simulation for **Empirical Rule Interval-Valued Neutrosophic Interpretive Structural Modelling (ERIVN-ISM)**. The ERIVN-ISM method enhances traditional **IVN-ISM** by applying the **Empirical Rule** to expert opinions, ensuring a more statistically grounded approach to decision modeling under uncertainty.

## 📌 Overview
ERIVN-ISM is a novel extension of **Interpretive Structural Modeling (ISM)** that utilizes **Interval-Valued Neutrosophic Numbers (IVNNs)** derived from expert opinions. Instead of relying on predefined IVN linguistic scales, ERIVN-ISM employs the **Empirical Rule (mean ± standard deviation)** to construct objective and data-driven intervals. This method provides:
- **More reliable expert judgment aggregation**
- **Reduced subjectivity in IVN number assignment**
- **Greater robustness in decision modeling**

## 🏗 Project Structure
```
📂 ERIVN-ISM-Simulation
 ├── 📄 main.py              # Main script for running the simulation
 ├── 📄 README.md            # Documentation (this file)
 ├── 📄 requirements.txt      # List of dependencies
 ├── 📂 data                 # Directory for input/output files (if applicable)
 ├── 📂 results              # Stores generated simulation outputs
 ├── 📄 LICENSE              # License information
```

## ⚙️ Installation & Setup
To run the simulation on your local machine, follow these steps:

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/ERIVN-ISM-Simulation.git
cd ERIVN-ISM-Simulation
```

### 2️⃣ Create a virtual environment (optional but recommended)
```sh
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate   # On Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Running the Simulation
Execute the **main script** to perform IVN-ISM and ERIVN-ISM comparisons:
```sh
python main.py
```
During execution, the script will:
- Generate expert judgments using different IVN linguistic scales.
- Apply **Empirical Rule** to construct IVNNs.
- Compute decision matrices and threshold-based **Reachability Matrices (IRM)**.
- Compare structural consistency using **Dice-Sørensen Similarity (DSS)**.
- Generate and visualize results in **boxplot format**.

## 📊 Simulation Results
The simulation evaluates the impact of different IVN linguistic scales by comparing:
1. **Traditional IVN-ISM vs. ERIVN-ISM**
2. **Different linguistic scales used in IVN number assignments**
3. **Structural similarity using Dice-Sørensen Similarity (DSS)**

The results demonstrate that **ERIVN-ISM** provides **more reliable and stable outputs** compared to traditional IVN-ISM, which is sensitive to scale selection.

### Example Output
![Simulation Results](results/comparison_boxplots.png)

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing
Contributions are welcome! If you would like to improve the simulation or propose modifications:
1. **Fork** the repository
2. **Create** a new branch (`feature/new-feature`)
3. **Commit** your changes
4. **Submit** a pull request

## 📩 Contact
For any questions or discussions, feel free to **open an issue** or contact me via:
📧 Email: your.email@example.com  
🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)

---

Happy coding! 🚀

