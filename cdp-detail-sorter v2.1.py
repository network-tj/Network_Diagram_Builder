import glob

queryoutput = input("Name of file output: ")
hostcheck = "hostname"
devicecheck = "Device ID"
ipaddresscheck = "IP address"
platformcheck = "Platform"
interfacecheck = "Interface"
hyphencheck = "---"

dir = "C:/Users/tj/PycharmProjects/Python-Learning/_Network Automation"

for file in glob.glob('*.log'):
    with open(file) as search:
        with open(queryoutput,"a") as foutput:
            for line in search:
                line = line.rstrip()
                if hostcheck in line:
                    hostentry = line.split("hostname ")[1]
                    foutput.write("Below CDP information is from " + hostentry + "\n")
                elif devicecheck in line:
                    foutput.write("Local Device: " + hostentry + "\n")
                    foutput.write("Remote " + line + "\n")
                elif ipaddresscheck in line:
                    foutput.write("Remote " + line.lstrip() + "\n")
                elif platformcheck in line:
                    foutput.write(line.split(",")[0] + "\n")
                elif interfacecheck in line:
                    foutput.write("Local Interface: " + line.split(",  Port")[0] + "\n")
                    foutput.write("Remote Interface: " + line.split("port): ")[1] + "\n")
                elif hyphencheck in line:
                    foutput.write(line)
                    foutput.write("\n")
                    foutput.write("\n")