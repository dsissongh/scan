import subprocess

host = "172.16.10.97"

ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
lines = str(out).split("\\")
#for line in lines:
elements = lines[7].split(",")
print(elements[3])