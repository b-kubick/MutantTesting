import pytest

# Import the mutation functions and the Polynomial class
from Polynomial import Polynomial
from MutationOperators import (
    coefficient_mutation,
    arithmetic_operation_mutation,
    control_flow_mutation,
    redundant_code_insertion,
    boundary_value_mutation
)

# Test the coefficient mutation
def test_coefficient_mutation():
    poly = Polynomial([1, 2, 3])  # 1x^2 + 2x + 3
    mutated_poly = coefficient_mutation(poly)
    assert mutated_poly.coefficients == [2, 3, 4], "Coefficient mutation did not work as expected."

# Test the arithmetic operation mutation
def test_arithmetic_operation_mutation():
    poly = Polynomial([1, 2, 3])  # 1x^2 + 2x + 3
    other = Polynomial([3, 2, 1])  # 3x^2 + 2x + 1
    mutated_poly = arithmetic_operation_mutation(poly)
    result = mutated_poly + other
    assert result.coefficients == [-2, 0, 4], "Arithmetic operation mutation did not work as expected."

# Test the control flow mutation
def test_control_flow_mutation():
    poly = Polynomial([1, -1])  # x - 1
    mutated_poly = control_flow_mutation(poly)
    # You need a test that checks the modified behavior of the mutated method
    # This might involve checking for a root with the new epsilon value
    # For example:
    root = mutated_poly.find_root_bisection(0, 2)
    assert abs(poly.evaluate(root)) < 1e-6 * 2, "Control flow mutation did not work as expected."

# Test the redundant code insertion
def test_redundant_code_insertion():
    poly = Polynomial([1, 2, 3])
    mutated_poly = redundant_code_insertion(poly)
    # You might test the performance or simply that the method still computes correctly
    result = mutated_poly.evaluate(2)
    assert result == poly.evaluate(2), "Redundant code insertion did not work as expected."

# Test the boundary value mutation
def test_boundary_value_mutation():
    poly = Polynomial([1, 0, -2])  # x^2 - 2
    mutated_poly = boundary_value_mutation(poly)
    # Similar to the control flow test, this should check the modified behavior
    root = mutated_poly.find_root_bisection(0, 2)
    assert root > 0.1 and root < 1.9, "Boundary value mutation did not work as expected."

# Run the tests
if __name__ == "__main__":
    pytest.main()
