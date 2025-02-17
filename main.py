import pyfiglet
import subprocess
from colorama import Fore, init, Style

# Initialize colorama
init(autoreset=True)

# Function to create a box
def create_box(content, width, color=Fore.RESET):
    border = color + "+" + "-" * width + "+"
    padded_content = [
        color + "|" + line.center(width) + "|" for line in content
    ]
    return [border] + padded_content + [border]
    
url_box = create_box(
    [Fore.CYAN + Style.BRIGHT + "https://t.me/D4rkCipherX"], 30, Fore.CYAN
)

menu_box = create_box(
    [
        Fore.YELLOW + Style.BRIGHT + "1. Get Token",
        Fore.YELLOW + Style.BRIGHT + "2. Auto Referral",
        Fore.YELLOW + Style.BRIGHT + "3. Setup",
        Fore.YELLOW + Style.BRIGHT + "4. Openloop | {IP}",
        Fore.YELLOW + Style.BRIGHT + "5. Openloop | {PROXY}",
    ],
    40,
    Fore.YELLOW,
)

print("\n".join(url_box))
print("\n".join(menu_box))

# Accept user input
try:
    choice = int(input(Fore.GREEN + Style.BRIGHT + "\nEnter your choice (1-5): "))
    
    
    scripts = {
        1: "getToken.js",
        2: "autoreff.js",
        3: "setup.js",
        4: "openloop.js",
        5: "openloop-proxy.js"
    }
    
    
    if choice in scripts:
        print(Fore.CYAN + Style.BRIGHT + f"\nRunning script: {scripts[choice]}")
        # Run the corresponding script using subprocess
        subprocess.run(["node", scripts[choice]])
    else:
        print(Fore.RED + Style.BRIGHT + "\nInvalid choice! Please select a number between 1 and 5.")
except ValueError:
    print(Fore.RED + Style.BRIGHT + "\nInvalid input! Please enter a number between 1 and 5.")