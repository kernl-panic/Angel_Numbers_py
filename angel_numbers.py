# Angel Number Project version 1.0
# Reid Davis
# February 6, 2023

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
    
player = {'name': "", 'love_single': "", 'love_relationship': "", 'twinflame': "", 'career': "", 'spiritual': "", 'life': ""}







print("Welcome to my Angel Number Project!\nI made this tool for those who have been seeing certain numbers over and over again and might be curious as to what they mean.\n")

player_name = ""

player_name = input("First, may I have your name? ")

player['name'] = player_name

print("Hi, {pn}! Here's how this works:\nMaybe you've been seeing a certain number everywhere you look, like '1111' or '777'. These numbers hold a lot of significance in their meaning and can be used as guidance pertaining to certain areas of your life.\n\nThis program will tell you how the number you are seeing can be interpreted and hopefully offer some insight into what the Universe might be trying to tell you.\n\nTo give you the most relevant information, first I'll need to ask some questions about you.".format(pn=player_name))

skip_choice = ""

while skip_choice.lower() != 'yes' and skip_choice.lower() != 'y' and skip_choice.lower() != 'no' and skip_choice.lower() != 'n':
    skip_choice = input("If you would like to skip this part and get all information about the number, we can do that here.\nWould you like to skip the questions? (Yes/No) ")

if skip_choice.lower() == 'yes' or skip_choice.lower() == 'y':
    print("Okay! We'll give you all the information about your number.")
    relationship = 'both'
    player['twinflame'] = 'yes'
    player['career'] = 'yes'
    player['spiritual'] = 'yes'
    player['life'] = 'yes'

else:
    print("Fantastic! Here are some questions:\n")
    
    relationship = ""
    while relationship.lower() != 'yes' and relationship.lower() != 'y' and relationship.lower() != 'no' and relationship.lower() != 'n':
        relationship = input("Are you currently in a Relationship? (Yes/No) ")
        relationship = relationship.lower()

    
    while player['twinflame'].lower() != 'yes' and player['twinflame'].lower() != 'y' and player['twinflame'].lower() != 'no' and player['twinflame'].lower() != 'n':
        player['twinflame'] = input("Are you curious how this number relates to your Twin Flame? (Yes/No) ")
        player['twinflame'] = player['twinflame'].lower()
    
    
    while player['career'].lower() != 'yes' and player['career'].lower() != 'y' and player['career'].lower() != 'no' and player['career'].lower() != 'n':
        player['career'] = input("Would you like advice pertaining to your Career / Professional Life? (Yes/No) ")
        player['career'] = player['career'].lower()
    
    
    while player['spiritual'].lower() != 'yes' and player['spiritual'].lower() != 'y' and player['spiritual'].lower() != 'no' and player['spiritual'].lower() != 'n':
        player['spiritual'] = input("Would you like to know this number's meaning in regards to Spirituality? (Yes/No) ")
        player['spiritual'] = player['spiritual'].lower()
    
    
    while player['life'].lower() != 'yes' and player['life'].lower() != 'y' and player['life'].lower() != 'no' and player['life'].lower() != 'n':
        player['life'] = input("Do you wish to know what your number means regarding your Path in Life? (Yes/No) ")
        player['life'] = player['life'].lower()

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

angel_number = ""
letters = "abcdefghijklmnopqrstuvwxyz"

def are_all_same(number_string):
    counter = 0
    for num in number_string:
        if num == num[0]:
            pass
        else:
            counter += 1
    print("Counter: {}".format(counter))
    return counter == 0

while type(angel_number) == str:
    angel_number = input(("Perfect. Now just enter the number you wish to learn about and I'll tell you all about it: "))
    has_letter = False
    counter = 0
    for i in angel_number:
        if i in letters:
            counter += 1
        else:
            pass
    
    are_same = are_all_same(angel_number)
    
    if counter != 0 or are_same == False:
        pass
    else:
        angel_number = int(angel_number)

print(type(angel_number))
