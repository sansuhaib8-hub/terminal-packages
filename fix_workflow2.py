path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = "      - name: Build core packages for aarch64 (via docker)"
new = """      - name: Install build tools (automake, autoconf, libtool)
        run: |
          ./scripts/run-docker.sh sudo apt-get update -y
          ./scripts/run-docker.sh sudo apt-get install -y automake autoconf libtool m4 perl gettext

      - name: Build core packages for aarch64 (via docker)"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، install step زیادکرایەوە.")
