import os
from collections import deque
#os.system("ovs-vsctl show > ovs.txt")
vec = deque()

cmd = "ovs-vsctl del-port fptest-br %s"

f = open("ovs.txt", "r")
for line in f.readlines():
    line = line.strip()
    if "Port" in line:
        line = line.replace("Port", "").replace(" ", "")
        vec.append(line[1:-1])
    if "error" in line:
        port = vec.pop()
        print port
        os.system(cmd % port)

f.close()
