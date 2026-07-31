path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """      - name: Assemble rootfs zip
        run: |
          mkdir -p rootfs
          cd rootfs
          for deb in ../output-aarch64/*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-rootfs-aarch64.zip rootfs

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-rootfs-aarch64
          path: kurdapk-rootfs-aarch64.zip"""

new = """      - name: Assemble bootstrap zip (bash + coreutils)
        run: |
          mkdir -p bootstrap
          cd bootstrap
          for deb in ../output-aarch64/bash_*.deb ../output-aarch64/coreutils_*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-bootstrap.zip bootstrap

      - name: Assemble python zip
        run: |
          mkdir -p python-pkg
          cd python-pkg
          for deb in ../output-aarch64/python*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-python.zip python-pkg

      - name: Assemble git zip
        run: |
          mkdir -p git-pkg
          cd git-pkg
          for deb in ../output-aarch64/git*.deb; do
            ar x "$deb"
            tar xf data.tar.xz
            rm -f data.tar.xz control.tar.xz debian-binary
          done
          cd ..
          zip -r kurdapk-git.zip git-pkg

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-bootstrap-zip
          path: kurdapk-bootstrap.zip

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-python-zip
          path: kurdapk-python.zip

      - uses: actions/upload-artifact@v4
        with:
          name: kurdapk-git-zip
          path: kurdapk-git.zip"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، دابەشکرا بۆ ٣ zip.")
