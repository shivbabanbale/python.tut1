Word=input("enter the any String  ")
vowels = "AaEeIiOoUu"

res = set([each for each in Word if each in vowels])
print("The vlowels present in the string:\n ",res)