import hashlib

def check_password(password):
    print(f"[+] Checking: {password}")
    # simple demo checker
    if len(password) < 8:
        print("Weak: Too short!")
    else:
        print("Strong password!")
    
if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    check_password(pwd)
