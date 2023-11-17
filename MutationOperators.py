# Implementing the mutation operators requires programmatically modifying the source code of the Polynomial class.

# 1. Coefficient Mutation (This operator changes the coefficients of the polynomial.)


def coefficient_mutation(polynomial):
    mutated_polynomial = polynomial.copy()
    for i in range(len(mutated_polynomial.coefficients)):
        # Example mutation: increment each coefficient by 1
        mutated_polynomial.coefficients[i] += 1
    return mutated_polynomial

# 2. Arithmetic Operation Mutation ( This operator switches arithmetic operations.)
def arithmetic_operation_mutation(polynomial):
    mutated_polynomial = polynomial.copy()

    # Example mutation: switch addition and subtraction in __add__ method
    def new_add(self, other):
        # Incorrect implementation as an example
        return Polynomial([a - b for a, b in zip(self.coefficients, other.coefficients)])
    
    mutated_polynomial.__add__ = new_add.__get__(mutated_polynomial)
    return mutated_polynomial

# 3. Control Flow Mutation (This operator modifies control flow statements.)
def control_flow_mutation(polynomial):
    mutated_polynomial = polynomial.copy()

    # Example mutation: change the convergence condition in the root-finding method
    original_method = polynomial.find_root_bisection
    def new_method(self, a, b, epsilon, max_iterations):
        # Example: change the convergence condition
        return original_method(self, a, b, epsilon / 2, max_iterations)
    
    mutated_polynomial.find_root_bisection = new_method.__get__(mutated_polynomial)
    return mutated_polynomial

# 4. Redundant Code Insertion (This operator adds non-functional code.)
def redundant_code_insertion(polynomial):
    mutated_polynomial = polynomial.copy()

    # Example mutation: add a no-op loop in the evaluate method
    original_method = polynomial.evaluate
    def new_method(self, x):
        for _ in range(1000):  # No-op loop
            pass
        return original_method(self, x)
    
    mutated_polynomial.evaluate = new_method.__get__(mutated_polynomial)
    return mutated_polynomial

# 5. Boundary Value Mutation (This operator changes boundary values in methods.)
def boundary_value_mutation(polynomial):
    mutated_polynomial = polynomial.copy()

    # Example mutation: change the initial values in the root-finding method
    original_method = polynomial.find_root_bisection
    def new_method(self, a, b, epsilon, max_iterations):
        # Change initial interval slightly
        return original_method(self, a + 0.1, b - 0.1, epsilon, max_iterations)
    
    mutated_polynomial.find_root_bisection = new_method.__get__(mutated_polynomial)
    return mutated_polynomial
