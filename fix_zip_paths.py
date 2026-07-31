path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

replacements = [
    (
"""      - name: Assemble bootstrap zip (bash + coreutils)
        run: |
          mkdir -p bootstrap
          cd bootstrap
          for deb in ../output-aarch64/bash_*.deb ../output-aarch64/coreutils_*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-bootstrap.zip bootstrap""",
"""      - name: Assemble bootstrap zip (bash + coreutils)
        run: |
          mkdir -p bootstrap_raw bootstrap
          cd bootstrap_raw
          for deb in ../output-aarch64/bash_*.deb ../output-aarch64/coreutils_*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          cp -r bootstrap_raw/data/data/*/files/usr bootstrap/
          zip -r kurdapk-bootstrap.zip bootstrap"""
    ),
    (
"""      - name: Assemble python zip
        run: |
          mkdir -p python-pkg
          cd python-pkg
          for deb in ../output-aarch64/python*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-python.zip python-pkg""",
"""      - name: Assemble python zip
        run: |
          mkdir -p python-pkg-raw python-pkg
          cd python-pkg-raw
          for deb in ../output-aarch64/python*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          cp -r python-pkg-raw/data/data/*/files/usr python-pkg/
          zip -r kurdapk-python.zip python-pkg"""
    ),
    (
"""      - name: Assemble git zip
        run: |
          mkdir -p git-pkg
          cd git-pkg
          for deb in ../output-aarch64/git*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-git.zip git-pkg""",
"""      - name: Assemble git zip
        run: |
          mkdir -p git-pkg-raw git-pkg
          cd git-pkg-raw
          for deb in ../output-aarch64/git*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          cp -r git-pkg-raw/data/data/*/files/usr git-pkg/
          zip -r kurdapk-git.zip git-pkg"""
    ),
]

count_total = 0
for old, new in replacements:
    if old not in content:
        print(f"هەڵە: نموونەیەک نەدۆزرایەوە (سەرەتای: {old[:50]}...)")
    else:
        content = content.replace(old, new, 1)
        count_total += 1

with open(path, "w") as f:
    f.write(content)

print(f"{count_total}/3 گۆڕانکاری سەرکەوتوو بوو.")
