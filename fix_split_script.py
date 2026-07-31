path = "split_exec_data.py"

with open(path, "r") as f:
    content = f.read()

old = """            if is_elf(full_path):
                so_name = rel_path.replace("/", "_") + ".so"
                out_path = os.path.join(exec_dir, so_name)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                subprocess.run(["cp", full_path, out_path], check=True)
                manifest[rel_path] = so_name"""

new = """            if is_elf(full_path):
                base = os.path.basename(rel_path)
                if ".so" in base:
                    # Real shared library: keep its original filename so the
                    # dynamic linker can resolve DT_NEEDED entries by name.
                    so_name = base
                else:
                    # Standalone executable: mangle the path into a unique
                    # .so-suffixed name (we invoke these via manifest lookup,
                    # never by bare filename, so collisions must be avoided).
                    so_name = rel_path.replace("/", "_") + ".so"
                out_path = os.path.join(exec_dir, so_name)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                subprocess.run(["cp", full_path, out_path], check=True)
                manifest[rel_path] = so_name"""

if old not in content:
    print("هەڵە: نموونەکە نەدۆزرایەوە.")
else:
    content = content.replace(old, new, 1)
    with open(path, "w") as f:
        f.write(content)
    print("سەرکەوتوو بوو.")
