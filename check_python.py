import subprocess
result = subprocess.run(
    ["./scripts/run-docker.sh", "bash", "-c", "apt-cache search '^python3\\.[0-9]+$' && echo --- && ls /usr/bin/python3*"],
    capture_output=True, text=True
)
print(result.stdout)
print(result.stderr)
