#!/bin/bash

echo "🚀 Starting CI validation for XSOAR demo project..."

# Check Python syntax
echo "🔍 Checking Python syntax in scripts/"
for file in scripts/*.py; do
    echo "Checking $file..."
    python3 -m py_compile "$file" || exit 1
done

# Optional: Check for existence of playbook_description.md and diagram
echo "📄 Checking documentation files..."
[ -f playbook_description.md ] || { echo "Missing playbook_description.md"; exit 1; }
[ -f playbook_diagram.png ] || { echo "Missing playbook_diagram.png"; exit 1; }

echo "✅ Validation passed."
