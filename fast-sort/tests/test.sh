#!/bin/bash

mkdir -p /logs/verifier

curl -LsSf https://astral.sh/uv/0.8.17/install.sh | sh
source "$HOME/.local/bin/env"

uvx pytest@8.4.1 /tests/test_outputs.py -rA

# If tests pass, run benchmark.py.
# Output is saved to a file by the code in benchmark.py itself.
if [ $? -eq 0 ]; then
  cd /tests && python benchmark.py 1
else
  echo '{"reward": 0}' > /logs/verifier/reward.json
fi
