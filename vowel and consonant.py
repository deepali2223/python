ch = str(input())
ch = ch.lower()
if ch >= 'a' and ch <= 'z':

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Vowel.")
    else:
        print("Consonant.")
else:    
    print("Not an alphabet.")
