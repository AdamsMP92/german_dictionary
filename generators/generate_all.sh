#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p ../csv-files

if python -c "import pandas" >/dev/null 2>&1; then
    python_cmd=(python)
elif command -v pixi >/dev/null 2>&1; then
    python_cmd=(pixi run python)
else
    echo "Neither Python with pandas nor pixi was found." >&2
    exit 1
fi

for generator in dict_*.py; do
    echo "Generating ${generator%.py}.csv"
    "${python_cmd[@]}" "$generator"
done
