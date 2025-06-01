def is_palindrome(word):
    word = word.lower()  
    return word == word[::-1]

kelime = input("Bir kelime girin: ")

if is_palindrome(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")
