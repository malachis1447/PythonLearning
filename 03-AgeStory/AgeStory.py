# AgeStory.py
# Kain M. Snyder
# Thu Aug 10th 2023 0238 MDT

# Tell a story about a character using variables to allow the story to be dynamic

#define variables

characterAge = str("22.52")
characterName = "Malachi"
characterIsMale = bool(True)
sideCharacterList = ["Jerry", "Brandon"]
CharacterA, CharacterB = sideCharacterList
# Main function, tells the story about the character from the above labeled variables

print("There once was a man named " + characterName + ".")
print("he was " + characterAge + " years old."),
print("He was friends with a coworker named " + CharacterA + ","),
print("and he has a cousin named " + CharacterB + "."),

print( CharacterA + " & " + CharacterB + " encouraged " + characterName + " to get back into Computer Programming." ),
print("This program is " + characterName + "'s program now that he's back."),
