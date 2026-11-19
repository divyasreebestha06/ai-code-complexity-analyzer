import sys
import json
from analyzer.metrics import CodeComplexityAnalyzer

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        code = "def sample(x):\n    if x > 0:\n        return 1\n    return 0"
    res = CodeComplexityAnalyzer.analyze_source(code)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
