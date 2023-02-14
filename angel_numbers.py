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

three.meaning = """\nRemember that life is a balance of work and play. If you’re seeing 333 everywhere, it’s a nudge from your angels to “live, laugh, and love.”\n\nLife is not only about the destination, but the journey: enjoy it!\n\nIn fact, your ability to relax and play may help propel you forward.\n\nAnxiety about following the right path does not accelerate our growth nearly as much as creativity and the opportunity to experiment."""

three.love_single = """\n333 is a sign that your love life will flourish.\n\nIf you are currently single, a great romance could be on its way.\n\nRelax and be yourself, and your soulmate will find you.\n\nAlthough 333 is a good omen for your love life, don’t become too distracted from your independence.\n\nYou have a purpose outside of your relationships: honor that purpose."""

three.love_relationship = """\n333 is a sign that your love life will flourish.\n\nIf you are in a relationship, 333 could indicate you have found your soulmate.\n\nBy practicing vulnerability, embracing your playful side, and letting your hair loose, you will cultivate intimacy with your partner.\n\nAlthough 333 is a good omen for your love life, don’t become too distracted from your independence.\n\nYou have a purpose outside of your relationships: honor that purpose."""

three.twinflame = """\nIf you see 333, your twin flame may be close by.\n\nBy being yourself and working to manifest positivity, you’re bound to attract your twin flame.\n\nBut let it happen naturally: you can’t force an interaction with your twin flame (or your soulmate, for that matter).\n\nBe yourself, and do good work, and the angels will guide your twin flame to you.\n\nRemember that while your twin flame and your soulmate could be the same person, they do not have to be."""

three.career = """\n333 is a sign you have the power to achieve financial success.\n\nIf you’re feeling financially discouraged right now, take heart: angel number 333 is a sign you are not meant to struggle forever.\n\nBy being who you are, remaining positive, and keeping yourself open to new and unexpected opportunities, you will achieve financial security—you may even thrive.\n\nThe 3 in multiples usually says finances are unifying and coming together in a positive way.\n\nIf you are working towards a promotion at work, keep pushing forward with confidence: your angels have your back.\n\nIf you’re looking for a new source of income, don’t lose hope. Keep up your optimistic attitude, and an opportunity will present itself.\n\nDon’t be afraid to take it when it does."""

three.spiritual = """\nThe number 3 represents the Holy Trinity. When you see this number tripled, it is a reminder that you, too, are a blend of the physical and the spiritual, the earthly and the heavenly.\n\n333 is a reminder to embrace your status as a divine creature, a holy collaboration of flesh, mind, and spirit.\n\nYou exist in the physical and external, and in the spiritual and internal.\n\nYou are a holy being, so do not be distracted by the physical world.\n\n333 is a message from your guardian angels that you must dedicate time to cultivating your spiritual identity.\n\nSet aside time for daily meditation or prayer. In time, you will develop a strong spiritual identity."""

three.life = """\n3 is a sign of positivity, self-expression, and independence.\n\nYou are one-of-a-kind, and you can’t hide it even if you want to.\n\nBut the shadow side of these attributes is self-doubt: when you embrace your unique self, it can be easy to feel directionless.\n\nThe only way out of self-doubt is through it: the more you practice dancing to the beat of your own drum, the more certain of yourself and of your path you will become.\n\nWhile it may be tempting to follow the paths others take, 3 is a sign from your angels that you can’t fake your way through life.\n\nIt may seem like the easier path at first, but you can’t do it forever: it’s far more freeing to embrace your true self."""




four = Number()

four.meaning = """\nThe number 4 symbolizes “the worker."\n\nThe worker is a focused, no-nonsense laborer who relies on tried-and-true methods to achieve success.\n\nThis number is a symbol of your great potential, including the potential to rise above and fight through any obstacles that fall in your path.\n\nIf you're seeing the number 4, it's a sign to duck your head and keep moving forward the best way you know how: you're on the right path, you just need to keep going.\n\nWhen you see multiple 4s in a row, it’s a sign to multiply your energy: devote extra attention to the things you really value, such as your family and friends, your career, or your love life.\n\n444 is also a signal that there are important relationships to develop.\n\nThese relationships are not limited to romance: they can be platonic or professional as well.\n\nKeep an open heart during this time, and you may make some of the most meaningful connections of your life.\n\nIt could also be a nudge to develop the relationships you already have.\n\nMaybe you’ll grow closer to a friend you lost touch with, or maybe you’ll get to know the people you see every day.\n\nYour mail carrier, your barista, or the woman who walks her dog at the same time as you."""

four.love_single = """\nIf you’re single, 444 could be a sign that a romance is close by.\n\nIt could be a signal from your guardian angels that it will soon be time to build a connection with a new partner.\n\nBeing prepared will help you recognize your partner when you meet them and build a strong foundation with them.\n\nBelieve in yourself and your worth, and keep your eyes open: you could meet your future partner any moment.\n\nMaybe you already have!"""

four.love_relationship = """\nIn relationships, 444 is all about structure.\n\nIf you’re in a romantic relationship, or if you’ve found your twin flame, 444 could be a sign your connection is built to last.\n\nIf your relationship is tense or unhappy, it could be a sign to assess your relationship’s foundations: is it strong enough to stand the test of time?\n\nEven if your relationship is going well, don’t stop working on it: relationships take patience and effort if they are to be successful.\n\nThe number 444 is a reminder to keep building towards a strong future with your partner by practicing mutual respect and honesty."""

four.twinflame = """\nRemember that twin flames are not necessarily romantic partners, but they could be.\n\nTwin flames are two halves of one soul: while you may have many soulmates in your life, you only have one twin flame."""

four.career = """\n444 means your career is going according to the divine plan. You just have to dig in and work.\n\nAs aforementioned, the number 4 symbolizes “the worker,” and work is just what you have to do right now.\n\nYour angels know the ultimate plan for you and your career, and if you’re seeing the number 444, it’s a sign from your angels that you’re on the right track: you just have to work hard and keep pressing on.\n\n444 is a sign that you need to get down to brass tacks to achieve your dreams. But don’t be intimidated. 444 means your angels are cheering you on. They believe in you.\n\n444 could also be a sign that something huge is on the horizon.\n\nMaybe a promotion, or a new opportunity. Whatever is coming, you just have to be ready to meet it.\n\nYour angels are trying to ready you for the big things ahead.\n\nBe available to their guidance and their support, and you’ll be just fine.\n\nIf you’ve been considering taking any professional chances, such as changing careers or investing money in a risky endeavor, 444 could be a sign that you have your angels’ blessing.\n\nIt might not just be that something big is coming: 444 might be a sign you will need to act when it does come.\n\nFor better or worse, how will you meet big change?"""

four.spiritual = """\nAngel number 444 is a sign that you are on the right path.\n\nYour guardian angels are surrounding you at this time, and they are cheering you on.\n\nIf you’re seeing 444 everywhere you look, it’s a sign the universe’s divine plan is in motion.\n\nYou just have to trust your intuition and keep forging ahead, and everything will work out.\n\nAngel number 444 is a reminder to rely on your inner wisdom: you are stronger and more capable than you may realize!\n\nWhen you see 444, it means that now is the time to practice manifesting the life you’ve always dreamed of: it’s within your reach."""

four.life = """\nThe number 444 is a sign you need to lean into your abilities to shape your future.\n\nDon’t sit back and let life pass by: take charge, and understand your own potential to facilitate great change.\n\n444 is a sign that you’re on the path you’re meant to be on—you just need to persevere, even if it feels hard or scary or like you’re not doing the right thing.\n\nIf you see 444 everywhere you turn, it’s a sign your angels are watching you take risks and maybe even fail at some of them, but they’re on your side. You’re not alone.\n\nWhen you want to take a chance but you feel doubt creeping in, remember your angels are standing guard.\n\nNext time you see 444, ask yourself: what risk should I be taking right now? What am I afraid of trying next? How can I push myself to reach my goal today?\n\nYour angels have your back."""




five = Number()

five.meaning = """\n5 is a symbol not only of change, but of health, vitality, and balance.\n\nThe only constant, as they say, is change. Therefore, don’t view change as a disruption to your life, but as an integral part of it.\n\nCycles and transformation are part of the natural order of things. The divine plan moves on a turning wheel.\n\nWhen tripled, 5 indicates an intense need for change and balance. It's time for the pendulum to swing in the other direction.\n\nThe number 5 also indicates curiosity and a penchant for exploration. It is a number full of possibilities and potential.\n\nIf you see the number 5 everywhere you look, it indicates you’re in need of some excitement. Now is the time to try new things and to experiment.\n\nIf you have been experiencing any self-doubt lately, consider 555 a sign to trust yourself. Your angels know you're capable of whatever you set your mind to.\n\nIf you've been craving a change in the day-to-day, now may be the time to go after some excitement."""

five.love_single = """\nIf you want to find romance, 555 is a sign to take a chance.\n\nIf you are single and want to be in a relationship, put yourself out there: ask out your crush, or strike up a conversation with an interesting or attractive stranger.\n\n555 is about practicing vulnerability and being yourself. Your angels are pushing you to recognize your worth, whether single or not.\n\n555 is a reminder to seize the day. Change doesn’t just happen: you must embrace it when it comes to you—or better yet, make it happen yourself."""

five.love_relationship = """\nIn romance, 555 is a nudge to show your partner more love.\n\nWhen you see the angel number 555, take it as a reminder to show your partner more love and tenderness at this time.\n\nYou may be craving attention and adoration yourself, but 555 is about taking action and being vulnerable: by giving more attention to your partner, you will receive the adoration you long for in return.\n\n5 represents the ultimate balance that comes from knowing when to move and when to be still: as the tide ebbs and flows, you cannot sit still forever and expect transformation to occur. 555 means it is your turn to move.\n\nPractice good communication with your partner to promote peace and harmony.\n\nAngel number 555 is a sign to be open in your relationship. Don’t wait for peace: make it happen."""

five.twinflame = """\nIn twin flame relationships, 555 is a sign to keep moving forward.\n\nIf you have found your twin flame, angel number 555 means progress and happiness are ahead—especially if you have recently endured tumultuous times in your relationship.\n\nThe hard work you have put into your relationship hasn’t been for naught.\n\nThe journey you share with your twin flame is going according to plan, just keep moving.\n\nYou and your twin flame can breathe easy: 555 is a blessing for you. But don’t take this peace for granted.\n\nContinue to tend to your twin flame relationship to make sure it remains strong.\n\nBecause your twin flame mirrors you, you can’t get away with anything less than radical honesty.\n\n555 is a reminder to be open with yourself and your twin flame in order to cultivate a strong relationship.\n\nRemember that your relationship with your twin flame is not necessarily romantic, though it can be.\n\nTwin flames are two people who share the same soul and therefore mirror one another, whereas soulmates are two people whose souls are very compatible."""

five.career = """\nAngel number 555 indicates changes in your career.\n\n555 is a push from your angels to consider your current professional status: are you where you’re meant to be? Do you enjoy the work you’re doing?\n\nIf the answer is no, it’s time to take steps in the right direction. Explore new job opportunities, and connect with professionals in other disciplines to see what doors may be open to you.\n\nIf the answer is yes, it’s time to reach for more. Maybe it’s time to go for that promotion you’ve had your eye on. Or maybe the change is as simple as better connecting with colleagues you haven’t gotten to know.\n\n555 is also a harbinger of financial abundance.\n\nIf you are seeing the angel number 555 everywhere you look, it is a sign that your wealth is going to increase.\n\nBe on alert: your angels may be trying to tell you that riches are coming your way, or that you must be open to opportunities to increase your wealth yourself."""

five.spiritual = """\nThe angel number 555 is a sign of spiritual transformation.\n\n555 is a message from your guardian angels telling you to embrace your status as a divine being in human form, and to recognize that you hold the power to make and receive great change.\n\nChange can be scary, but don’t worry: your angels want you to know you’re on the right path, and they’ve got your back no matter what’s coming down the pike.\n\n555 may also be a sign that you will have to take action to initiate change.\n\n555 could mean spiritual transformation is coming for you—but it could also be a sign you will have to make the movements yourself.\n\nYour angels may be nudging you to take control of your life and effect change on your own.\n\nThis is a high-energy time of exciting shifts and transformations—but it can also be daunting.\n\nDon’t fret: your angels have your back!"""

five.life = """\n555 is a reminder to take control of your well-being.\n\nYou cannot control every aspect of your physical and mental health, but you can still show yourself, your mind, and your body the respect it deserves.\n\n555 is a sign to practice agency when it comes to your health: now is the time to make changes you have been putting off or feeling too overwhelmed to implement.\n\nRegarding physical health, practising agency may mean implementing a new exercise routine, or finally making that doctor’s appointment to address an issue you are having, or switching practitioners if your current one doesn’t meet your needs.\n\nRegarding mental health, practising agency may mean seeking counseling to take control of your emotional and mental wellbeing, or implementing a yoga or meditation routine to help you achieve peace and contentment.\n\nIf angel number 555 keeps showing up, believe in yourself and your abilities.\n\n555 is about embracing your curiosity and taking risks to achieve your goals.\n\nThis can be daunting, even for those with a penchant for excitement and experimentation, but don’t worry. Whether the change is coming to you or your angels are urging you to take the reins and effect change yourself, be brave and believe in yourself.\n\nYou hold the power to live out the life the universe has set in motion for you.\n\nMaybe there are people or things that no longer serve you or that deplete your energy—555 could be a sign it is time to let go of them.\n\nMaybe there are goals you are too afraid to pursue—if you see 555, take the chance and follow your dreams. Whether you succeed or not, your angels have your back.\n\nThe change may be small or big, enlightening or confusing, devastating or joyous. No matter what, it is part of the divine plan, and it will bring you closer to your ultimate purpose."""




six = Number()

six.meaning = """"""

six.love_single = """"""

six.love_relationship = """"""

six.twinflame = """"""

six.career = """"""

six.spiritual = """"""

six.life = """"""




seven = Number()

seven.meaning = """"""

seven.love_single = """"""

seven.love_relationship = """"""

seven.twinflame = """"""

seven.career = """"""

seven.spiritual = """"""

seven.life = """"""




eight = Number()

eight.meaning = """"""

eight.love_single = """"""

eight.love_relationship = """"""

eight.twinflame = """"""

eight.career = """"""

eight.spiritual = """"""

eight.life = """"""




nine = Number()

nine.meaning = """"""

nine.love_single = """"""

nine.love_relationship = """"""

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