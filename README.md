# Mutation Testing for Polynomial Class

## Set up the Environment

- **Access Requirements**: Ensure access to the `Polynomial` class, your unit tests, and the `pytest` testing framework.

## Define Mutation Operators

- **Operator Identification**: Identify and define specific mutation operators for the `Polynomial` class.
- **Documentation**: Each operator should be well-documented.
- **Examples**: Operators may include changing coefficients, modifying arithmetic operations, introducing redundant code, etc.

## Implement Mutation Operators

- **Implementation**: Implement the mutation operators as methods in a separate Python module or script.
- **Modification Method**: These methods should modify the `Polynomial` class source code according to the defined mutation operators.
- **Examples and Usage**: Provide clear examples of how these operators should be applied.

## Apply Mutations

- **Mutation Application**: Apply the defined mutation operators to the `Polynomial` class to create mutant versions.
- **Mutant Variants**: Create multiple mutants, each representing a different mutation.

## Run Tests on Mutants

- **Testing**: Run your unit tests on each mutant version of the `Polynomial` class.
- **Outcomes**: Determine whether the mutants survive (test cases fail to detect the mutation) or are killed (test cases identify the mutation).

## Analyze Results

- **Results Analysis**: Analyze the results of the mutation testing.
- **Survival and Killing**: Identify which mutants survived and which were killed.
- **Mutation Classification**: Classify mutations into categories based on impact (e.g., harmless, equivalent, serious).

## Improve the Test Suite

- **Test Suite Revision**: Revise your test suite based on the mutation testing results.
- **Enhancing Coverage**: Add new test cases or modify existing ones to improve test coverage.

## Write a Report

- **Report Content**: Write a comprehensive report summarizing the mutation testing process.
  - Introduction
  - List of defined mutation operators
  - Description of applied mutations and their impact
  - Summary of mutant survival and killing
  - Analysis of the test suite's effectiveness
  - Recommendations for improving the test suite
  - Conclusion
- **Report Format**: The report should be in a README.md file in the root of the folder where analysis was performed.
- **Submission**: Zip or tarball the entire folder and submit.


pytest --cov=Polynomial --cov=MutationOperators mutationTestCases.py 
.