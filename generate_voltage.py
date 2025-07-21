import numpy as np

def generate_gate_voltages(n_samples=1000, seed=42):
    np.random.seed(seed)
    return np.random.uniform(-1, 1, size=(n_samples, 3))
