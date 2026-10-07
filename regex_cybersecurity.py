import re

def validate_password(pwd):
    checks = {
        "8 + chars"     : len(pwd) >= 8,
        "uppercase"     : bool(re.search(r"[A - Z]")),
        "lowercase"     : bool(re.search(r"[a - z]")),
        "digit"         : bool(re.search(r"\d", pwd)),
        "special"       : bool(re.search(r"[!@#$%^&*]" , pwd)),

    }

    for check , ok in checks.items():
                print(f"  {"✅" if ok else "❌"} {check}")
    return all(checks.values())
 
validate_password("Secure@123"),

def is_sqli(user_input):
        pat = r"(\b(SELECT | DROP | OR | AND | UNION)\b| -- |';)"
        return bool(re.search(pat , user_input , re.I))
