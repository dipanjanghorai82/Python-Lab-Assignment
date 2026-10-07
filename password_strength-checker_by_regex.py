import re

def evaluate_password(password):
    # 1. Base check: Must be strictly greater than 8 characters (9+ characters)
    if not re.match(r"^.{9,}$", password):
        return "Rejected: Password must be strictly greater than 8 characters."
    
    # 2. Score criteria tracking
    score = 0
    checks = {
        "Lowercase letter": r"[a-z]",
        "Uppercase letter": r"[A-Z]",
        "Number": r"[0-9]",
        "Special character": r"[!@#$%^&*(),.?\":{}|<>]"
    }
    
    # Check each regex pattern and add 1 point per match
    for name, pattern in checks.items():
        if re.search(pattern, password):
            score += 1
            
    # Extra point for an exceptionally strong, long password (e.g., 14+ characters)
    if len(password) >= 14:
        score += 1

    # 3. Determine the security level based on the score
    if score <= 2:
        return "Weak (Consider adding a mix of letters, numbers, and symbols)"
    elif score == 3:
        return "Medium (Good, but could be stronger with more character variety)"
    elif score >= 4:
        return "Strong (Excellent password security!)"

# Get user input
user_password = input("Enter your password to check: ")

# Evaluate and display result
result = evaluate_password(user_password)
print(f"\nSecurity Evaluation: {result}")
