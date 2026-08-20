# Computational Lineal Algebra for a Dehydration-Unit
## Description
This script solves steady-state mass balance problems for a multicomponent separation process (modeled around a Glycol Dehydration Unit). It utilizes computational linear algebra to resolve systems of simultaneous equations, determining the unknown mass flow rates of output streams based on known input flows and component mass fractions.

## Objective
To algorithmically solve $A \cdot X = B$ matrix equations for chemical engineering mass balances, ensuring system solvability and high-precision numerical outputs.

## Technical Stack
*   **Language:** Python 3.x
*   **Libraries:** `numpy` (`numpy.linalg.solve`, `numpy.linalg.det`).

## Methodology
1.  **Matrix Construction & Transposition:** Ingests field composition data and transposes the matrix to align components along rows and streams along columns to satisfy algebraic constraints.
2.  **Singularity Check:** Calculates the matrix determinant ($|A|$) prior to execution to prevent mathematical errors from linearly dependent process streams.
3.  **Numerical Resolution:** Applies exact linear algebra solvers to deduce the mass flow vector ($X$).
4.  **Sanity Check:** Re-multiplies the solved vector with the coefficient matrix to verify zero-error balance closure.

## Results
The algorithm successfully resolved the component matrix, returning the precise mass flow rates (kg/h) for the Dry Gas, Sour Water, Rich Glycol, and Tail Gas streams.
