from analyzer.metrics import CodeComplexityAnalyzer

class ReportGenerator:
    @staticmethod
    def generate_markdown(filename: str, source_code: str) -> str:
        metrics = CodeComplexityAnalyzer.analyze_source(source_code)
        return f"""# Code Quality Report: `{filename}`

- **Lines of Code (LOC):** {metrics['lines_of_code']}
- **Functions Defined:** {metrics['functions']}
- **Cyclomatic Complexity (CC):** {metrics['cyclomatic_complexity']}
- **Maintainability Index (MI):** {metrics['maintainability_index']} / 100
- **Overall Rating:** **{metrics['code_health']}**
"""
