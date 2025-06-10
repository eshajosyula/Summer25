import os, time

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

def susFiles():
    print("\n")
    print("============ sus files =============")
    sus = ['.exe', '.bat', '.ps1']
    for file in os.listdir('/Users/eshajosyula/Downloads'):
        if any(file.endswith(ext) for ext in sus):
            print("SUS : ", file)

def main():
    recentMods()
    printEnvVars()
    susFiles()


if __name__ == "__main__":
    main()
