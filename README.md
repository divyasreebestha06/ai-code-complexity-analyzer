# 🧠 ai-code-complexity-analyzer

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](analyzer/)
[![AST](https://img.shields.io/badge/AST-Static_Analysis-orange?style=for-the-badge)](analyzer/)
[![CI](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](ci/)

Static Python Code Complexity Analyzer computing Cyclomatic Complexity, Halstead metrics, and Maintainability Index.

## Features
- **Cyclomatic Complexity (McCabe):** Measures independent execution paths using Python's native AST parser.
- **Maintainability Index:** Computes composite maintainability score from cyclomatic complexity and LOC.
- **Automated Grading:** Classifies codebases into `EXCELLENT`, `MODERATE`, and `NEEDS_REFACTORING`.

## Usage
```bash
python -m analyzer.cli my_script.py
```
