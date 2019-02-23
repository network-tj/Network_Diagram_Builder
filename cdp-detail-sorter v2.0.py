import glob

hostcheck = "hostname"
devicecheck = "Device ID"
ipaddresscheck = "IP address"
platformcheck = "Platform"
interfacecheck = "Interface"
hyphencheck = "---"

dir = "C:/Users/tj/PycharmProjects/Python-Learning/_Network Automation"



for file in glob.glob('*.log'):
    with open(file) as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if hostcheck in line:
                hostentry = line.split("hostname ")[1]
                print("Below CDP information is from " + hostentry)
            elif devicecheck in line:
                print("Local Device: " + hostentry)
                print("Remote " + line)
            elif ipaddresscheck in line:
                print("Remote " + line.lstrip())
            elif platformcheck in line:
                print(line.split(",")[0])
            elif interfacecheck in line:
                print("Local Interface: " + line.split(",  Port")[0])
                print("Remote Interface: " + line.split("port): ")[1])
            elif hyphencheck in line:
                print(line)
                print("\n")