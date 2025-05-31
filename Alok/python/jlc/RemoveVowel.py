def remove_vowel():
  vowels="aeiouAEIOU"
  myword =  input("Enter Word1 ")
  no_vowel=""
  no_vowel="".join(ch for ch in myword if ch not in vowels)
  print(no_vowel)

remove_vowel()
