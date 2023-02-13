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
one.meaning = """\nAngel number 111 is a sign you're headed toward a new beginning.\n\nWhen you see this number, it’s the universe, your guardian angels, or the higher power you believe in telling you that you’re on the right path toward manifesting your dreams and visions into reality, whether it’s a new career, relationship, or a fresh start in a new town.\n\nYou’re approaching a new era of spiritual awakening and enlightenment because you’re in tune with your inner, higher self."""
one.love_single = """\n111 can be a sign that a new or deeper love is coming.\n\nIf you’re single, it means that a new relationship will enter your life soon if you keep your eyes peeled for opportunities to meet and connect with people.\n\nRecognize that you deserve love, and accept it from others with enthusiasm. When you carry love in your heart, you’ll find it elsewhere."""
one.love_relationship = """\nIf you’re already in love, this number could mean you’ll get married or engaged soon, or, if you’re already married, enter a new era of harmony, tranquility, and peace together.\n\n111 asks you to reflect on the quality of your relationships.\n\nAsk yourself questions like 'Does my relationship make me feel the way I want to feel?' or 'Do I get that feeling sometimes or not at all?' It’s normal to experience a range of feelings in a healthy and solid relationship, but your connection should make you feel content, supported, and cared for overall.\n\nRelationships can get distorted and strained when one or both partners bring low vibrations or negative energy into the mix."""
one.twinflame = """\n111 means you’ll meet or strengthen your bond with your twin flame.\n\nA twin flame is another soul that mirrors your own—it could be a romantic partner or a platonic, dear friend.\n\nSeeing 111 could mean you’ll meet your twin flame soon if you haven’t found each other already, or that you’ll both soon experience a spiritual awakening together.\n\nConfide in each other and share your dreams for the future when you meet.\n\nWhen one of you works toward your spiritual purpose, the other will be inspired to do the same.\n\n111 is a strong number for twin flames. It’s a wonderful sign that you’re both about to experience something that will draw you closer together."""
one.career = """\nEmbrace your leadership skills and be a role model for others.\n\nUse all of the tools at your disposal—your creativity, special skills, and intuition—to take charge of your circumstances.\n\nThe angels are asking you to be a force for good, so reflect on the changes you want to see in the world and take action to fulfill your higher calling.\n\nEverything you’ve learned so far has been preparing you for leadership."""
one.spiritual = """\n111 is a sign to nurture your connection with your Higher Self.\n\nThis is the part of you that knows what’s best for you at all times and has a direct connection to the energies of the universe. Some call it your intuition—the inner voice that guides your most meaningful, positive decisions. Your higher self is what leads you to your life’s spiritual purpose.\n\nTake time to reflect on habits and beliefs that no longer serve your highest good. Clear them from your mind to make space for more exciting, fulfilling thoughts."""
one.life = """\nNumber 1 is a symbol of confidence and action.\n\nIt vibrates with the energy of deep self-understanding and the knowledge that you have the skills and wisdom you need to accomplish your goals and believe in yourself.\n\nWhen you encounter 1s (like seeing 1111, 111, or 11), it means you’re approaching a milestone and everything is in place for you to succeed if you believe you can.\n\nThe universe or your guardian angels are sending you 1s to support and encourage you as you move through life with confidence."""

two = Number()
two.meaning = """\n\n222 is one of the most calming messages\n\nAngel number 222 asks you to have hope, faith, and trust.\n\nIf you come across it, you might even feel like a sense of peace has washed over you already.\n\n222 also reassures, 'Everything will definitely balance out in your life!'\n\nIf you’ve felt down on your luck or a little lost, 222 will emerge like a beacon of light.\n\nThis brilliant angel number wants to relay the message that you’ve got all the right tools—smarts, guts, and perseverance!\n\nStay hopeful! With all that on your side, you’ll be alright."""
two.love_single = """\nIf you’re single, 222 hints that a new love interest will show up.\n\nWhen you find yourself a little lonely or you just crave companionship, 222 often makes an appearance.\n\nMake sure to put your best foot forward and keep your head up high!\n\nYou’ll want to shine when you run into that attractive stranger who might just change your life."""
two.love_relationship = """\nFor long-term relationships, 222 reminds you to invest effort in love.\n\nIf you or your partner are at risk for taking the other for granted, your guardian angels will kick into gear.\n\nThey’ll send off a 222 as a rallying cry for you to make sparks fly in your romance again.\n\nMake sure to prioritize quality time—setting up an ongoing date night is a good start!"""
two.twinflame = """\n222 declares you’ll find a twin flame who will bring romantic bliss.\n\nMost of the time, a twin flame can be hot and heavy or seriously stormy. When 222 crops up, though, you can expect a way tamer twin flame connection.\n\nYou’ll still learn a lot from your twin flame, but your love affair will be a slow burn that you really savor.\n\nIn fact, it’ll probably feel like the fairy tale you’ve always been waiting for."""
two.career = """\nAngels can also send 222 to tell you that hard work really pays off.\n\n222 is also a special “congratulations!” for all the ways you’ve committed to a project or calling.\n\nWhether you’re a full-time student, a model employee, or a doting parent, 222 symbolizes that your angels are praising you.\n\nYou’ve really struck the right balance and made all the right decisions. All your discipline and determination has been noticed, and you’ll be richly rewarded for it.\n\nDual 22 also signifies large-scale ventures which could be lucrative and may depend on the public for success through hard work."""
two.spiritual = """\n222 provides hope and spiritual growth. If you’ve been curious about prayer, meditation, or any other metaphysical journey, 222 is a divine nudge.\n\nYour angels are excited by your new direction, and they’re hinting that there’s so much in store for you when you take your next step.\n\nStay optimistic and remember that the best is yet to come!\n\nIf you’ve endured one obstacle after the other and have reached out for a sign, 222 is meant to recharge your faith. 222 is a gentle reminder that you’ll find harmony. When life feels like it’s fallen apart or your heart is broken, The Universe will help you put the pieces back together."""
two.life = """\n222 announces that it’s time to make a clear list of life goals.\n\nWhen you are frazzled about what to do or have a ton of ideas to sift through, 222 invites you to slow down.\n\nSit down at your desk and take a deep breath. Then, concentrate on what you really want to accomplish.\n\nFor example, maybe you want to improve your physical health.\n\nTake out a pen and paper, then write down all the specific steps that will help you manifest your ideal future."""

three = Number()
three.meaning = """"""
three.love_single = """"""
three.twinflame = """"""
three.career = """"""
three.spiritual = """"""
three.life = """"""

four = Number()
four.meaning = """"""
four.love_single = """"""
four.twinflame = """"""
four.career = """"""
four.spiritual = """"""
four.life = """"""

five = Number()
five.meaning = """"""
five.love_single = """"""
five.twinflame = """"""
five.career = """"""
five.spiritual = """"""
five.life = """"""

six = Number()
six.meaning = """"""
six.love_single = """"""
six.twinflame = """"""
six.career = """"""
six.spiritual = """"""
six.life = """"""

seven = Number()
seven.meaning = """"""
seven.love_single = """"""
seven.twinflame = """"""
seven.career = """"""
seven.spiritual = """"""
seven.life = """"""

eight = Number()
eight.meaning = """"""
eight.love_single = """"""
eight.twinflame = """"""
eight.career = """"""
eight.spiritual = """"""
eight.life = """"""

nine = Number()
nine.meaning = """"""
nine.love_single = """"""
nine.twinflame = """"""
nine.career = """"""
nine.spiritual = """"""
nine.life = """"""
    

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

print("\n----------------------------------------------------------------------------")

while player_name == "":
    player_name = input("\nFirst, may I have your name?\n")

player['name'] = player_name

print("\n----------------------------------------------------------------------------")
print("\nHi, {name_first}{name_rest}! Here's how this works:\n\nMaybe you've been seeing a certain number everywhere you look, like '1111' or '777'.".format(name_first=player_name[0].upper(), name_rest=player_name[1:]))
print("These numbers hold a lot of significance in their meaning and can be used as guidance pertaining to certain areas of your life.\n")

print("Press any key to continue...")
wait()

print("\n----------------------------------------------------------------------------")
print("\nThis program will tell you how the number you are seeing can be interpreted and hopefully offer some insight into what the Universe might be trying to tell you.")
print("To give you the most relevant information, first I'll need to ask some questions about you.\n")

print("Press any key to continue...")
wait()

# Below: Takes input and keeps asking for input until the requirements are met - Either 'yes' - 'y' - 'no' - 'n'
# The relationship variable must be separate because if Player skips questions, it must be set to 'both' so we can set two keys using one variable later on
# The rest are iterated over in a for loop to set their corresponding 'player' keys - We can't do this with relationship having to change two keys

skip_choice = ""
print("\n----------------------------------------------------------------------------")

while skip_choice.lower() != 'yes' and skip_choice.lower() != 'y' and skip_choice.lower() != 'no' and skip_choice.lower() != 'n':
    skip_choice = input("\nIf you would like to skip this part and get all information about the number, we can do that here.\n\nWould you like to skip the questions? (Yes/No) ")

if skip_choice.lower() == 'yes' or skip_choice.lower() == 'y':
    print("\n----------------------------------------------------------------------------")
    print("\nOkay! We'll give you all the information about your number.")
    relationship = 'both'
    player['twinflame'] = 'yes'
    player['career'] = 'yes'
    player['spiritual'] = 'yes'
    player['life'] = 'yes'

else:
    print("\n----------------------------------------------------------------------------")
    print("\nFantastic! Here are some questions:")
    
    relationship = ""
    while relationship.lower() != 'yes' and relationship.lower() != 'y' and relationship.lower() != 'no' and relationship.lower() != 'n':
        relationship = input("\nAre you currently in a Relationship? (Yes/No) ")
        relationship = relationship.lower()

    print("\n----------------------------------------------------------------------------")
    while player['twinflame'].lower() != 'yes' and player['twinflame'].lower() != 'y' and player['twinflame'].lower() != 'no' and player['twinflame'].lower() != 'n':
        player['twinflame'] = input("\nAre you curious how this number relates to your Twin Flame? (Yes/No) ")
        player['twinflame'] = player['twinflame'].lower()
    
    print("\n----------------------------------------------------------------------------")
    while player['career'].lower() != 'yes' and player['career'].lower() != 'y' and player['career'].lower() != 'no' and player['career'].lower() != 'n':
        player['career'] = input("\nWould you like advice pertaining to your Career / Professional Life? (Yes/No) ")
        player['career'] = player['career'].lower()
    
    print("\n----------------------------------------------------------------------------")
    while player['spiritual'].lower() != 'yes' and player['spiritual'].lower() != 'y' and player['spiritual'].lower() != 'no' and player['spiritual'].lower() != 'n':
        player['spiritual'] = input("\nWould you like to know this number's meaning in regards to Spirituality? (Yes/No) ")
        player['spiritual'] = player['spiritual'].lower()
    
    print("\n----------------------------------------------------------------------------")
    while player['life'].lower() != 'yes' and player['life'].lower() != 'y' and player['life'].lower() != 'no' and player['life'].lower() != 'n':
        player['life'] = input("\nDo you wish to know what your number means regarding your Path in Life? (Yes/No) ")
        player['life'] = player['life'].lower()
    
    print("\n----------------------------------------------------------------------------")
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
    
    angel_number = ""
    print("\n----------------------------------------------------------------------------")
    # Angel_number is currently a string. Sets has_letter initially to False and counter to zero.
    
    angel_number = input(("\nNow just enter the number you wish to learn about and I'll tell you all about it:\n"))

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
    # Also now checks if Player entered no input and does not continue until data is entered
    if counter != 0 or angel_number == "" or are_all_same(angel_number) == False:
        pass
    else:
        break

print("\n----------------------------------------------------------------------------")
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

print("\n----------------------------------------------------------------------------")
print("\n\nHere's the general overview:\n")
print(angel_number.meaning)
print("\nPress any key to continue...")
wait()

if player['love_single'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nIf you are currently single: \n")
    print(angel_number.love_single)
    print("\nPress any key to continue...")
    wait()
if player['love_relationship'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nIf you are currently in a Relationship: \n")
    print(angel_number.love_relationship)
    print("\nPress any key to continue...")
    wait()
if player['twinflame'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nTwinflame: \n")
    print(angel_number.twinflame)
    print("\nPress any key to continue...")
    wait()
if player['career'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nProfessional Life / Career: \n")
    print(angel_number.career)
    print("\nPress any key to continue...")
    wait()
if player['spiritual'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nSpiritual signifance: \n")
    print(angel_number.spiritual)
    print("\nPress any key to continue...")
    wait()
if player['life'] == True:
    print("\n----------------------------------------------------------------------------")
    print("\n\nYour Path in Life: \n")
    print(angel_number.life)
    print("\nPress any key to continue...")
    wait()

print("\n----------------------------------------------------------------------------")
print("\nThere you have it!\n\nI hope this program was able to shed some light on how the Universe may be trying to communnicate with you.")
print("\nIf you would like to see a different number, feel free to run the Program again\n")
print("\nThanks for using my fun little program!")
print("\nExit...")
wait()