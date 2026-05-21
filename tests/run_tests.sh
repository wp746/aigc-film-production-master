#!/bin/bash
# Test runner for AIGC Film Production Master Skill

# Get the directory where this script resides
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR/.."

echo "=================================================="
echo "Running AIGC Film Production Master test suite..."
echo "=================================================="

python3 -m unittest discover -s tests -p "test_*.py"
RESULT=$?

echo "=================================================="
if [ $RESULT -eq 0 ]; then
    echo "SUCCESS: All tests passed!"
else
    echo "FAILURE: Some tests failed."
fi
echo "=================================================="

exit $RESULT
