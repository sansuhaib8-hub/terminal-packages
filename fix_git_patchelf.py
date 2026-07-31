path = "/data/data/com.termux/files/home/terminal-packages/.github/workflows/kurdapk-bootstrap.yml"

with open(path, "r") as f:
    content = f.read()

old = """        python3 split_exec_data.py git-pkg/usr git-exec git-data/usr
          zip -r kurdapk-git-exec.zip git-exec"""

new = """        python3 split_exec_data.py git-pkg/usr git-exec git-data/usr
          cd git-exec
          for f in *.so; do
            needed=$(patchelf --print-needed "$f" 2>/dev/null || true)
            for n in $needed; do
              case "$n" in
                *.so.*)
                  base=$(echo "$n" | sed -E 's/(\\.so)\\..*/\\1/')
                  patchelf --replace-needed "$n" "$base" "$f" 2>/dev/null || true
                  ;;
              esac
            done
          done
          cd ..
          zip -r kurdapk-git-exec.zip git-exec"""

if old not in content:
    print("ERROR: pattern not found")
else:
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)
    print("Patched successfully")
