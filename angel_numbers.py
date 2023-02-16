# Angel Number Project version 1.0
# Reid Davis
# February 6, 2023

# ***********  DISCLAIMER: All of the writing for the meanings of the numbers was pulled from Wikihow.com  ***************
# ***********  I only claim to have written the text during intial setup and explanation of the program    ***************
# ***********  I do not claim to have written the actual explanations of the numbers meanings              ***************

# References to the articles I used for the explanations of the different numbers below:

# References:

# https://www.wikihow.com/Angel-Number-Meaning-111

# https://www.wikihow.com/222-Angel-Number-Meaning

# https://www.wikihow.com/333-Angel-Number-Meaning-in-Love

# https://www.wikihow.com/444-Angel-Number-Meaning

# https://www.wikihow.com/555-Angel-Number-Meaning

# https://www.wikihow.com/666-Angel-Number

# https://www.wikihow.com/777-Angel-Number-Meaning

# https://www.wikihow.com/888-Angel-Number-Meaning

# https://www.wikihow.com/999-Angel-Number

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

one.spiritual = """\n111 is a sign to nurture your connection with your Higher Self.\n\nThis is the part of you that knows what’s best for you at all times and has a direct connection to the energies of the universe.\n\nSome call it your intuition—the inner voice that guides your most meaningful, positive decisions. Your higher self is what leads you to your life’s spiritual purpose.\n\nTake time to reflect on habits and beliefs that no longer serve your highest good. Clear them from your mind to make space for more exciting, fulfilling thoughts."""

one.life = """\nNumber 1 is a symbol of confidence and action.\n\nIt vibrates with the energy of deep self-understanding and the knowledge that you have the skills and wisdom you need to accomplish your goals and believe in yourself.\n\nWhen you encounter 1s (like seeing 1111, 111, or 11), it means you’re approaching a milestone and everything is in place for you to succeed if you believe you can.\n\nThe universe or your guardian angels are sending you 1s to support and encourage you as you move through life with confidence."""




two = Number()

two.meaning = """\n\n222 is one of the most calming messages\n\nAngel number 222 asks you to have hope, faith, and trust.\n\nIf you come across it, you might even feel like a sense of peace has washed over you already.\n\n222 also reassures, 'Everything will definitely balance out in your life!'\n\nIf you’ve felt down on your luck or a little lost, 222 will emerge like a beacon of light.\n\nThis brilliant angel number wants to relay the message that you’ve got all the right tools—smarts, guts, and perseverance!\n\nStay hopeful! With all that on your side, you’ll be alright."""

two.love_single = """\nIf you’re single, 222 hints that a new love interest will show up.\n\nWhen you find yourself a little lonely or you just crave companionship, 222 often makes an appearance.\n\nMake sure to put your best foot forward and keep your head up high!\n\nYou’ll want to shine when you run into that attractive stranger who might just change your life."""

two.love_relationship = """\nFor long-term relationships, 222 reminds you to invest effort in love.\n\nIf you or your partner are at risk for taking the other for granted, your guardian angels will kick into gear.\n\nThey’ll send off a 222 as a rallying cry for you to make sparks fly in your romance again.\n\nMake sure to prioritize quality time—setting up an ongoing date night is a good start!"""

two.twinflame = """\n222 declares you’ll find a twin flame who will bring romantic bliss.\n\nMost of the time, a twin flame can be hot and heavy or seriously stormy. When 222 crops up, though, you can expect a way tamer twin flame connection.\n\nYou’ll still learn a lot from your twin flame, but your love affair will be a slow burn that you really savor.\n\nIn fact, it’ll probably feel like the fairy tale you’ve always been waiting for."""

two.career = """\nAngels can also send 222 to tell you that hard work really pays off.\n\n222 is also a special “congratulations!” for all the ways you’ve committed to a project or calling.\n\nWhether you’re a full-time student, a model employee, or a doting parent, 222 symbolizes that your angels are praising you.\n\nYou’ve really struck the right balance and made all the right decisions. All your discipline and determination has been noticed, and you’ll be richly rewarded for it.\n\nDual 22 also signifies large-scale ventures which could be lucrative and may depend on the public for success through hard work."""

two.spiritual = """\n222 provides hope and spiritual growth. If you’ve been curious about prayer, meditation, or any other metaphysical journey, 222 is a divine nudge.\n\nYour angels are excited by your new direction, and they’re hinting that there’s so much in store for you when you take your next step.\n\nStay optimistic and remember that the best is yet to come!\n\nIf you’ve endured one obstacle after the other and have reached out for a sign, 222 is meant to recharge your faith.\n\n222 is a gentle reminder that you’ll find harmony. When life feels like it’s fallen apart or your heart is broken, The Universe will help you put the pieces back together."""

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

five.love_relationship = """\nIn romance, 555 is a nudge to show your partner more love.\n\nWhen you see the angel number 555, take it as a reminder to show your partner more love and tenderness at this time.\n\nYou may be craving attention and adoration yourself, but 555 is about taking action and being vulnerable: by giving more attention to your partner, you will receive the adoration you long for in return.\n\n5 represents the ultimate balance that comes from knowing when to move and when to be still: as the tide ebbs and flows, you cannot sit still forever and expect transformation to occur.\n\n555 means it is your turn to move.\n\nPractice good communication with your partner to promote peace and harmony.\n\nAngel number 555 is a sign to be open in your relationship. Don’t wait for peace: make it happen."""

five.twinflame = """\nIn twin flame relationships, 555 is a sign to keep moving forward.\n\nIf you have found your twin flame, angel number 555 means progress and happiness are ahead—especially if you have recently endured tumultuous times in your relationship.\n\nThe hard work you have put into your relationship hasn’t been for naught.\n\nThe journey you share with your twin flame is going according to plan, just keep moving.\n\nYou and your twin flame can breathe easy: 555 is a blessing for you. But don’t take this peace for granted.\n\nContinue to tend to your twin flame relationship to make sure it remains strong.\n\nBecause your twin flame mirrors you, you can’t get away with anything less than radical honesty.\n\n555 is a reminder to be open with yourself and your twin flame in order to cultivate a strong relationship.\n\nRemember that your relationship with your twin flame is not necessarily romantic, though it can be.\n\nTwin flames are two people who share the same soul and therefore mirror one another, whereas soulmates are two people whose souls are very compatible."""

five.career = """\nAngel number 555 indicates changes in your career.\n\n555 is a push from your angels to consider your current professional status: are you where you’re meant to be? Do you enjoy the work you’re doing?\n\nIf the answer is no, it’s time to take steps in the right direction. Explore new job opportunities, and connect with professionals in other disciplines to see what doors may be open to you.\n\nIf the answer is yes, it’s time to reach for more. Maybe it’s time to go for that promotion you’ve had your eye on. Or maybe the change is as simple as better connecting with colleagues you haven’t gotten to know.\n\n555 is also a harbinger of financial abundance.\n\nIf you are seeing the angel number 555 everywhere you look, it is a sign that your wealth is going to increase.\n\nBe on alert: your angels may be trying to tell you that riches are coming your way, or that you must be open to opportunities to increase your wealth yourself."""

five.spiritual = """\nThe angel number 555 is a sign of spiritual transformation.\n\n555 is a message from your guardian angels telling you to embrace your status as a divine being in human form, and to recognize that you hold the power to make and receive great change.\n\nChange can be scary, but don’t worry: your angels want you to know you’re on the right path, and they’ve got your back no matter what’s coming down the pike.\n\n555 may also be a sign that you will have to take action to initiate change.\n\n555 could mean spiritual transformation is coming for you—but it could also be a sign you will have to make the movements yourself.\n\nYour angels may be nudging you to take control of your life and effect change on your own.\n\nThis is a high-energy time of exciting shifts and transformations—but it can also be daunting.\n\nDon’t fret: your angels have your back!"""

five.life = """\n555 is a reminder to take control of your well-being.\n\nYou cannot control every aspect of your physical and mental health, but you can still show yourself, your mind, and your body the respect it deserves.\n\n555 is a sign to practice agency when it comes to your health: now is the time to make changes you have been putting off or feeling too overwhelmed to implement.\n\nRegarding physical health, practising agency may mean implementing a new exercise routine, or finally making that doctor’s appointment to address an issue you are having, or switching practitioners if your current one doesn’t meet your needs.\n\nRegarding mental health, practising agency may mean seeking counseling to take control of your emotional and mental wellbeing, or implementing a yoga or meditation routine to help you achieve peace and contentment.\n\nIf angel number 555 keeps showing up, believe in yourself and your abilities.\n\n555 is about embracing your curiosity and taking risks to achieve your goals.\n\nThis can be daunting, even for those with a penchant for excitement and experimentation, but don’t worry.\n\nWhether the change is coming to you or your angels are urging you to take the reins and effect change yourself, be brave and believe in yourself.\n\nYou hold the power to live out the life the universe has set in motion for you.\n\nMaybe there are people or things that no longer serve you or that deplete your energy—555 could be a sign it is time to let go of them.\n\nMaybe there are goals you are too afraid to pursue—if you see 555, take the chance and follow your dreams. Whether you succeed or not, your angels have your back.\n\nThe change may be small or big, enlightening or confusing, devastating or joyous. No matter what, it is part of the divine plan, and it will bring you closer to your ultimate purpose."""




six = Number()

six.meaning = """\n666 is like a gentle reminder to focus on what really matters.\n\nThis number sequence may appear randomly, but it could be a sign from the universe to keep your priorities in check.\n\nIf you see this number frequently, it might be time to reassess your goals and make sure you're staying true to your authentic path.\n\nSometimes, you might lose sight of your original ambitions.\n\nFor example, if you try to be a people-pleaser all the time, then you might not have enough time or energy to work on creative projects you've always wanted to tackle.\n\nIn this case, 666 can remind you to make more time for yourself and your passions.\n\nIf you have some unhealthy habits, 666 invites you to replace them.\n\nMaybe you have some patterns—like comparing yourself to people on social media—that impact your emotional or mental health.\n\n666 is a clue that angels have taken notice and want you to build a positive mindset and prioritize a balanced lifestyle instead.\n\nIf you're sweating the small stuff, 666 encourages you to destress. Lately, you might find yourself overwhelmed by what seem like big issues.\n\nYou could be worried about how people perceive you or how successful you seem.\n\nWhen you see 666, it's a great chance to stop, take a deep breath, and ground yourself.\n\nIf you're overlooking your health, 666 might keep popping up. Maybe you're downing your fifth cup of coffee and turning down yet another night of good sleep.\n\nIf you haven't exactly been taking great care of yourself, 666 can help remind you to get back on track.\n\nOnce the angels give you a friendly poke, you'll probably feel inspired to change your lifestyle for the better."""

six.love_single = """\nIn your love life, 666 can be a sign that you're close to coming into contact with your twin flame.\n\nThis is also an angel's way of letting you know that you'll need to learn to communicate better with this individual.\n\nOnce you determine if you've found your soulmate, the next step is to hold onto them by practicing unconditional love."""

six.love_relationship = """\nDuring clashes with a Significant Other, 666 may show up to resolve conflicts.\n\nIf you've found your twin flame and don't want to snuff out your fun and fiery love affair, then it's important to cool off when conversations get heated.\n\n666 reminds you to take it easy on your sweetie and embrace all their positive qualities instead of nitpicking or picking fights.\n\nBe gentle with your Significant Other when 666 shows up. A twin flame relationship is all about healing emotional wounds and achieving spiritual growth together.\n\nIn order to achieve that, you and your partner will have to laugh off silly arguments and show each other kindness whenever you can.\n\nWhen you put respect over being "right" all the time, your relationship will be one for the ages."""

six.twinflame = """\nIf love’s on your mind, 666 says you’ll meet your twin flame. If you’ve been hungering for an intense romance, then 666 is reassurance that you’re destined to find a twin flame."""

six.career = """\nThe number 666 asks you to keep sight of your biggest goals.\n\nIf you've been bogged down with a lot of distractions, such as binge-watching TV every night, 666 can help shift your focus.\n\nWhen you see it, you may find that you'd like to be more productive and work on what you really care about, such as writing your own screenplay instead of just passively enjoying shows.\n\nA lot of people see the number 666 and think it's unlucky. But if you're seeing it a lot, it is actually an omen of good fortune.\n\nIt means that you're on the right track for your career and finances. You should continue pursuing your goals and following your dreams.\n\nTrust that you are headed in the right direction and everything will fall into place."""

six.spiritual = """\nThe angel number 666 asks you to redirect your energy so you'll thrive.\n\nSure, 666 is calling out that you're facing lots of temptations, but the angels sending it aren't trying to lecture you.\n\nThey just really care about you and want to make sure that you steer clear of any toxic people, media, or patterns that keep you from manifesting your goals.\n\n666 is sometimes associated with the Devil, but it's just an angelic revelation that there's some chaos that might throw you off track.\n\nIn Christianity, 666 is known as the “mark of the beast,” but it can be interpreted in many different ways.\n\nThe repeated presence of the number 6 just signifies that humans are not perfect like God is, and so they’re easily influenced by temptation.\n\nIf it helps, you can think of the "Devil" major arcana card from a Tarot deck. When you read tarot cards, the Devil just symbolizes forces you need to resist.\n\nThe number 666 is also a gentle reminder that you are always connected to the divine. No matter what might be going on in your life at the moment, remember that you have a higher purpose.\n\nYou are always connected to something bigger and better."""

six.life = """\nThe number 6 is a sign that self-love is a must-have in your life.\n\nIn the Tarot, the number 6 represents "The Lovers." In addition, in numerology, 6 symbolizes total and perfect love.\n\nIn essence, once you tap into the power of 6, you can fully love yourself. When you embrace all of who you are, others will, too.\n\nIf the number 6 is tripled, it's a hint that you'll enjoy perfect harmony.\n\nOnce you're hit with 666, it's actually a great sign you'll achieve balance in your friendships, career, and love life.\n\nNumerically speaking, when you channel the energy of the three sixes, you'll amplify peace in every aspect of your life.\n\nWhen you're under a lot of pressure, 666 is a sign to practice self-care.\n\nDuring periods of time when you're trying to take on the whole world, 666 can help you slow down.\n\nYou might feel like you need to rescue everyone, even if it's really draining and exhausting. Once you spot 666, your guardian angels can intervene and guide you to put yourself first.\n\nSearch for inner peace if 666 keeps making an appearance. Be honest and ask yourself if you feel a sense of balance.\n\nIf you don't, take steps to build habits that promote calmness and emotional resilience. You may wish to meditate or practice deep breathing so you can gain control of your emotions."""




seven = Number()

seven.meaning = """\nThe number 777 is a sign to keep pushing forward.\n\nIf you’re experiencing tough times, the angels want you to know that the heavenly realm is on your side.\n\nIdentify what you can control in a situation, and remember to visualize your end goal–all of your efforts will pay off soon!\n\nTo overcome obstacles, create an actionable list of steps you can take. Break down large tasks into shorter ones, or record your progress in a journal.\n\nWhen repeated, the number 7 represents higher self-awareness. There are 7 colors in the rainbow, 7 chakras, and 7 spiritual levels to heaven.\n\nWhen 7 is multiplied (77 or 777), the angels are urgently trying to get your attention. They want you to strive for spiritual enlightenment and trust your intuition when making decisions.\n\nSelf-reliance is crucial to reach self-awareness. It might be challenging if you frequently ask people for advice, but remember that you create all your experiences!\n\nWhen decision-making, reflect on the past and use it as guidance."""

seven.love_single = """\nIf you’re single, 777 is a sign to focus on your spiritual path. The angels are advising you to work on all the relationships in your life, starting with yourself.\n\nIt’s important to have a clear, peaceful mind before pursuing a relationship. If you don’t know who you are and what you want, you might attract the wrong partner!\n\nTo connect with your spiritual side, practice daily gratitude journaling. Write down a list of all the things you’re thankful for and find ways to give back to your community."""

seven.love_relationship = """\nIf you’re in a relationship, use your spiritual journey as a tool to strengthen your bond with your partner.\n\nFoster meaningful conversations by asking them open-ended questions so you can grow together as a couple.\n\nIt’s important to consider that some people aren’t looking for advice when they share their problems. Listen carefully to your partner before responding.\n\nThe most meaningful response can be validating what the other person is feeling."""

seven.twinflame = """\nIf you see 777, the angels are preparing you for your twin flame’s arrival.\n\nTwin flames refer to two individuals who share a deep, powerful connection–they’re two halves of the same soul.\n\nIf you haven’t found your twin flame yet, the number 777 is a sign that your other half is nearby. Twin flames can appear in the most unexpected places, so keep an open heart and mind.\n\nYou might run into someone special very soon!\n\nWhen the angels guide you to your other half, there are several signs you’ve met your twin flame.\n\nMany people believe twin flames share a past life, so you may experience feelings of deja vu when you encounter them for the first time."""

seven.career = """\nCareer-wise, the angels are encouraging you to embrace change. Everyone faces periods of uncertainty in their career.\n\nIf you’re facing obstacles, it’s important to develop a growth mindset and view every challenge as an opportunity to learn!\n\nIf you find yourself struggling to cope with failure, consider talking to a close friend or family member.\n\nAnother perspective can shed new light on a situation and help you overcome your mistakes."""

seven.spiritual = """\nThe angel number 777 represents completeness. The number 777 signifies that your spirit and soul are in alignment.\n\nYour guardian angels want you to know that you’re on the right path in your spiritual journey, as long as you work toward a balanced life.\n\nIn Christianity, 777 is often referred to as “God’s number”.\n\nIt represents the perfection of the Holy Trinity, serving as a reminder to trust in divine timing.\n\nThe angel number 777 represents good fortune. Commonly associated with jackpots, the number 777 is a sign of prosperity.\n\nEven if you don’t win the lottery, the angels want you to remain patient and focused. Good things take time!\n\nIn some cultures, 777 represents lack of discipline and gambling.\n\nIt’s important to learn how to be content with your life so you don’t get swept away by materialistic desires."""

seven.life = """\nThe number 777 serves as a reminder that you’re on the right path.\n\nYour guardian angels want you to know that positive change is on the horizon. Keep working toward your goals and be mindful of who you surround yourself with.\n\nThe number 777 could be a warning to focus on your surroundings.\n\nIf certain people or activities are preventing you from achieving your highest spiritual self, replace them with ones that increase harmony in your life.\n\nDiscover your purpose in life.\n\nLife is hectic sometimes, and it can be a challenge to slow down and reflect.\n\nTo help find your purpose in life, reflect on who you are, what you consider meaningful, and what you want in life.\n\nWrite down who inspires you and figure out how they achieved their goals.\n\nUse their life as a blueprint for your own, focusing on small changes you can make to increase your happiness.\n\nBring positive energy into your life.\n\nHigh frequency vibrations, like feelings of joy and clarity, have the ability to improve your mental, physical, and emotional state.\n\nAttract this energy by putting yourself first or actively thinking positive thoughts.\n\nRemember that your thoughts can manifest into reality. By maintaining a positive outlook, you attract positive people and experiences into your life."""




eight = Number()

eight.meaning = """\n888 is an indicator of abundance, wealth, and material success.\n\nSeeing the angel number 888 means that you’re about to enter a period of prosperity.\n\nYou might inherit a large fortune from a deceased relative, win the lottery, or start a new job with a higher salary.\n\nThe unending curves of the number 8 reflect the flow of cosmic cycles and the endless circulation of abundance.\n\n888 also reflects the reality that cycles ebb and flow, meaning that abundance will one day pass."""

eight.love_single = """\nAngel number 888 means love is on the way.\n\nIf you’re single, seeing 888 could be an indicator that love is just around the corner.\n\nYour angels are using manifestations of 888 to reassure you that you are exactly where you need to be and good fortune is coming in only a matter of time."""

eight.love_relationship = """\n888 is a reminder to balance your relationship.\n\nReceiving messages of 888 from the universe may be a sign that your relationship has become one-sided.\n\nIt is a directive to ensure that both partners are putting equal effort into communicating and growing together to allow love to flow in both directions."""

eight.twinflame = """\nIf you’re seeing 888, you are in perfect sync with your twin flame.\n\nA twin flame is the other half of your soul who, when you meet, restores your mind and spirit in oneness.\n\n888 means that you will meet your twin flame soon, and you should use this period of abundance to open yourself to infinite love."""

eight.career = """\nSeeing 888 means you should manifest career changes.\n\n888 means that you have been successfully manifesting events like a raise, job change, or career achievement.\n\nAs you enter this abundant period, put even more emphasis on your manifestations with the power of the universe behind you.\n\nRecognize that you’re on the right track when you see 888.\n\nAngel number 888 is a sign from the universe that you are on the right track to achieving your goals and reaching your higher self."""

eight.spiritual = """\nAngel number 888 is connected to infinity and cosmic cycles.\n\nSince the number 8 is a sideways infinity symbol, 888 is considered to be an indicator of triple infinity.\n\nThis means that your life is open to limitless abundance and possibilities.\n\n888 is a message of balance. The mirror image represents the balance between the higher and the lower, spiritual movement and the material world.\n\nIf your life has been feeling out of balance recently, seeing 888 means that it will be restored.\n\nIt can also mean that you must prioritize balance in your life going forward.\n\nThe circle on top represents the spiritual aspects of things or the creative or your mind and then the bottom represents the material world."""

eight.life = """\nSeeing 888 means a cycle has come to end.\n\nYou could be seeing 888 more frequently because you’ve outgrown a romantic relationship or a career that no longer serves you.\n\nThe universe is telling you to let go and trust the process.\n\n888 also means you have wisdom to share.\n\nThe universe may be sending you a message to share your wisdom and talents with others.\n\n\nThe universe recognizes your hard work with angel number 888.\n\nThis number is a sign from the angels that they recognize your hard work and will be rewarding you soon.\n\nIt can also be a sign that you’ve done all you can in a certain situation and must now leave the rest up to the universe.\n\nWhile seeing this angel number may mean that your hard work is being recognized, it may also mean that your bad decisions are going to be punished following the cycle of karma. Whatever you have sowed is about to be reaped."""




nine = Number()

nine.meaning = """\nSeeing 999 means one phase of your life is ending so another can begin.\n\nYou’re entering a new period of change-maybe a new job is on the horizon, you’re about to form a new relationship, or you’ve let go of heavy emotions from the past.\n\n999 is a reminder to trust life’s cyclical nature and have faith that the universe is guiding you to a higher potential.\n\nThese changes may be obvious, like an upcoming move across the country, or very subtle, like a new outlook on life gained from a recent experience.\n\n999 is an amplification of the number 9.\n\n9 is the largest single-digit number, so it naturally symbolizes endings and new beginnings.\n\nIt vibrates with the experience and energy of the numbers beneath it and represents spiritual service to the whole.\n\nIn numerology, 9 means completion, wisdom, and a duty to help others."""

nine.love_single = """\n999 encourages you to find people who help you grow.\n\nIt doesn’t have to be a romantic partner—999 encourages you to feel and explore all kinds of love.\n\nLove for your friends and family, compassion for animals and wildlife, and self-love are all encouraged by this angel number.\n\nInvest in relationships with people you trust, who let you be independent and make your own choices and share and support your life goals."""

nine.love_relationship = """\n999 might be a sign to end a draining or toxic relationship.\n\nIf a friend or significant other is holding you back from reaching your potential or your relationship has simply run its course, a 999 sighting means it’s time to let them go to make room for new and fulfilling partnerships.\n\nIt might also be a sign to heal old wounds, find closure from past heartbreak, or release resentment and grudges toward old enemies."""

nine.twinflame = """\n999 might be a sign that you’re about to find (or already found) your twin flame\n\nSomeone you consider a soulmate or to whom you’re inextricably connected."""

nine.career = """\n\nActively pursue your goals. Angel numbers present themselves to guide you, not to work for you.\n\nLook for ways to begin thriving—break off toxic relationships, show kindness to yourself and others, and look to the future.\n\nIt’s OK if you don’t know exactly what you’re working toward at first. Trust that the universe and your intuition will guide you toward your ultimate purpose.\n\nLet go of any negativity holding you back. As you focus on inner peace and harmony, your path in life will come into focus.\n\nYou could be standing on the edge of a breakthrough and not realize it yet! Be bold and have faith in the universe’s plan for you."""

nine.spiritual = """\n999 signals a new calling or a higher purpose.\n\nThis angel number appears in your life when you’ve obtained the ability to achieve your goals.\n\nLook inward and follow your intuition—the universe is calling on you to stop doubting yourself and find new inner strength.\n\n999 is associated with light-working (making your own choices instead of following the norms), and you may have the destiny to help others.\n\nTrust that you are on the right path. When you follow your instincts, your personal, spiritual meaning of 999 will become clear to you.\n\nSeeing 999 means you’ve ascended to a spiritual point where you can serve the whole. The lives of the people you care about are attached to you and your actions.\n\nBecome an example of how to live authentically and inspire others to do the same.\n\nThink of yourself as a role model—the universe has given you this wonderful responsibility because it believes you are up to the task!\n\nReject the status quo and make decisions based on your spirit.\n\nThe angel number 999 is the encouragement to break the mold and try something new."""

nine.life = """\nPractice gratitude for leveling up from one phase of life to the next. The universe sends you 999 to help you move on to bigger and better things.\n\nRecognize that you’re being given opportunities for growth and being shown new ways to love yourself and the people in your life.\n\nThank the universe for its blessing, and be proud of your hard work and accomplishments so far!\n\nReflect on what you were doing or thinking when you saw 999. This number often appears when the thing it relates to is near you.\n\nIt's hard to watch one door close, but remember that another is opening.\n\nWhen you come across 999 repeatedly, a major part of your life is ending so that you can grow and evolve into the person you were meant to be.\n\nTrust that it’s for the best and surrender yourself to life’s cyclical nature. 999 is here to keep your spirits high and make you shine.\n\nAs you gain spiritual clarity and move closer to your goals, you’ll feel fulfilled by all the positive changes in your life."""
    

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
    print("\nOkay! I'll give you all the information about your number.")
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
print("\nIf you opted to skip the questions, you'll see it all!")
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
print("\nThere you have it!\n\nI hope this was able to shed some light on how the Universe may be trying to communnicate with you.")
print("\nIf you would like to see a different number, feel free to run the Program again\n")
print("\nThanks for using my fun little program!")
print("\nExit...")
wait()