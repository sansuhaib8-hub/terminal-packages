path = ".github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

replacements = [
    ("cp -r bootstrap_raw/data/data/*/files/usr bootstrap/\n          zip -r kurdapk-bootstrap.zip bootstrap",
     "cp -r bootstrap_raw/data/data/*/files/usr bootstrap/\n          tar czf kurdapk-bootstrap.tar.gz bootstrap"),
    ("cp -r python-pkg-raw/data/data/*/files/usr python-pkg/\n          zip -r kurdapk-python.zip python-pkg",
     "cp -r python-pkg-raw/data/data/*/files/usr python-pkg/\n          tar czf kurdapk-python.tar.gz python-pkg"),
    ("cp -r git-pkg-raw/data/data/*/files/usr git-pkg/\n          zip -r kurdapk-git.zip git-pkg",
     "cp -r git-pkg-raw/data/data/*/files/usr git-pkg/\n          tar czf kurdapk-git.tar.gz git-pkg"),
    ("path: kurdapk-bootstrap.zip", "path: kurdapk-bootstrap.tar.gz"),
    ("path: kurdapk-python.zip", "path: kurdapk-python.tar.gz"),
    ("path: kurdapk-git.zip", "path: kurdapk-git.tar.gz"),
]

count_total = 0
for old, new in replacements:
    if old not in content:
        print(f"هەڵە: نموونەیەک نەدۆزرایەوە: {old[:60]}")
    else:
        content = content.replace(old, new, 1)
        count_total += 1

with open(path, "w") as f:
    f.write(content)

print(f"{count_total}/6 گۆڕانکاری سەرکەوتوو بوو.")
