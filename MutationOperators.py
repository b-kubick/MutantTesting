from Polynomial import Polynomial

# Implementing the mutation operators requires programmatically modifying the source code of the Polynomial class.
class MutationOperators:
    # 1. Coefficient Mutation (This operator changes the coefficients of the polynomial.)
    def coefficient_mutation(polynomial):
        """
        Coefficient Mutation: Increment each coefficient by 1.
        This mutation tests the polynomial's handling of different coefficients.
        """
        mutated_coefficients = [c + 1 for c in polynomial.coefficients]
        return Polynomial(mutated_coefficients)
    
    # 2. Arithmetic Operation Mutation ( This operator switches arithmetic operations.)
    @staticmethod
    def arithmetic_operation_mutation(polynomial):
        """
        Arithmetic Operation Mutation: Invert the addition operation in __add__ method.
        This mutation checks if the tests can detect incorrect arithmetic operations.
        """
        def new_add(self, other):
            # Inverting the addition operation
            return Polynomial([a - b for a, b in zip(self.coefficients, other.coefficients)])

        polynomial.__add__ = new_add.__get__(polynomial, Polynomial)
        return polynomial

    
    # 3. Control Flow Mutation (This operator modifies control flow statements.)
    @staticmethod
    def control_flow_mutation(polynomial):
        """
        Control Flow Mutation: Change the condition in a method, like find_root.
        This mutation assesses the tests' ability to verify control flow logic.
        """
        original_method = polynomial.find_root
        def new_method(a, b, epsilon, max_iterations):
            # Change in the control flow, e.g., using a different epsilon value
            return original_method(a, b, epsilon * 2, max_iterations)

        polynomial.find_root = new_method.__get__(polynomial, Polynomial)
        return polynomial
    
    # 4. Redundant Code Insertion (This operator adds non-functional code.)
    @staticmethod
    def redundant_code_insertion(polynomial):
        """
        Redundant Code Insertion: Add non-functional code, like a no-op loop.
        This mutation tests if the test suite can identify performance issues.
        """
        original_evaluate = polynomial.evaluate
        def new_evaluate(x):
            # Inserting a redundant loop
            for _ in range(1000):
                pass
            return original_evaluate(x)

        polynomial.evaluate = new_evaluate.__get__(polynomial, Polynomial)
        return polynomial
    
    # 5. Boundary Value Mutation (This operator changes boundary values in methods.)
    @staticmethod
    def boundary_value_mutation(polynomial):
        """
        Boundary Value Mutation: Modify the boundary values in a method.
        This mutation checks if the tests handle boundary conditions properly.
        """
        original_method = polynomial.some_boundary_dependent_method
        def new_method(boundary_arg1, boundary_arg2):
            # Altering boundary values
            return original_method(boundary_arg1 + 1, boundary_arg2 - 1)

        polynomial.some_boundary_dependent_method = new_method.__get__(polynomial, Polynomial)
        return polynomial
