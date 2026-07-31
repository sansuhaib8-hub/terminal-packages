path = "packages/python/build.sh"

with open(path, "r") as f:
    content = f.read()

# 1. Add --without-tcltk to configure args
old1 = 'TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" --build=$TERMUX_BUILD_TUPLE --with-system-ffi --with-system-expat --without-ensurepip"'
new1 = 'TERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" --build=$TERMUX_BUILD_TUPLE --with-system-ffi --with-system-expat --without-ensurepip"\nTERMUX_PKG_EXTRA_CONFIGURE_ARGS+=" --without-tcltk"'

# 2. Remove _tkinter from the required-modules check
old2 = 'for module in _bz2 _curses _lzma _sqlite3 _ssl _tkinter zlib; do'
new2 = 'for module in _bz2 _curses _lzma _sqlite3 _ssl zlib; do'

count1 = content.count(old1)
count2 = content.count(old2)

if count1 == 0 or count2 == 0:
    print(f"هەڵە: نموونەکان نەدۆزرانەوە. count1={count1}, count2={count2}")
else:
    content = content.replace(old1, new1, 1)
    content = content.replace(old2, new2, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، tkinter بەتەواوی لابرا.")
