path = "lib/terminal_panel.dart"

with open(path, "r") as f:
    content = f.read()

old = """  Future<void> _checkTermux() async {
    setState(() => _checking = true);
    final available = await OwnTerminalService.isReady();
    setState(() {
      _termuxAvailable = available;
      _checking = false;
    });
  }"""

new = """  Future<void> _checkTermux() async {
    setState(() => _checking = true);
    final available = await OwnTerminalService.isReady();
    // ---- DEBUG ----
    final debug = await OwnTerminalService.debugInfo();
    // ignore: avoid_print
    print('KURDAPK_DEBUG: $debug');
    // ---- END DEBUG ----
    setState(() {
      _termuxAvailable = available;
      _checking = false;
    });
  }"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو.")
