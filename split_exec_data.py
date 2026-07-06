#!/usr/bin/env python3
"""
Splits a package tree (e.g. bootstrap/usr) into:
  - <name>-exec/    : ELF executables and .so shared libraries
  - <name>-data/    : everything else (scripts, docs, config, python stdlib, etc.)
Also writes <name>-exec/manifest.json mapping original relative path -> .so filename.
"""
import sys
import os
import json
import subprocess


def is_elf(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == b"\x7fELF"
    except Exception:
        return False


def main():
    src_dir = sys.argv[1]      # e.g. bootstrap/usr
    exec_dir = sys.argv[2]     # e.g. bootstrap-exec
    data_dir = sys.argv[3]     # e.g. bootstrap-data/usr

    os.makedirs(exec_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    manifest = {}

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, src_dir)

            if os.path.islink(full_path):
                link_target = os.readlink(full_path)
                resolved = os.path.realpath(full_path)

                # If the symlink resolves to a real .so file, copy that real
                # file under the symlink's own name into exec_dir too, so the
                # dynamic linker can find it by the exact NEEDED name
                # (e.g. libreadline.so.8 -> real libreadline.so.8.2 content).
                if os.path.isfile(resolved) and is_elf(resolved) and ".so" in fname:
                    out_path = os.path.join(exec_dir, fname)
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    subprocess.run(["cp", resolved, out_path], check=True)
                    manifest[rel_path] = fname
                    continue

                # Otherwise, preserve as a symlink in the data tree
                out_path = os.path.join(data_dir, rel_path)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                if os.path.lexists(out_path):
                    os.remove(out_path)
                os.symlink(link_target, out_path)
                continue

            if is_elf(full_path):
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
                manifest[rel_path] = so_name
            else:
                out_path = os.path.join(data_dir, rel_path)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                subprocess.run(["cp", full_path, out_path], check=True)

    with open(os.path.join(exec_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Exec files: {len(manifest)}")
    print(f"Done: {src_dir} -> {exec_dir} (exec) + {data_dir} (data)")


if __name__ == "__main__":
    main()
