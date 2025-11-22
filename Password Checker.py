import string
import numpy as np
import pandas as pd

print("\n PASSWORD STRENGTH CHECKER \n")

def check_len(password):
    return len(password) >= 8

def check_char_type(password):
    A_upper = any(ch.isupper() for ch in password)
    A_lower = any(ch.islower() for ch in password)
    A_digit = any(ch.isdigit() for ch in password)
    A_symbol = any(ch in string.punctuation for ch in password)
    return A_upper, A_lower, A_digit, A_symbol

def calculate_strength(password):
    score_components = np.array([check_len(password),
                                *check_char_type(password)], dtype=int)

    score = np.sum(score_components)
    if score <= 2:
        level = "Weak"
    elif score in [3, 4]:
        level = "Moderate"
    else:
        level = "Strong"

    return score, level

def show_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not any(ch.isupper() for ch in password):
        suggestions.append("Add an uppercase letter (A-Z)")
    if not any(ch.islower() for ch in password):
        suggestions.append("Add a lowercase letter (a-z)")
    if not any(ch.isdigit() for ch in password):
        suggestions.append("Add a number (0-9)")
    if not any(ch in string.punctuation for ch in password):
        suggestions.append("Add a special character (e.g., @, #, $, %, !)")

    return suggestions

password = input("Enter your password: ")

score, level = calculate_strength(password)

print("\nPassword Strength:", level)
print("Score:", score, "/ 5")

if level != "Strong":
    print("\nSuggestions to improve your password:")
    tips = show_suggestions(password)
    for t in tips:
        print(t)

password_log = pd.DataFrame({
    "Password": [password],
    "Score": [score],
    "Level": [level]
})

print("\nPassword strength log:")
print(password_log)

print("\nThank you for using Password Strength Checker!")