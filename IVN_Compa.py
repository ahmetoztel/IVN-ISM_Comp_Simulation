import numpy as np
import random
import matplotlib.pyplot as plt

def dice_sorensen_similarity(mat1, mat2):
    intersection = np.sum(np.logical_and(mat1, mat2))  # Ortak eleman sayısı
    total = np.sum(mat1) + np.sum(mat2)  # İki matrisin toplam eleman sayısı
    return (2 * intersection) / total if total != 0 else 0

def ivn_weighted_aggregation():
    replications = int(input("Enter the number of replications: "))
    DSS_A_B, DSS_A_C, DSS_B_C = [], [], []

    linguistic_scales = {
        "Scale_A": {
            0: [ [0.1, 0.2], [0.5, 0.6], [0.7, 0.8] ],
            1: [ [0.2, 0.4], [0.5, 0.6], [0.5, 0.6] ],
            2: [ [0.4, 0.6], [0.4, 0.5], [0.3, 0.4] ],
            3: [ [0.6, 0.8], [0.3, 0.4], [0.2, 0.4] ],
            4: [ [0.7, 0.9], [0.2, 0.3], [0.1, 0.2] ]
        },
        "Scale_B": {
            0: [ [0, 0], [0, 0], [1, 1] ],
            1: [ [0.2, 0.5], [0.1, 0.2], [0.5, 0.75] ],
            2: [ [0.5, 0.5], [0.2, 0.3], [0.5, 0.5] ],
            3: [ [0.5, 0.75], [0.1, 0.2], [0.2, 0.5] ],
            4: [ [0.7, 0.95], [0, 0.1], [0, 0.25] ]
        },
        "Scale_C": {
            0: [ [0.1, 0.2], [0.1, 0.2], [0.7, 0.8] ],
            1: [ [0.2, 0.4], [0.2, 0.3], [0.5, 0.6] ],
            2: [ [0.4, 0.5], [0.2, 0.3], [0.3, 0.4] ],
            3: [ [0.5, 0.6], [0.2, 0.3], [0.2, 0.3] ],
            4: [ [0.7, 0.8], [0.1, 0.2], [0.1, 0.2] ]
        }
    }

    for w in range(replications):
        z = random.randint(5, 20)
        x = random.randint(10, 30)
        w_j = 1 / z  # Equal weights for experts

        IVNCrisp_A = np.zeros((x, x))
        IVNCrisp_B = np.zeros((x, x))
        IVNCrisp_C = np.zeros((x, x))

        for i in range(x):
            for j in range(x):
                if i == j:
                    continue

                expert_vals_A, expert_vals_B, expert_vals_C = [], [], []

                for t in range(z):
                    rand_choice = random.randint(0, 4)
                    expert_vals_A.append(linguistic_scales["Scale_A"][rand_choice])
                    expert_vals_B.append(linguistic_scales["Scale_B"][rand_choice])
                    expert_vals_C.append(linguistic_scales["Scale_C"][rand_choice])

                def compute_ivn_weighted_average(expert_vals, w_j):
                    T_values = [e[0] for e in expert_vals]
                    I_values = [e[1] for e in expert_vals]
                    F_values = [e[2] for e in expert_vals]

                    T_L = 1 - np.prod([(1 - T[0]) ** w_j for T in T_values])
                    T_U = 1 - np.prod([(1 - T[1]) ** w_j for T in T_values])
                    I_L = np.prod([I[0] ** w_j for I in I_values])
                    I_U = np.prod([I[1] ** w_j for I in I_values])
                    F_L = np.prod([F[0] ** w_j for F in F_values])
                    F_U = np.prod([F[1] ** w_j for F in F_values])

                    return (T_L + T_U + (1 - F_L) + (1 - F_U) + (T_L * T_U) + np.sqrt(abs((1 - F_L) * (1 - F_U)))) / 6

                IVNCrisp_A[i, j] = compute_ivn_weighted_average(expert_vals_A, w_j)
                IVNCrisp_B[i, j] = compute_ivn_weighted_average(expert_vals_B, w_j)
                IVNCrisp_C[i, j] = compute_ivn_weighted_average(expert_vals_C, w_j)

        IVNThreshold_A = np.mean(IVNCrisp_A)
        IVNThreshold_B = np.mean(IVNCrisp_B)
        IVNThreshold_C = np.mean(IVNCrisp_C)

        IRM_A = (IVNCrisp_A >= IVNThreshold_A).astype(int)
        IRM_B = (IVNCrisp_B >= IVNThreshold_B).astype(int)
        IRM_C = (IVNCrisp_C >= IVNThreshold_C).astype(int)

        DSS_A_B.append(dice_sorensen_similarity(IRM_A, IRM_B))
        DSS_A_C.append(dice_sorensen_similarity(IRM_A, IRM_C))
        DSS_B_C.append(dice_sorensen_similarity(IRM_B, IRM_C))

    plt.figure(figsize=(12, 4))
    for i, (dss, label) in enumerate(zip([DSS_A_B, DSS_A_C, DSS_B_C], ["A vs B", "A vs C", "B vs C"])):
        plt.subplot(1, 3, i + 1)
        plt.boxplot(dss, vert=True, patch_artist=True, showmeans=True, meanline=True)
        plt.title(f"Comparison: {label}")
        plt.ylabel("Dice-Sørensen Similarity")
    plt.tight_layout()
    plt.show()

    return np.mean(DSS_A_B), np.mean(DSS_A_C), np.mean(DSS_B_C)

# Example usage
mean_A_B, mean_A_C, mean_B_C = ivn_weighted_aggregation()
print(f"Mean DSS (A vs B): {mean_A_B}")
print(f"Mean DSS (A vs C): {mean_A_C}")
print(f"Mean DSS (B vs C): {mean_B_C}")
