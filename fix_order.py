path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """          ./scripts/run-docker.sh ./build-package.sh -a aarch64 -o output-aarch64 bash
          ./scripts/run-docker.sh ./build-package.sh -a aarch64 -o output-aarch64 coreutils"""

new = """          ./scripts/run-docker.sh ./build-package.sh -a aarch64 -o output-aarch64 coreutils
          ./scripts/run-docker.sh ./build-package.sh -a aarch64 -o output-aarch64 bash"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، ڕیزبەندی گۆڕا.")
