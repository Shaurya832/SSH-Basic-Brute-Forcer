SSH Brute-Forcer

A straightforward Python script designed to attempt SSH logins using a provided list of passwords. This tool is built for educational purposes and authorized security testing only.
Features

    Flexible Password List: Choose between using a default password-list.txt file (located in the same directory as the script) or providing a path to a custom password list.

    Basic Error Handling: Implements try-except blocks to gracefully handle SSH authentication failures (paramiko.AuthenticationException) and general connection issues.

    Clear Console Output: Provides real-time feedback on each password attempt, indicating success or failure.

Getting Started
Prerequisites

To run this script, you will need:

    Python 3.x: Ensure Python is installed on your system. You can download it from python.org.

    paramiko library: This Python library is used for SSH connectivity. Install it using pip:

    pip install paramiko

Installation

    Save the script:
    Copy your Python code and save it as a .py file (e.g., ssh_bruteforce.py).

    Prepare your password list:
    If you intend to use the "default" password list option, create a text file named password-list.txt in the same directory as your ssh_bruteforce.py script. Each potential password should be on a new line.

    Example password-list.txt content:

    userpass123
    changeme
    password
    secret123

How to Use

    Open your terminal or command prompt.

    Navigate to the directory where you saved ssh_bruteforce.py (and password-list.txt if using the default option).

    Execute the script using Python:

    python ssh_bruteforce.py

    Follow the interactive prompts:

        The script will first ask if you want to use the default password list or a custom one. Type default or custom and press Enter.

        You will then be prompted to enter the IP Address of the target SSH server.

        Next, enter the Username for which you want to attempt logins.

        If you selected "custom" earlier, you will be asked to provide the full path to your custom password list file.

Important Notes & Disclaimer

    Ethical and Legal Use: This script is designed for educational purposes and legitimate security assessments (penetration testing) on systems for which you have explicit, written permission. Attempting to access systems without authorization is illegal and unethical.

    Server Rate Limiting: Be aware that many SSH servers implement security measures such as rate limiting or account lockouts after a certain number of failed login attempts. Using this script can trigger these defenses, potentially leading to your IP being temporarily blocked or the target account being locked.

    Host Key Verification: For simplicity and ease of use in a learning environment, this script utilizes paramiko.AutoAddPolicy(). This policy automatically adds unknown host keys to your known_hosts file without manual verification. In a production or highly secure penetration testing scenario, a more stringent host key verification policy would typically be employed to mitigate Man-in-the-Middle (MITM) attack risks. For personal learning and testing on known, controlled environments, this approach is generally acceptable.
