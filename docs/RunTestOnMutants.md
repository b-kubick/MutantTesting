# Running Tests on Mutant Versions of the Polynomial Class

## Steps to Run Tests on Mutants

### 1. Prepare Mutant Files
- Ensure each mutant version of the `Polynomial` class is saved in separate Python files within the `mutated/` directory.
- For example, `Polynomial_Mutant1.py`, `Polynomial_Mutant2.py`, etc.

### 2. Modify Test Suite for Each Mutant
- Temporarily adjust `PolyTest.py` to import the `Polynomial` class from each mutant file instead of the original file.
- Change the import statement at the top of `PolyTest.py` for each run.
  - Example: Replace `from src.Polynomial import Polynomial` with `from mutated.Polynomial_Mutant1 import Polynomial` to test the first mutant.

### 3. Run the Tests
- Use a testing framework like pytest.
- Navigate to the directory containing `PolyTest.py`.
- Run the tests using a command like `pytest PolyTest.py` or `python -m pytest PolyTest.py`.
- Optionally, redirect the output to a results file, e.g., `pytest PolyTest.py > results/test_results_mutant1.txt`.

### 4. Repeat for Each Mutant
- Repeat the process for each mutant version, changing the import statement in `PolyTest.py` each time.

### 5. Analyze Test Outcomes
- Review the output or the contents of the `.txt` files in the `results/` directory.
- Determine if each mutant is "killed" (tests fail, indicating detection of the mutation) or "survives" (tests pass, mutation goes undetected).

### 6. Document the Results
- Keep a record of which mutants were killed and which survived.
- This information is crucial for analyzing the effectiveness of your test suite and identifying areas for improvement.

## Considerations
- Ensure your test environment is set up with all necessary dependencies.
- Important: Reset the import statement in `PolyTest.py` back to the original `Polynomial` class after testing all mutants.
- Completing these steps will give you a clear understanding of the strengths and weaknesses of your test suite.
