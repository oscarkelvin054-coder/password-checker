import re, random, string

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "=== OSCAR HACKER TOOL v3.0 PRO ===" + RESET)

COMMON = ["123456","password","qwerty","admin","123","letmein"]

pwd = input("Enter password to check: ")

score = 0
print(f"\n{ CYAN }[+] Analyzing: {pwd}{ RESET }\n")

if pwd.lower() in COMMON:
    print(RED + "❌ VERY WEAK - Common password! Score: 0/100" + RESET)
    crack = "Instant - 0 seconds"
else:
    if len(pwd) >= 12:
        score += 30
        print(GREEN + "✅ Length 12+ : +30" + RESET)
        crack = "500 years"
    elif len(pwd) >= 8:
        score += 15
        print(YELLOW + "⚠️  Length 8-11 : +15" + RESET)
        crack = "5 days"
    else:
        print(RED + "❌ Too short (<8) : +0" + RESET)
        crack = "2 seconds"

    if re.search(r"[A-Z]", pwd):
        score += 20
        print(GREEN + "✅ Has UPPERCASE : +20" + RESET)
    else:
        print(RED + "❌ No UPPERCASE : +0" + RESET)

    if re.search(r"[0-9]", pwd):
        score += 20
        print(GREEN + "✅ Has NUMBER : +20" + RESET)
    else:
        print(RED + "❌ No NUMBER : +0" + RESET)

    if re.search(r"[!@#$%^&*()_+\-={}\[\]:;\"'<>,.?/]", pwd):
        score += 30
        print(GREEN + "✅ Has SYMBOL (!@#$) : +30" + RESET)
    else:
        print(RED + "❌ No SYMBOL : +0" + RESET)

    print(f"\n--- FINAL SCORE: {score}/100 ---")
    print(f"⏱️  Time to crack: {crack}")

    if score < 40:
        print(RED + "🔴 WEAK - Change am NOW!" + RESET)
    elif score < 75:
        print(YELLOW + "🟡 MEDIUM - E fit better" + RESET)
    else:
        print(GREEN + "🟢 STRONG - You be hacker!" + RESET)

# Bonus - generate strong password
chars = string.ascii_letters + string.digits + "!@#$%"
strong = ''.join(random.choice(chars) for _ in range(12))
print(CYAN + f"\n💡 Suggested strong password: {strong}" + RESET)
