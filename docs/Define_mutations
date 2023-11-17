# Mutation Operators for Polynomial Class

## Coefficient Mutation
- **Description**: Alters the coefficients of the polynomial. Changes may include incrementing, decrementing, or setting coefficients to zero.
- **Purpose**: To test if the polynomial's evaluation, arithmetic operations, and root-finding methods correctly handle varied coefficients.
- **Implementation Suggestion**: Modify each coefficient in a loop, applying different changes (e.g., `coef += 1`, `coef -= 1`, `coef = 0`).

## Arithmetic Operation Mutation
- **Description**: Switches arithmetic operations in methods like `__add__`, `__sub__`, and `__mul__`. For example, swapping addition with subtraction in the `__add__` method.
- **Purpose**: To check if the test suite can detect incorrect results due to altered arithmetic logic.
- **Implementation Suggestion**: In the `__add__` method, replace `+` with `-` and vice versa. In the `__mul__` method, try implementing incorrect multiplication logic.

## Control Flow Mutation
- **Description**: Modifies control flow statements, such as conditions in loops or if-else constructs. For example, changing the condition in the root-finding method.
- **Purpose**: To assess whether the tests verify the correct flow of logic in the algorithms.
- **Implementation Suggestion**: In the bisection method, alter the convergence condition or the condition that checks if the interval contains a root.

## Redundant Code Insertion
- **Description**: Introduces redundant or non-functional code that doesn't change the core functionality.
- **Purpose**: To test whether the suite can identify performance issues or unnecessary code blocks.
- **Implementation Suggestion**: Add no-op loops or redundant calculations that don’t affect the output but may affect performance.

## Boundary Value Mutation
- **Description**: Modifies the boundary values used in methods, especially in the root-finding method.
- **Purpose**: To test if the boundary conditions are properly handled in the algorithms.
- **Implementation Suggestion**: Alter the initial values or the epsilon value in the bisection method.

Each of these mutation operators should be implemented as a method in your `MutationOperators.py` module. These methods will programmatically alter the source code of the Polynomial class to create mutant versions. The effectiveness of your test suite is then evaluated based on its ability to detect these mutations.

