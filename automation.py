import subprocess
from itertools import product
import os

# Make sure the results folder exists
os.makedirs("results", exist_ok=True)

# Define parameter ranges
T_max_vals = [100]  # Example value; adjust as needed
n_vals = [50, 100]
k_vals = [5, 10]
p_vals = [0.05, 0.1]
weighted_vals = [0, 1]
negative_weight_vals = [0, 1]
saved_graph_choice = ['n']
save_my_graph_choice = ['n']
kernel_vals = [0.0, 1.0]

# Generate all combinations (you can slice to limit number of runs)
combinations = list(product(
    T_max_vals,
    n_vals,
    k_vals,
    p_vals,
    weighted_vals,
    negative_weight_vals,
    saved_graph_choice,
    save_my_graph_choice,
    kernel_vals
))

combinations = combinations[:160]  # Limit to 160 runs

# Loop through each parameter set
for idx, (T_max, n, k, p, w, w_neg, load, save, kernel) in enumerate(combinations):
    print(f"\n▶ Running simulation {idx+1}/{len(combinations)}")
    print(f"   Parameters: T={T_max}, n={n}, k={k}, p={p}, weighted={w}, negative={w_neg}, kernel={kernel}")

    # Construct the simulated CLI input as string
    input_str = f"{T_max}\n{n}\n{k}\n{p}\n{w}\n"
    if w == 1:
        input_str += f"{w_neg}\n"
    input_str += f"{load}\n{save}\n{kernel}\n"

    # Generate a filename prefix for saving figures
    prefix = f"echo_n{n}_k{k}_p{p}_w{w}_neg{w_neg}_ker{kernel}".replace('.', '_')
    env = os.environ.copy()
    env["FILENAME_PREFIX"] = prefix  # Pass it to simulate.py using env var

    # Run the simulation and capture outputs
    result = subprocess.run(
        ["python", "simulate.py"],
        input=input_str,
        text=True,
        capture_output=True,
        env=env
    )

    # Log output
    log_path = f"results/{prefix}_log.txt"
    with open(log_path, "w") as f:
        f.write(result.stdout)
        f.write("\n\nSTDERR:\n")
        f.write(result.stderr)

    print(f"   ✅ Output logged to {log_path}")
