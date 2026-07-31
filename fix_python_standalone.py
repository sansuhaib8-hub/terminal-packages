path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """      - name: Ensure host python3.11 is available
        run: |
          ./scripts/run-docker.sh bash -c '
            if ! command -v python3.11 >/dev/null 2>&1; then
              sudo ln -sf "$(command -v python3)" /usr/local/bin/python3.11
            fi
            python3.11 --version
          '"""

new = """      - name: Ensure host python3.11 is available
        run: |
          ./scripts/run-docker.sh bash -c '
            if ! python3.11 --version 2>/dev/null | grep -q "3.11"; then
              cd /tmp
              curl -L -o py311.tar.gz https://github.com/indygreg/python-build-standalone/releases/download/20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz
              tar xf py311.tar.gz
              sudo ln -sf /tmp/python/bin/python3.11 /usr/local/bin/python3.11
            fi
            python3.11 --version
          '"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، standalone python3.11 زیادکرا.")
