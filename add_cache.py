path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = "      - uses: actions/checkout@v4"
new = """      - uses: actions/checkout@v4

      - name: Cache termux build packages
        uses: actions/cache@v4
        with:
          path: |
            ~/.termux-build-cache
          key: termux-pkgs-${{ hashFiles('packages/**/build.sh') }}
          restore-keys: |
            termux-pkgs-"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، cache زیادکرا.")
