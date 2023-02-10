# Angel Number Project version 1.0
# Reid Davis
# February 6, 2023

import msvcrt as m

def wait():
    m.getch()



class Number:
    def __init__(self):
        self.meaning = ""
        self.love_single = ""
        self.love_relationship = ""
        self.twinflame = ""
        self.career = ""
        self.spiritual = ""
        self.life = ""
    
    def __repr__(self):
        return self.meaning


# Each number is an object of the Number Class that has it's own meaning for love, twinflame, career, spiritual, life, and general explanation
# Later on, after the user input section is done, we will take the players number and associate it with one of these Classes
# Example: If player enters "11" their number will become 'one' - If player enters "777777" their number will become 'seven'

# Going to make the numbers 111 - 222 - 333 and so on...Instead of 1 - 2 - 3 - 4
one = Number()
one.meaning = """In numerology, the number 1 reflects new beginnings, power, and action.\nA huge reason why you might be seeing angel number 1 is that your guardian angels want you to focus on the present.\nUnfortunately, many of us will get distracted by worries about the past or future.\nWe may find ourselves ruminating over things that went wrong, or worrying about what the future holds for us.\nThis ultimately causes us to feel stuck and useless. We can’t change the past, and we don’t know what will happen in the future, so we must try to concentrate on the here and now.\n\nMeditation and mindfulness are great ways to focus on the here and now.\nBy grounding yourself and paying attention to your current moods and sensations, you are able to find comfort and solace in the moment."""
one.love_single = "The angel number 1 also has clear messages regarding your love life. Generally, this number reflects new beginnings and action.\nIf you are single, your guardian angels are telling you that it is time to leave the past in the past and embrace the next phase of your romantic life. Broken hearts and old relationships that did not go well are still affecting your approach to love, and this is ultimately holding you back from happiness.\n\nIt is time to reflect on where you are and where you wish to be regarding love. What do you want from a partner, and what do you need to let go of?\n"
one.love_relationship = "If you are in a relationship, the angel number 1 beckons in the next phase of love for you and your partner.\nThis may be moving in together or getting married. Or, it may simply be the words ‘I love you’! Whatever it is, it will be an exciting time for you and your partner"
one.twinflame = """If you haven’t met your twin flame yet, the angel number 1 is telling you that it is time to focus on yourself first.\nOf course, we all want to meet our twin flame, but we really need to be in the best place spiritually in order to do so.\nAs twin flames and spirituality go hand in hand, we must explore our spiritual side before meeting our other half.\nWith angel number 1, you are going through a time of change and personal growth.\nTake time to embrace this, paying attention to your goals and dreams. You will meet your twin flame when the time is right\n\nIf you know who your twin flame is, angel number 1 signifies the next stage of your relationship.\nA twin flame relationship has 8 distinct stages, and all of them are equally important.\nThe next stage is just around the corner for you and your twin flame, so go with the flow and learn from this adventure!"""
one.career = """The number 1 serves as a reminder of your own personal power.\nSeeing this angel number may be a push from your angels to manifest your goals and be proactive when it comes to the next phase of your life.\nYou have the power within you to create your own reality.\nSeeing the angel number 1 is a sign of energy and power, so it may be time to work with the Law of Attraction and manifest your dreams!"""
one.spiritual = """If you are seeing this number a lot, your guardian angels want you to experience new ideas regarding spirituality.\nThe angel number 1 is often seen as a wake-up call in regard to spirituality.\nIt asks you to put faith in the universe and embrace your spiritual side.\nNumber 1 is a number of new beginnings, and this can be reflected in your approach to your spirituality\nIt is time to explore your spiritual side in an open-minded way"""
one.life = """The Angel number 1 is also a message of encouragement from our guardian angels\nThey want you to know that you are on the right path in life, and you should keep on doing what you are doing\nYou have a strong sense of self, and you must listen to your intuition for guidance\nYou are making the right choices in order to move forward on your true path in life, even if you feel as if you are going in circles sometimes\nLife is full of ups and downs, but ultimately, you will get to where you dream to be.\nYou are moving in the right direction, so keep doing what you are doing\n\nThe angel number 1 also reflects new beginnings, and so a reason why you might be seeing it is because you are at the beginning of a new adventure\nIf you are seeing the angel number 1 a lot, it may be because one chapter of your life is coming to a close, with another one beginning.\nThis is an exciting time, although it might be a bit scary\nThis new phase of your life will be so rewarding! You will discover new aspects of yourself and hidden depths of your soul.\nIt will be a time of self-exploration and personal development, so keep moving forward and doing what you are doing"""

two = Number()
two.meaning = ""
two.love_single = ""
two.twinflame = ""
two.career = ""
two.spiritual = ""
two.life = ""

three = Number()
three.meaning = ""
three.love_single = ""
three.twinflame = ""
three.career = ""
three.spiritual = ""
three.life = ""

four = Number()
four.meaning = ""
four.love_single = ""
four.twinflame = ""
four.career = ""
four.spiritual = ""
four.life = ""

five = Number()
five.meaning = ""
five.love_single = ""
five.twinflame = ""
five.career = ""
five.spiritual = ""
five.life = ""

six = Number()
six.meaning = ""
six.love_single = ""
six.twinflame = ""
six.career = ""
six.spiritual = ""
six.life = ""

seven = Number()
seven.meaning = ""
seven.love_single = ""
seven.twinflame = ""
seven.career = ""
seven.spiritual = ""
seven.life = ""

eight = Number()
eight.meaning = ""
eight.love_single = ""
eight.twinflame = ""
eight.career = ""
eight.spiritual = ""
eight.life = ""

nine = Number()
nine.meaning = ""
nine.love_single = ""
nine.twinflame = ""
nine.career = ""
nine.spiritual = ""
nine.life = ""
    

# player is a Dictionary that will hold values based on their answers to the questions
# Then based on the values, we will output specific traits of the number
# If "career" is False, we will not output the numbers self.career
# If twinflame is True, we will output the information in self.twinflame
# If player skipped questions and wants all information, all values will be True and we will output all attributes

player = {'name': "", 'love_single': "", 'love_relationship': "", 'twinflame': "", 'career': "", 'spiritual': "", 'life': ""}

# Beginning of Program

print("\nWelcome to my Angel Number Project!\n\nI made this tool for those who have been seeing certain numbers over and over again and might be curious as to what they mean.\n")

print("Press any key to continue...")
wait()

player_name = ""

while player_name == "":
    player_name = input("\nFirst, may I have your name?\n")

player['name'] = player_name

print("\nHi, {name_first}{name_rest}! Here's how this works:\n\nMaybe you've been seeing a certain number everywhere you look, like '1111' or '777'.".format(name_first=player_name[0].upper(), name_rest=player_name[1:]))
print("These numbers hold a lot of significance in their meaning and can be used as guidance pertaining to certain areas of your life.\n")

print("Press any key to continue...")
wait()

print("\nThis program will tell you how the number you are seeing can be interpreted and hopefully offer some insight into what the Universe might be trying to tell you.")
print("To give you the most relevant information, first I'll need to ask some questions about you.\n")

print("Press any key to continue...")
wait()

# Below: Takes input and keeps asking for input until the requirements are met - Either 'yes' - 'y' - 'no' - 'n'
# The relationship variable must be separate because if Player skips questions, it must be set to 'both' so we can set two keys using one variable later on
# The rest are iterated over in a for loop to set their corresponding 'player' keys - We can't do this with relationship having to change two keys

skip_choice = ""

while skip_choice.lower() != 'yes' and skip_choice.lower() != 'y' and skip_choice.lower() != 'no' and skip_choice.lower() != 'n':
    skip_choice = input("\nIf you would like to skip this part and get all information about the number, we can do that here.\n\nWould you like to skip the questions? (Yes/No) ")

if skip_choice.lower() == 'yes' or skip_choice.lower() == 'y':
    print("\nOkay! We'll give you all the information about your number.")
    relationship = 'both'
    player['twinflame'] = 'yes'
    player['career'] = 'yes'
    player['spiritual'] = 'yes'
    player['life'] = 'yes'

else:
    print("\nFantastic! Here are some questions:\n")
    
    relationship = ""
    while relationship.lower() != 'yes' and relationship.lower() != 'y' and relationship.lower() != 'no' and relationship.lower() != 'n':
        relationship = input("Are you currently in a Relationship? (Yes/No) ")
        relationship = relationship.lower()

    
    while player['twinflame'].lower() != 'yes' and player['twinflame'].lower() != 'y' and player['twinflame'].lower() != 'no' and player['twinflame'].lower() != 'n':
        player['twinflame'] = input("\nAre you curious how this number relates to your Twin Flame? (Yes/No) ")
        player['twinflame'] = player['twinflame'].lower()
    
    
    while player['career'].lower() != 'yes' and player['career'].lower() != 'y' and player['career'].lower() != 'no' and player['career'].lower() != 'n':
        player['career'] = input("\nWould you like advice pertaining to your Career / Professional Life? (Yes/No) ")
        player['career'] = player['career'].lower()
    
    
    while player['spiritual'].lower() != 'yes' and player['spiritual'].lower() != 'y' and player['spiritual'].lower() != 'no' and player['spiritual'].lower() != 'n':
        player['spiritual'] = input("\nWould you like to know this number's meaning in regards to Spirituality? (Yes/No) ")
        player['spiritual'] = player['spiritual'].lower()
    
    
    while player['life'].lower() != 'yes' and player['life'].lower() != 'y' and player['life'].lower() != 'no' and player['life'].lower() != 'n':
        player['life'] = input("\nDo you wish to know what your number means regarding your Path in Life? (Yes/No) ")
        player['life'] = player['life'].lower()
    
    print("\nPerfect! That's all I need.")

# As stated above, everything else is checked in a for loop
# Relationship must be checked separately because it is the only one that can have the value 'both' instead of 'yes'/'y' and 'no'/'n' (Which is what determines the corresponding keys in player)
# Since the above loops/inputs set the player keys to either 'yes'/'y' or 'no'/'n' (except for relationship) - Here we change the key to True if 'yes' and False if 'no'

if relationship == 'both':
    player['love_single'] = True
    player['love_relationship'] = True
elif relationship.lower() == 'yes' or relationship.lower() == 'y':
    player['love_relationship'] = True
    player['love_single'] = False
elif relationship.lower() == 'no' or relationship.lower() == 'n':
    player['love_relationship'] = False
    player['love_single'] = True

for i in player:
    if player[i] == 'yes' or player[i] == 'y':
        player[i] = True
    elif player[i] == 'no' or player[i] == 'n':
        player[i] = False
    else:
        pass

print("\nPress any key to continue...")
wait()

# Angel number must be initialized as a string so we can check it's value in the while loop below
# 'letters' is used to check if any individual item in the player's input is a letter instead of a number

angel_number = ""
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Working! - are_all_same() attempts to check the player's input to see if all numbers are the same (1111) and not one is different (1112)
# If the string is equal to: The first letter of the string times however long the string is - All characters are the same

def are_all_same(number_string):
    if number_string == len(number_string) * number_string[0]:
        return True
    else:
        return False




# If counter is not zero, it passes, so the while loop keeps prompting until all items are numbers
# If ALL characters input are numbers, the loop is broken and player's input is stored in angel_number

while True:
    
    angel_number = input(("\nNow just enter the number you wish to learn about and I'll tell you all about it:\n"))
    
    # Angel_number is currently a string. Sets has_letter initially to False and counter to zero.
    
    has_letter = False
    counter = 0
    
    # Checks each "letter" in angel_number against the list of letters.
    # If any are a letter instead of number counter will not be zero
    for i in angel_number:
        if i in letters:
            counter += 1
        else:
            pass
    
    # If all characters are not a letter + All numbers in the string are the same number - The while loop is broken and input is accepted
    if counter != 0 or are_all_same(angel_number) == False:
        pass
    else:
        break

print("\nBased on your answers to the questions, I'll tell you what your number means")
print("\nIf you opted to skip the questions, you'll just see everything!")
print("\nPress any key to continue...")
wait()


# Based on the number Player selected, angel_number will be assigned to one of our number Classes, which contains the meaning attributes
# Since our previous function checks to make sure all numbers entered are indentical, all we have to do is check for a single number

if '1' in angel_number:
    angel_number = one
elif '2' in angel_number:
    angel_number = two
elif '3' in angel_number:
    angel_number = three
elif '4' in angel_number:
    angel_number = four
elif '5' in angel_number:
    angel_number  = five
elif '6' in angel_number:
    angel_number = six
elif '7' in angel_number:
    angel_number = seven
elif '8' in angel_number:
    angel_number = eight
elif '9' in angel_number:
    angel_number = nine


# Now that angel_number has been assigned to the correct number Class, this prints out the different attributes based on the Player's answers (dictionary keys)

print("\n\nHere's the general overview:\n")
print(angel_number.meaning)
print("\nPress any key to continue...")
wait()

if player['love_single'] == True:
    print("\n\nIf you are currently single: \n")
    print(angel_number.love_single)
    print("\nPress any key to continue...")
    wait()
if player['love_relationship'] == True:
    print("\n\nIf you are currently in a Relationship: \n")
    print(angel_number.love_relationship)
    print("\nPress any key to continue...")
    wait()
if player['twinflame'] == True:
    print("\n\nTwinflame meaning: \n")
    print(angel_number.twinflame)
    print("\nPress any key to continue...")
    wait()
if player['career'] == True:
    print("\n\nHere's some guidance related to your Professional Life / Career: \n")
    print(angel_number.career)
    print("\nPress any key to continue...")
    wait()
if player['spiritual'] == True:
    print("\n\nThis number's Spiritual signifance: \n")
    print(angel_number.spiritual)
    print("\nPress any key to continue...")
    wait()
if player['life'] == True:
    print("\n\nRegarding your Path in Life: \n")
    print(angel_number.life)
    print("\nPress any key to continue...")
    wait()