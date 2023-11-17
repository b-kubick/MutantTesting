from Polynomial import Polynomial

# Implementing the mutation operators requires programmatically modifying the source code of the Polynomial class.

# 1. Coefficient Mutation (This operator changes the coefficients of the polynomial.)
def coefficient_mutation(polynomial):
    """
    Coefficient Mutation: Increment each coefficient by 1.
    This mutation tests the polynomial's handling of different coefficients.
    """
    mutated_coefficients = [c + 1 for c in polynomial.coefficients]
    return Polynomial(mutated_coefficients)

# 2. Arithmetic Operation Mutation ( This operator switches arithmetic operations.)
def arithmetic_operation_mutation(polynomial):
    """
    Arithmetic Operation Mutation: Invert the addition operation in __add__ method.
    This mutation checks if the tests can detect incorrect arithmetic operations.
    """
    # Directly assign a lambda function to __add__ that inverts the addition operation
    polynomial.__add__ = lambda self, other: Polynomial([a - b for a, b in zip(self.coefficients, other.coefficients)])
    return polynomial


# 3. Control Flow Mutation (This operator modifies control flow statements.)
def control_flow_mutation(polynomial):
    """
    Control Flow Mutation: Change the condition in a method, like find_root.
    This mutation assesses the tests' ability to verify control flow logic.
    """
    original_method = polynomial.find_root_bisection
    # Change in the control flow, e.g., using a different epsilon value
    polynomial.find_root_bisection = lambda a, b, epsilon=1e-6, max_iterations=100: original_method(a, b, epsilon * 2, max_iterations)
    return polynomial

# 4. Redundant Code Insertion (This operator adds non-functional code.)
def redundant_code_insertion(polynomial):
    """
    Redundant Code Insertion: Add non-functional code, like a no-op loop.
    This mutation tests if the test suite can identify performance issues.
    """
    original_evaluate = polynomial.evaluate
    # Inserting a redundant loop
    polynomial.evaluate = lambda x: (sum(1 for _ in range(1000)) or 0) + original_evaluate(x)
    return polynomial

# 5. Boundary Value Mutation (This operator changes boundary values in methods.)
def boundary_value_mutation(polynomial):
    """
    Boundary Value Mutation: Modify the boundary values in a method.
    This mutation checks if the tests handle boundary conditions properly.
    """
    original_method = polynomial.find_root_bisection
    # Altering boundary values
    polynomial.find_root_bisection = lambda a, b, epsilon=1e-6, max_iterations=100: original_method(a + 0.1, b - 0.1, epsilon, max_iterations)
    return polynomial





# Creating an instance of the Polynomial class
original_polynomial = Polynomial([1, 2, 3])  # Example polynomial: x^2 + 2x + 3

# Creating a "copy" by instantiating a new Polynomial with the same coefficients
polynomial_copy = Polynomial(original_polynomial.coefficients.copy())

# Applying mutations
mutant1 = coefficient_mutation(original_polynomial)
mutant2 = arithmetic_operation_mutation(polynomial_copy)

# Displaying the original and mutated polynomials
original_polynomial.coefficients, mutant1.coefficients, mutant2.coefficients
