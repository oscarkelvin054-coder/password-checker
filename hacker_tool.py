import re

print("=== OSCAR HACKER TOOL v2.0 ===")

COMMON = ["123456","password","qwerty","admin","123","letmein"]

pwd = input("Enter password to check: ")

score = 0
print(f"\n[+] Analyzing: {pwd}\n")

if pwd.lower() in COMMON:
    print("❌ VERY WEAK - Common password! Score: 0/100")
else:
    # Length
    if len(pwd) >= 12:
        score += 30
        print("✅ Length 12+ : +30")
    elif len(pwd) >= 8:
        score += 15
        print("⚠️  Length 8-11 : +15 (use 12+)")
    else:
        print("❌ Too short (<8) : +0")

    # Uppercase
    if re.search(r"[A-Z]", pwd):
        score += 20
        print("✅ Has UPPERCASE : +20")
    else:
        print("❌ No UPPERCASE : +0")

    # Number
    if re.search(r"[0-9]", pwd):
        score += 20
        print("✅ Has NUMBER : +20")
    else:
        print("❌ No NUMBER : +0")

    # Symbol
    if re.search(r"[!@#$%^&*()_+\-={}\[\]:;\"'<>,.?/]", pwd):
        score += 30
        print("✅ Has SYMBOL (!@#$) : +30")
    else:
        print("❌ No SYMBOL : +0")

    print(f"\n--- FINAL SCORE: {score}/100 ---")
    if score < 40:
        print("🔴 WEAK - Change am NOW!")
    elif score < 75:
        print("🟡 MEDIUM - E fit better")
    else:
        print("🟢 STRONG - You be hacker!")

