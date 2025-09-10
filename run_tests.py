#!/usr/bin/env python3
<<<<<<< HEAD
"""
Test runner for AGENTIC-devDOCS automation scripts.
"""
=======
\"\"\"
Test runner for AGENTIC-devDOCS automation scripts.
\"\"\"
>>>>>>> 3adb7ff0547ece3b76ca0e727f06913ec9e5bd75

import subprocess
import sys
import os

def run_tests():
<<<<<<< HEAD
    """Run all tests using pytest"""
=======
    \"\"\"Run all tests using pytest\"\"\"
>>>>>>> 3adb7ff0547ece3b76ca0e727f06913ec9e5bd75
    try:
        # Run pytest
        result = subprocess.run([
            sys.executable, '-m', 'pytest', 
            'tests/', 
            '-v', 
            '--tb=short'
        ], check=True, capture_output=True, text=True)
        
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with return code {e.returncode}")
        print(e.stdout)
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("Error: pytest not found. Please install it with 'pip install pytest'")
        return False

if __name__ == "__main__":
    success = run_tests()
<<<<<<< HEAD
    sys.exit(0 if success else 1)
=======
    sys.exit(0 if success else 1)
>>>>>>> 3adb7ff0547ece3b76ca0e727f06913ec9e5bd75
