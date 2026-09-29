password = input("Enter password to check: ")

if len(password) < 8:
    print("🔴 WEAK - Too short!")
elif password == "123456" or password == "password":
    print("🔴 WEAK - Common password!")
else:
    print("🟢 STRONG - You good!")
    print(f"Length: {len(password)}")
