import os

def getSysProcInfo(): # system and process info

    # ======= possible os cmds =========
    currUser = os.getlogin()            # returns current user
    osName = os.name                    # returns name of system
    path = os.getenv("PATH")            # returns full path address
    sysinfo = os.uname()                # returns detailed info about system (model, release version, machine, etc.)
    pid = os.getpid()                   # returns current process id

    # ======= prints ==========
    print("OS name: ", osName)
    print("current user: ", currUser)
    print("!!!!path!!!! : " , path)
    print("sysinfo : ", sysinfo)
    print("pid : ", pid)

def main():
    getSysProcInfo()

if __name__ == "__main__":
    main()