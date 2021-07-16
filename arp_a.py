from subprocess import Popen, PIPE, STDOUT

# Send arp -a request to console and store dynamic IP addresses of reply in dynaIP
arpA_req = Popen('arp -a', stdin=PIPE, stdout=PIPE, stderr=STDOUT)
dynaIP = []

while arpA_req.stdout.readline():
    line = arpA_req.stdout.readline().decode('ascii').rsplit()

    if len(line) == 3:
        ip, phyAdd, ipType = line

        if ipType == 'dynamic':
            dynaIP.append(line)

# Use tracert to get ip addresses resolved to name
for ip in dynaIP:
    print('IP ADDRESS:', ip[0])

    nbtstatA_req = Popen('tracert ' + ip[0], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    while nbtstatA_req.stdout.readline():
        print(nbtstatA_req.stdout.readline())
