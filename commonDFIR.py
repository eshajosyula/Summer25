import os, time, platform

# list all files w/ last modified time
def recentMods():
    print("\n")
    print("============ recent mods =============")
    for file in os.listdir("."):
        path = os.path.join(".", file)
        if os.path.isfile(path):
            print(file, time.ctime(os.path.getmtime(path)))
    print("\n")

# print all env vars
def printEnvVars():
    print("\n")
    print("============ environment vars =============")
    for key in os.environ:
        print(key, "=", os.environ[key])

# print names of suspicious files
def susFiles():
    print("\n")
    print("============ sus files =============")
    sus = ['.exe', '.bat', '.ps1']
    for file in os.listdir('/Users/eshajosyula/Downloads'):
        if any(file.endswith(ext) for ext in sus):
            print("SUS : ", file)

# print all open ports
def getOpenPorts():
    print("checking 4 open network connections...")
    connections = os.popen("netstat -an").read()

    for line in connections.splitlines():
        if "ESTABLISHED" in line or "LISTEN" in line:
            print("->", line)

# print all running processes
def openProc():
    print("\n======================================================================================")
    print("running processes :\n")
    processes = os.popen("ps aux").read()
    print(processes)

# prints out known malware in computer files
def checkForMalware():
    iocFiles = [".Xauthority", "id_rsa", "malware.sh"]
    paths2check = ["/tmp", "/home", "/var/tmp"]

    for path in paths2check:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file in iocFiles:
                    print("found sus file : ", os.path.join(root, file))


def main():
    # recentMods()
    # printEnvVars()
    # susFiles()
    getOpenPorts()
    # openProc()
    checkForMalware()


if __name__ == "__main__":
    main()
