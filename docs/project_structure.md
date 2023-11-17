polynomial-mutation-testing/
│
├── src/
│   ├── Polynomial.py         # Contains the Polynomial class definition
│   └── MutationOperators.py  # Module with mutation operator implementations
│
├── tests/
│   └── PolyTest.py           # Unit tests for the Polynomial class
│
├── mutated/
│   ├── Polynomial_Mutant1.py # Mutant version of Polynomial (e.g., coefficient mutation)
│   ├── Polynomial_Mutant2.py # Mutant version of Polynomial (e.g., arithmetic operation mutation)
│   ├── ...                   # Other mutant versions as needed
│   └── Polynomial_MutantN.py # N-th mutant version of Polynomial
│
├── results/
│   ├── test_results_mutant1.txt # Test results for the first mutant
│   ├── test_results_mutant2.txt # Test results for the second mutant
│   ├── ...                       # Test results for other mutants
│   └── test_results_mutantN.txt # Test results for the N-th mutant
│
└── README.md              # Project documentation and mutation testing report

