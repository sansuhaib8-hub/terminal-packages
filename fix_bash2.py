path = "packages/bash/build.sh"

with open(path, "r") as f:
    content = f.read()

old = 'termux_step_pre_configure() {\n\tCFLAGS+=" -std=gnu17"'
new = 'termux_step_pre_configure() {\n\tCFLAGS+=" -std=gnu17"\n\texport CC_FOR_BUILD="gcc -std=gnu17"'

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو، CC_FOR_BUILD زیادکرا.")
