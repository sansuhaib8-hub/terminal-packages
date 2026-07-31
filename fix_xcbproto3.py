path = "packages/xcb-proto/build.sh"

with open(path, "r") as f:
    content = f.read()

old = '''TERMUX_PKG_EXTRA_CONFIGURE_ARGS="
PYTHON=python${TERMUX_PYTHON_VERSION}
am_cv_python_pythondir=$TERMUX_PYTHON_HOME/site-packages
am_cv_python_version=${TERMUX_PYTHON_VERSION}
"'''

new = '''TERMUX_PKG_EXTRA_CONFIGURE_ARGS="
PYTHON=python3
am_cv_python_pythondir=$TERMUX_PYTHON_HOME/site-packages
am_cv_python_version=${TERMUX_PYTHON_VERSION}
"'''

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، PYTHON بۆ python3 گۆڕا.")
