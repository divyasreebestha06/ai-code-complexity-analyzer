import ast
import math
from typing import Dict, Any

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.cyclomatic_complexity = 1  # Base complexity
        self.functions_count = 0
        self.lines_of_code = 0
        self.branch_nodes = (
            ast.If, ast.For, ast.While, ast.With,
            ast.Try, ast.ExceptHandler, ast.Assert
        )

    def visit_FunctionDef(self, node):
        self.functions_count += 1
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.functions_count += 1
        self.generic_visit(node)

    def generic_visit(self, node):
        if isinstance(node, self.branch_nodes):
            self.cyclomatic_complexity += 1
        super().generic_visit(node)

class CodeComplexityAnalyzer:
    @staticmethod
    def analyze_source(source_code: str) -> Dict[str, Any]:
        lines = [line for line in source_code.splitlines() if line.strip() and not line.strip().startswith("#")]
        loc = len(lines)
        tree = ast.parse(source_code)
        visitor = ComplexityVisitor()
        visitor.visit(tree)

        cc = visitor.cyclomatic_complexity
        # Maintainability Index approximation: 171 - 5.2 * ln(Halstead) - 0.23 * CC - 16.2 * ln(LOC)
        # Simplified normalized score (0 - 100)
        penalty = (cc * 3.5) + (math.log(max(1, loc)) * 8)
        mi = max(0, min(100, round(100 - penalty, 2)))

        rating = "EXCELLENT" if mi >= 75 else ("MODERATE" if mi >= 50 else "NEEDS_REFACTORING")

        return {
            "lines_of_code": loc,
            "functions": visitor.functions_count,
            "cyclomatic_complexity": cc,
            "maintainability_index": mi,
            "code_health": rating
        }
