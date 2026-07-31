path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """      - name: List built debs
        run: ls -la output-aarch64/"""

new = """      - name: List built debs
        run: ls -la output-aarch64/

      - name: Assemble rootfs zip
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

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، step زیادکرا.")
