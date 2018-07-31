from appJar import gui


def Press(Button):
    if Button == "what is this?":
        intro()
    elif Button == "check":
        check()
    elif Button == "i figured it out!":
        aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte = random()

        quiz(aska, ansa, askb, ansb, askc, ansc, askd, ansd, hintd, aske, anse, hinte)
    elif Button == "quit":
        app.stop()


def intro():
    app.infoBox("explanation", "in my dimension, we have a Green Glass Door.")
    app.infoBox("explanation", "there are many things behind the Green Glass Door, and none of it makes sense.")
    app.infoBox("explanation", "but All things behind the Green Glass Door Follow a Pattern.")
    app.infoBox("explanation", "only i know the Pattern, but you can discover the Pattern, just stay quiet if you do.")
    app.infoBox("explanation", "you can Guess something, and i Will Tell you if it is behind the Green Glass Door.")
    app.infoBox("explanation", "try to figure out the Pattern with the responses.")


def check():
    count = 0
    temp = 2
    x = 0
    y = 1
    Guess = app.getEntry("Guess: ").lower()
    app.clearEntry("Guess: ")
    Guess_list = list(Guess)
    for Letter in Guess_list:
        count += 1
    count -= 1
    z = count

    if count < 1 and Guess != "!":
        app.setMessage("behind", "nothing with less than two Letters in its name is behind the Green Glass Door.")
        return

    if Guess_list[z] == "s":
        isare = "are"
    else:
        isare = "is"

    while count > 0:
        temp = 0
        if Guess_list[x] == Guess_list[y]:
            response = Guess.capitalize(), isare, "behind the Green Glass Door."
            response = " ".join(response)
            app.setMessage("behind", response)
            temp = 1
        else:
            x += 1
            y += 1
        count -= 1
    if temp == 0:
        response = Guess, isare, "not behind the Green Glass Door."
        response = " ".join(response)
        app.setMessage("behind", response)


def random():
    # randomizes the quiz.
    from random import randint
    numa = randint(1, 3)
    if numa == 1:
        aska = "do 'Glasses'"
        ansa = True
    elif numa == 2:
        aska = "do 'contacts'"
        ansa = False
    elif numa == 3:
        aska = "does 'Seeing'"
        ansa = True
    numb = randint(1, 3)
    if numb == 1:
        askb = "'sandals'"
        ansb = False
    elif numb == 2:
        askb = "'Slippers'"
        ansb = True
    elif numb == 3:
        askb = "'shoes'"
        ansb = False
    numc = randint(1, 3)
    if numc == 1:
        askc = "'Moon'"
        ansc = True
    elif numc == 2:
        askc = "'sun'"
        ansc = False
    elif numc == 3:
        askc = "'earth'"
        ansc = False
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
    yorn = app.yesNoBox("start", "you think you figured out the Pattern?")
    if yorn is True:
        q1 = "Well,", aska, "exist behind the Green Glass Door?"
        q1 = " ".join(q1)
        a = app.yesNoBox("question 1", q1)

        q2 = "do", askb, "exist behind the Green Glass Door?"
        q2 = " ".join(q2)
        b = app.yesNoBox("question 2", q2)

        q3 = "and does the", askc, "exist behind the Green Glass Door?"
        q3 = " ".join(q3)
        c = app.yesNoBox("question 3", q3)

        if a is ansa and b is ansb and c is ansc:
            q4 = "Hmm... okay. what part of", askd, "Follows the Pattern?"
            q4 = " ".join(q4)
            d = app.textBox("question 4", q4)
            d = d.lower()

            q5 = "and what part of", aske, "Follows the Pattern?"
            q5 = " ".join(q5)
            e = app.textBox("question 5", q5)
            e = e.lower()

            if d in ansd and e in anse:
                app.infoBox("victory!", "ha! you got it!")
                app.infoBox("victory!", "only words with the same letter twice in a row are behind the Green Glass Door!")
                app.infoBox("victory!", "and if you didn't know that and just got lucky, Well now you do.")
                app.infoBox("Shoosh.", "just don't Tell anyone, 'kay?")
                app.infoBox("victory!", "thanks for playing the Green Glass Door!")
                app.stop()

            elif d == hintd or e == hinte:
                # if Successfully misled, this Will re-guide them.
                app.infoBox("Incorrect", "Incorrect, capital letters are not the Pattern.")
                app.infoBox("hint", "however, the words that are capitalized do Follow the Pattern.")
            else:
                app.infoBox("Incorrect", "you may have the format of your answer Off, or you were just plain Incorrect.")
        else:
            app.infoBox("Incorrect", "i'm afraid that was Incorrect.")


app = gui("Green Glass Door", "600x400")
app.setBg("#66FF66")
app.setFont(20)
app.addLabel("title", "The Green Glass Door")
app.setLabelBg("title", "#00FF00")
# app.setLabelFont(size=22)
app.addLabelEntry("Guess: ")
app.setFocus("Guess: ")
app.addButtons(["what is this?", "check", "i figured it out!", "quit"], Press)
app.setButtonBg("what is this?", "#00CC00")
app.setButtonBg("check", "#00CC00")
app.setButtonBg("i figured it out!", "#00CC00")
app.setButtonBg("quit", "#00CC00")
app.addMessage("behind", "")
app.setMessageWidth("behind", "500")
app.addLabel("Buffer", "")

app.go()

