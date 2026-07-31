#!/usr/bin/env python3
"""
Splits a package tree (e.g. bootstrap/usr) into:
  - <name>-exec/    : ELF executables and .so shared libraries
  - <name>-data/    : everything else (scripts, docs, config, python stdlib, etc.)
Also writes <name>-exec/manifest.json mapping original relative path -> .so filename.

Two-pass approach:
  Pass 1: copy every real (non-symlink) ELF file into exec_dir, recording
          rel_path -> so_name in the manifest.
  Pass 2: walk symlinks. If a symlink resolves (via realpath) to a file that
          was copied in pass 1, add an entry mapping the symlink's own
          rel_path to the SAME so_name as its target (e.g. "bin/ls" ->
          "bin_coreutils.so" when ls is a symlink to coreutils). This covers
          busybox-style applet symlinks (ls -> coreutils) and version
          symlinks (python3 -> python3.11) alike. Symlinks that don't
          resolve to a known exec entry are preserved as real symlinks in
          the data tree (their old behavior).
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
    realpath_to_so_name = {}
    symlinks = []

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, src_dir)

            if os.path.islink(full_path):
                symlinks.append((rel_path, full_path))
                continue

            if is_elf(full_path):
                base = os.path.basename(rel_path)
                if ".so" in base:
                    so_name = base
                else:
                    so_name = rel_path.replace("/", "_") + ".so"
                out_path = os.path.join(exec_dir, so_name)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                subprocess.run(["cp", full_path, out_path], check=True)
                manifest[rel_path] = so_name
                realpath_to_so_name[os.path.realpath(full_path)] = so_name
            else:
                out_path = os.path.join(data_dir, rel_path)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                subprocess.run(["cp", full_path, out_path], check=True)

    for rel_path, full_path in symlinks:
        resolved = os.path.realpath(full_path)
        so_name = realpath_to_so_name.get(resolved)

        if so_name is not None:
            manifest[rel_path] = so_name
            continue

        link_target = os.readlink(full_path)
        out_path = os.path.join(data_dir, rel_path)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        if os.path.lexists(out_path):
            os.remove(out_path)
        os.symlink(link_target, out_path)

    with open(os.path.join(exec_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Exec files: {len(manifest)}")
    print(f"Done: {src_dir} -> {exec_dir} (exec) + {data_dir} (data)")


if __name__ == "__main__":
    main()
