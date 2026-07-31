import re

path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

# Remove the entire "Install build tools" step block
pattern = re.compile(
    r"\n      - name: Install build tools.*?(?=\n      - name: Build core packages)",
    re.DOTALL
)

new_content, count = pattern.subn("", content)

if count == 0:
    print("هیچ گۆڕانکارییەک نەکرا! step-ەکە نەدۆزرایەوە.")
else:
    with open(path, "w") as f:
        f.write(new_content)
    print(f"سەرکەوتوو بوو، {count} step سڕایەوە.")
