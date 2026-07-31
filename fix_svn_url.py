path = "packages/subversion/build.sh"

with open(path, "r") as f:
    content = f.read()

old = "TERMUX_PKG_SRCURL=https://www.apache.org/dist/subversion/subversion-${TERMUX_PKG_VERSION}.tar.bz2"
new = "TERMUX_PKG_SRCURL=https://archive.apache.org/dist/subversion/subversion-${TERMUX_PKG_VERSION}.tar.bz2"

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، URL گۆڕا بۆ archive.")
