path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

# ---- 1. Replace assemble steps to add split + separate archives ----
replacements = [
    (
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
          tar czf kurdapk-bootstrap.tar.gz bootstrap""",
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
          python3 split_exec_data.py bootstrap/usr bootstrap-exec bootstrap-data/usr
          zip -r kurdapk-bootstrap-exec.zip bootstrap-exec
          tar czf kurdapk-bootstrap-data.tar.gz bootstrap-data"""
    ),
    (
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
          tar czf kurdapk-python.tar.gz python-pkg""",
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
          python3 split_exec_data.py python-pkg/usr python-exec python-data/usr
          zip -r kurdapk-python-exec.zip python-exec
          tar czf kurdapk-python-data.tar.gz python-data"""
    ),
    (
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
          tar czf kurdapk-git.tar.gz git-pkg""",
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
          python3 split_exec_data.py git-pkg/usr git-exec git-data/usr
          zip -r kurdapk-git-exec.zip git-exec
          tar czf kurdapk-git-data.tar.gz git-data"""
    ),
    (
"""      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-bootstrap-zip
          path: kurdapk-bootstrap.tar.gz

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-python-zip
          path: kurdapk-python.tar.gz

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-git-zip
          path: kurdapk-git.tar.gz""",
"""      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-bootstrap-exec
          path: kurdapk-bootstrap-exec.zip

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-bootstrap-data
          path: kurdapk-bootstrap-data.tar.gz

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-python-exec
          path: kurdapk-python-exec.zip

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-python-data
          path: kurdapk-python-data.tar.gz

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-git-exec
          path: kurdapk-git-exec.zip

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-git-data
          path: kurdapk-git-data.tar.gz"""
    ),
]

count = 0
for old, new in replacements:
    if old not in content:
        print(f"هەڵە: نموونەیەک نەدۆزرایەوە (سەرەتای: {old[:60]!r})")
    else:
        content = content.replace(old, new, 1)
        count += 1

with open(path, "w") as f:
    f.write(content)

print(f"{count}/4 گۆڕانکاری سەرکەوتوو بوو.")
