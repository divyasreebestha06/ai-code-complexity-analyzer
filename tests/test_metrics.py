import unittest
from analyzer.metrics import CodeComplexityAnalyzer

class TestComplexityAnalyzer(unittest.TestCase):
    def test_simple_function(self):
        code = """
def add(a, b):
    return a + b
"""
        res = CodeComplexityAnalyzer.analyze_source(code)
        self.assertEqual(res["cyclomatic_complexity"], 1)
        self.assertEqual(res["functions"], 1)
        self.assertGreater(res["maintainability_index"], 80)

    def test_branching_complexity(self):
        code = """
def classify(num):
    if num > 100:
        return 'high'
    elif num > 50:
        return 'mid'
    elif num > 0:
        return 'low'
    else:
        return 'negative'
"""
        res = CodeComplexityAnalyzer.analyze_source(code)
        self.assertGreater(res["cyclomatic_complexity"], 3)
        self.assertEqual(res["functions"], 1)

if __name__ == "__main__":
    unittest.main()
