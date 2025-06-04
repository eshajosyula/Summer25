import os

# keywords

SUS = ["nc", "ncat", "base64", "chmod 777", "sudo rm", "scp", "curl", "wget", "python3 -m http.server"]

def scan_history(): # essentially ctrl + f the keywords in SUS and flags it as suspicious
    res = []

    try:
        path = os.path.expanduser("~/.zsh_history")

        with open(path, "r") as file:
            for line in file:
                for keyword in SUS:
                    if keyword in line:
                        res.append(line.strip())

    except FileNotFoundError:
        print("couldn't find zsh history.")

    return res

def main():
    print("=== BLUEWATCH: Suspicious Command Scanner ===\n")

    alerts = scan_history()

    if alerts:
        for alert in alerts:
            print("sus command:", alert)
    else:
        print("no sus commands found!!")

if __name__ == "__main__":
    main()
