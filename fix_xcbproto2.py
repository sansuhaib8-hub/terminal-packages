path = "packages/xcb-proto/build.sh"

with open(path, "r") as f:
    content = f.read()

addition = '''
termux_step_pre_configure() {
\tautoreconf -fi
}
'''

if "termux_step_pre_configure" in content:
    print("هەڵە: pre_configure پێشتر هەیە، پێویستە بە دەستی تێکەڵ بکرێت.")
else:
    content = content.rstrip() + "\n" + addition
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، autoreconf زیادکرا.")
