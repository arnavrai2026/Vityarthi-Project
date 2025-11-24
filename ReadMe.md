Overview: 
This is a Python-based Password Strength Checker tool. It evaluates the strength of a 
user's password by checking its length and the inclusion of uppercase letters, lowercase 
letters, digits, and special characters. Based on these criteria, the password receives a 
score and a strength classification: Weak, Moderate, or Strong. 
Features: 
● Minimum password length check (at least 8 characters) 
● Checks for uppercase letters (A-Z) 
● Checks for lowercase letters (a-z) 
● Checks for digits (0-9) 
● Checks for special characters (punctuation) 
● Provides a numeric score and strength level based on the checks 
● Suggests improvements when the password is not strong 
● Logs password strength results using a pandas DataFrame
Requirements: 
● Python 3.x 
● numpy 
● pandas 
Usage: 
1. Run the script. 
2. Enter your password when prompted. 
3. View the password strength, score, and suggestions for improvement. 
4. See a log of the password strength evaluation.
Example: 
========PASSWORD STRENGTH CHECKER======== 
Enter your password: Example@123 
Password Strength: Strong 
Score: 5 / 5 
Password strength log: 
Password Score Level 
0 Example@123 5 Strong 
Thank you for using Password Strength Checker!