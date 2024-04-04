str=input("enter string:")
str=str.lower()
vowels="aeiou"
consonants="bcdfghjklmnpqrstuvwxyz"
vowel_dict=dict.fromkeys(vowels,0)
consonant_dict=dict.fromkeys(consonants,0)
for char in str:
    if char in vowels:
        vowel_dict[char]+=1
    else:
        consonant_dict[char]+=1
print("vowel count:",vowel_dict)
print("consonant count:",consonant_dict)
