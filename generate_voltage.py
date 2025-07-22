import numpy as np

def generate_gate_voltages(n_samples=1000, seed=42):
    np.random.seed(seed)
    return np.random.uniform(-1, 1, size=(n_samples, 3))

def assign_dot_states(X):
    Y = []
    for v in X:
        if v[0] + v[1] > 0.5:
            Y.append(2)  # double dot
        elif v[0] > 0.3:
            Y.append(1)  # single dot
        else:
            Y.append(0)  # no dot
    return np.array(Y)

def add_noise(X, noise_level=0.05):
    return X + np.random.normal(0, noise_level, X.shape)

X_raw = generate_gate_voltages()
Y = assign_dot_states(X_raw)
X_noisy = add_noise(X_raw)