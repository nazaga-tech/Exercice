

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, minimize

# ─────────────────────────────────────────────
# Fonctions objectifs
# ─────────────────────────────────────────────
def f1(x):
    return x ** 2

def f2(x):
    return (x - 5) ** 2


def methode_scalarisation(poids_liste):
    """
    Minimise  f(x) = w1*f1(x) + w2*f2(x)
    pour chaque couple de poids (w1, w2).
    """
    print("\n" + "=" * 60)
    print("MÉTHODE 1 — SCALARISATION (somme pondérée)")
    print("=" * 60)

    resultats = []
    for w1, w2 in poids_liste:
        def f_scalaire(x):
            return w1 * f1(x) + w2 * f2(x)

        res = minimize_scalar(f_scalaire, bounds=(0, 10), method="bounded")
        x_opt = res.x
        resultats.append((w1, w2, x_opt, f1(x_opt), f2(x_opt)))
        print(f"  w1={w1:.1f}, w2={w2:.1f}  →  x*={x_opt:.4f}"
              f"   f1={f1(x_opt):.4f}   f2={f2(x_opt):.4f}")

    return resultats


