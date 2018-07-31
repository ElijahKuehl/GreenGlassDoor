# every word that Follows the pattern will be capitalized.
# The pattern is only words with the same letter repeated side by side are behind the Green Glass Door.


def Green_Glass_Door():
    count = 0
    temp = 2
    x = 0
    y = 1
    print
    print "what Will you Guess? if you think you have figured out the Pattern, type '!'."
    # lets you put in a word, and Tells you if it Follows the Pattern
    Guess = raw_input()
    Guess = Guess.lower()
    Guess_list = list(Guess)
    for Letter in Guess_list:
        count += 1
    count -= 1
    z = count
    if count < 1 and Guess != "!":
        print
        print "there is nothing behind the Green Glass Door with less than two Letters in its name."
        Green_Glass_Door()
    # makes Grammar Happen
    if Guess_list[z] == "s":
        isare = "are"
    else:
        isare = "is"
    while count > 0:
        temp = 0
        if Guess_list[x] == Guess_list[y]:
            print
            print Guess.capitalize(), isare, "behind the Green Glass Door."
            temp = 1
            Green_Glass_Door()
        else:
            x += 1
            y += 1
        count -= 1
    if temp == 0:
        print
        print Guess, isare, "not behind the Green Glass Door."
        Green_Glass_Door()
    if Guess == "!":
        aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte = random()

        quiz(aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte)
        return


def random():
    # randomizes the quiz.
    from random import randint
    numa = randint(1, 3)
    if numa == 1:
        aska = "do 'Glasses'"
        ansa = ["y", "yes"]
    elif numa == 2:
        aska = "do 'contacts'"
        ansa = ["n", "no"]
    elif numa == 3:
        aska = "does 'Seeing'"
        ansa = ["y", "yes"]
    numb = randint(1, 3)
    if numb == 1:
        askb = "'sandals'"
        ansb = ["n", "no"]
    elif numb == 2:
        askb = "'Slippers'"
        ansb = ["y", "yes"]
    elif numb == 3:
        askb = "'shoes'"
        ansb = ["n", "no"]
    numc = randint(1, 3)
    if numc == 1:
        askc = "'Moon'"
        ansc = ["y", "yes"]
    elif numc == 2:
        askc = "'sun'"
        ansc = ["n", "no"]
    elif numc == 3:
        askc = "'earth'"
        ansc = ["n", "no"]
    numd = randint(1, 3)
    if numd == 1:
        askd = "'Apples'"
        ansd = ["p", "pp"]
        hintd = "a"
    elif numd == 2:
        askd = "'Wood'"
        ansd = ["o", "oo"]
        hintd = "w"
    elif numd == 3:
        askd = "'Process'"
        ansd = ["s", "ss"]
        hintd = "p"
    nume = randint(1, 3)
    if nume == 1:
        aske = "'Speed'"
        anse = ["e", "ee"]
        hinte = "s"
    elif nume == 2:
        aske = "'Running'"
        anse = ["n", "nn"]
        hinte = "r"
    elif nume == 3:
        aske = "'Ball'"
        anse = ["l", "ll"]
        hinte = "b"
    return aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte


def quiz(aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte):
    # Will quiz you to See if you truly know the Pattern.
    print "\nanswer using yes(y) or no(n)"
    print "you think you figured out the Pattern?"
    yorn = raw_input()
    yorn = yorn.lower()
    if yorn in ["y", "yes"]:
        print "\nWell,", aska, "exist behind the Green Glass Door?"
        a = raw_input()
        a = a.lower()
        print "\ndo", askb, "exist behind the Green Glass Door?"
        b = raw_input()
        b = b.lower()
        print "\nand does the", askc, "exist behind the Green Glass Door?"
        c = raw_input()
        c = c.lower()
        if a in ansa and b in ansb and c in ansc:
            print "\nHmm... okay. what part of", askd, "Follows the Pattern?"
            d = raw_input()
            d = d.lower()
            print "\nand what part of", aske, "Follows the Pattern?"
            e = raw_input()
            e = e.lower()
            if d in ansd and e in anse:
                print "\nha! you got it!"
                print "\nonly words that have the same letter twice in a row are behind the Green Glass Door!"
                print "\nand if you didn't know that and just got lucky, Well now you do."
                print "\njust don't Tell anyone, 'kay?"
                print "\nthanks for playing the Green Glass Door!"
                return
            elif d == hintd or e == hinte:
                # if Successfully misled, this Will re-guide them.
                print "\ncapital letters are not the Pattern, but the capitalized words do follow the Pattern."
                Green_Glass_Door()
            else:
                print "\nyou may have had the format of your answer Off, or you were just plain Incorrect.\n"
                Green_Glass_Door()
        else:
            print "\ni'm afraid that is Incorrect."
            Green_Glass_Door()
    elif yorn in ["n", "no"]:
        print "\nWell then what did you type '!' for?"
        Green_Glass_Door()
    else:
        print "\ni didn't quite catch that..."
        Green_Glass_Door()


def intro():
    print "\n\nin my dimension, we have a Green Glass Door."
    print "\nthere are many things behind the Green Glass Door, and nothing makes sense."
    print "\nbut All things behind the Green Glass Door Follow a Pattern."
    print "\nonly i know the Pattern, but you can discover the Pattern, just stay quiet if you do."
    print "\nyou can Guess something, and i Will Tell you if it is behind the Green Glass Door."
    Green_Glass_Door()


if __name__ == "__main__":
    intro()
