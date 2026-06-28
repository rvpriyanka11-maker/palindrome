# Simple Palindrome Checker in Python

def is_palindrome(word):
    # Convert to lowercase for consistency
    word = word.lower()
    # Compare word with its reverse
    return word == word[::-1]

# Example usage
test_word = input("Enter a word: ")
if is_palindrome(test_word):
    print(f"✅ '{test_word}' is a palindrome!")
else:
    print(f"❌ '{test_word}' is not a palindrome.")
