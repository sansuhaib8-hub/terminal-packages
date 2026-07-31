path = "packages/tar/build.sh"

with open(path, "r") as f:
    content = f.read()

old = 'termux_step_pre_configure() {\n\tCPPFLAGS+=" -D__USE_FORTIFY_LEVEL=0"'
new = 'termux_step_pre_configure() {\n\t(cd "$TERMUX_PKG_SRCDIR" && autoreconf -fi)\n\tCPPFLAGS+=" -D__USE_FORTIFY_LEVEL=0"'

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە، پێویستە بە دەستی بپشکنین.")
else:
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، autoreconf زیادکرا.")
