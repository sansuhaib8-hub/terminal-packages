path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """      - name: Ensure host python3.11 is available
        run: |
          ./scripts/run-docker.sh sudo apt-get update -y
          ./scripts/run-docker.sh sudo apt-get install -y python3.11"""

new = """      - name: Ensure host python3.11 is available
        run: |
          ./scripts/run-docker.sh bash -c '
            if ! command -v python3.11 >/dev/null 2>&1; then
              sudo ln -sf "$(command -v python3)" /usr/local/bin/python3.11
            fi
            python3.11 --version
          '"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، symlink زیادکرا.")
