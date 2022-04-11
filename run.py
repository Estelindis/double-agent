"""
Project Portfolio 3 (Python): "Double Agent"
Developed and written by Siobhán Mooney, April 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
"""

import time

text_speed = 0.5

stats = {
    "information": 0,
    "legitimacy": 3,
    "trust_gov": 5,
    "trust_pref": 5
}

inventory = {
    "adari_knife": 0,
    "adari_poison": 0,
    "khell_poison": 0,
    "adari_outfit": 0,
    "khell_uniform": 0
}

plot = {
    "spy_under_duress": False,
    "spy_try_to_flee": False,
    "knife_taken": False,
    "offended_gov": False
}


def bad_end():
    """
    Prints some gruesome text when the user reaches a bad ending.
    """
    print('''\033[38;5;196m

▄███████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██  ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░██ ░██ ▒██  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░██░  █▌
  ▒██▒ ░ ░▓█▒░██▓░▓████▒   ░▓████▒▒██░   ▓██░░██████▌
  ▒ ░░    ▒ ▒░▓░▒░▒ ▓░ ░   ░░ ▒░ ░░ ▓░   ▒ ▒  ▒▒▓  ▓
    ░     ▒ ░░▒ ░ ░ ▒  ░    ░ ░  ░░ ▒░   ░ ▒░ ░ ▒  ▒
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░
          ░  ░  ░   ░  ░      ░  ░         ░    ░  ░ \033[0m\n''')


def p_d(text):
    """
    Print a line of text, then delay for text_speed.

    The function name is abbreviated to permit longer text strings.
    For clarity: p_d stands for "print, delay."
    Standard delay, as stored in the global variable text_speed, is 2 seconds.
    This delay can be quickened or slowed via Settings.
    """
    print(text)
    delay = text_speed
    time.sleep(delay)


def get_string(question):
    """Returns a non-empty string, input by the user.

    Runs a while loop, using the "question" parameter to seek user input.
    If an empty string is given (i.e. the user just presses ENTER)
    the loop will print an error message and request input again.
    """
    while True:
        input_string = input(f"{question}\n")
        if not input_string:
            print("Please input something rather than nothing.")
        else:
            return input_string


def make_choice(choice_list):
    """
    Returns the user's choice from a list of options.

    Lists should have between two and four items.
    List items follow this format: "[Choice number]: [Choice text.]"
    If the user inputs an invalid choice, they are asked again.
    Once the user inputs a valid choice, that choice is returned.
    """
    for numbered_choice in choice_list:
        print(numbered_choice)
    choice_num = len(choice_list)
    choice_made = False
    choice_final = ""
    while not choice_made and choice_num == 2:
        user_input_2 = get_string("")
        if user_input_2 == "1":
            choice_made = True
            choice_final = "1"
        elif user_input_2 == "2":
            choice_made = True
            choice_final = "2"
        else:
            p_d("Please choose option 1 or 2.")
    while not choice_made and choice_num == 3:
        user_input_3 = get_string("")
        if user_input_3 == "1":
            choice_made = True
            choice_final = "1"
        elif user_input_3 == "2":
            choice_made = True
            choice_final = "2"
        elif user_input_3 == "3":
            choice_made = True
            choice_final = "3"
        else:
            p_d("Please choose option 1, 2, or 3.")
    while not choice_made and choice_num == 4:
        user_input_4 = get_string("")
        if user_input_4 == "1":
            choice_made = True
            choice_final = "1"
        elif user_input_4 == "2":
            choice_made = True
            choice_final = "2"
        elif user_input_4 == "3":
            choice_made = True
            choice_final = "3"
        elif user_input_4 == "4":
            choice_made = True
            choice_final = "4"
        else:
            p_d("Please choose option 1, 2, 3, or 4.")
    return choice_final


def show_briefing():
    """
    Called from within start_game to print establishing text.
    """
    p_d("An empire led by evil sorcerers has conquered most of your world.")
    p_d("The Khell Imperium defeated every nation that resisted its advance.")
    p_d("Faced with conquest, your nation, Adar, took an unprecedented step.")
    p_d("You surrendered without a fight.")
    p_d("The reason why is a tightly-guarded secret.")
    p_d("To gain the Imperium’s trust, your leaders sacrificed their pride.")
    p_d("Trusted as collaborators, chosen Adari would rise in Imperial ranks.")
    p_d("In time, they would strike decisively from within.")
    p_d("Now, perhaps, that time has come.\n")
    p_d("You are one of Adar’s secret agents.")
    p_d("Until today, you’ve served minor Khell bureaucrats.")
    p_d("Spying in the shadows. Reporting to the hidden leaders of Adar.")
    p_d("From the Imperial perspective, your record has been excellent.")
    p_d("But one thing always held you back in the eyes of the Khell.")
    p_d("Your open interest in the language and customs of your own people.")
    p_d("The ruling sorcerers profess the superiority of their culture.")
    p_d("All official business takes place in the Khell language.")
    p_d("Knowledge of Adari ways is disdained in the Imperial bureaucracy...")
    p_d("...so most infiltrators hide their interest in such things.\n")
    p_d(f"But you, {NAME}... You’re different.")
    p_d("You feel that serving your people in secret...")
    p_d("...doesn’t mean you have to openly disavow their past.")
    p_d("On free days, you wear Adari clothes, not the Imperial style.")
    p_d("You also let yourself be seen reading Adari books.")
    p_d("This has occasioned questions from the Khell, some of them sharp.")
    p_d("But your service is exceptionally competent.")
    p_d("You seem loyal to the Imperium in every other way.")
    p_d("As such, your strange proclivities haven’t landed you in jail...")
    p_d("...with the few remaining Adari dissidents.")
    p_d("However, your career has advanced slowly.")
    p_d("You've been limited to serving lesser Khell.\n")
    p_d("Until now.\n")
    p_d("BRIEFING FINISHED.\n")


def show_how_to_play():
    """
    Called from within start_game to print gameplay info.
    """
    p_d("GAMEPLAY\n")
    p_d("Once your mission begins, read story text...")
    p_d("...then choose options from a numbered list.")
    p_d("To choose an option, type its number (e.g. 1), then press ENTER.")
    p_d("Some choices will add or remove items from your inventory.")
    p_d("Some choices will increase or decrease your statistics.\n")
    p_d("INVENTORY\n")
    p_d("As a spy, choosing which equipment to carry is important.")
    p_d("There may be times when the best choice is none at all.\n")
    p_d("STATISTICS (hereafter, stats) \n")
    p_d("As a spy, your duty is to gather information.")
    p_d("You’ll need trust to maintain your cover.")
    p_d("But your efforts to gain trust...")
    p_d("...may strengthen the grasp of Khell rulership on your people.\n")
    p_d("You have two known stats: Information, and Governor's Legitimacy.")
    p_d("You will be told when you gain or lose either of these stats.")
    p_d("Information starts at 0.")
    p_d("Bringing Information to high levels will empower the Adari to act.")
    p_d("Governor's Legitimacy starts at 3.")
    p_d("It’s hard to know what effects high or low Legitimacy may have.\n")
    p_d("You have two hidden stats: Governor’s Trust, and Prefect’s Trust.")
    p_d("You will not be told explicitly when you gain or lose Trust.")
    p_d("Due to your established reputation, both forms of Trust start at 5.")
    p_d("Bringing trust to high levels will open new possibilities.")
    p_d("If either form of Trust reaches 0, there will be... consequences.\n")
    p_d("If you survive to the end of your mission...")
    p_d("...these stats will determine its possible outcomes.\n")
    p_d("SETTINGS and DEV TOOLS\n")
    p_d("To access Settings, input 'S' or 'Settings' at any choice prompt.")
    p_d("In Settings, you can change text speed, see your current...")
    p_d("...inventory and known stats, and access a glossary.\n")
    p_d("To access Dev Tools, input 'T' or 'Tools' at any choice prompt.")
    p_d("Dev Tools exist to help you test the game, should you so wish.")
    p_d("They are not recommended for an immersive play experience.\n")
    p_d("INFORMATION FINISHED.\n")
    input("To start your mission, input any key.")


def opening_scene():
    """
    Called from within start_game to begin the story proper.
    """
    global plot
    p_d("MISSION START...\n")
    print("┌───── •✧✵✧• ─────┐")
    print("  DAY 1: MIDNIGHT ")
    p_d("└───── •✧✵✧• ─────┘\n")
    p_d("It begins on a quiet night, before second moonrise.")
    p_d("You’re working late, searching for secrets.")
    p_d("Then you hear a band of Runeguards at the door.")
    p_d("For a moment, you wonder if you’ve been discovered.")
    p_d("Then you bury your doubts, hide your work, and greet them.\n")
    p_d("The Runeguards escort you to the Governor’s Palace.")
    p_d("From here, a sorcerer rules your people on the Emperor’s behalf.")
    p_d("This building was once the seat of Adari democracy.")
    p_d("One day, you hope, it will be again.\n")
    p_d("When you arrive, the Governor is nowhere to be seen.")
    p_d("Instead, the Prefect of the Runeguard awaits you.\n")
    p_d("The Runeguard protects the Emperor and his Governors.")
    p_d("Bestowed with imbued magic items by the sorcerers...")
    p_d("...Runeguards don’t need brute strength to be deadly.")
    p_d("Arms and raiment aside, most have the look of scholars.\n")
    p_d("The Prefect is the leader of their local cohort.")
    p_d("She carries a powerful blade granted by the Emperor himself.")
    p_d("She also has the build of a professional athelete...")
    p_d("...which may tell you everything you need to know about her.")
    p_d("At a gesture, her subordinates leave. The two of you are alone.\n")
    p_d("“Adjunct,” she greets you crisply.\n")
    p_d("That’s all anyone’s allowed to call you now.")
    p_d("In the Imperium, only the sorcerous ruling class are granted names.")
    p_d("Everyone else, including the Prefect herself, has only a title.")
    p_d("Of course, your parents did name you in secret.")
    p_d(f"In the privacy of your mind, you always call yourself {NAME}.")
    p_d("But the Khell must never know that.\n")
    p_d("How do you greet the Prefect?")
    opening_options = [
        "  1. Respectfully.",
        "  2. Neutrally.",
        "  3. Playfully."
    ]
    opening_answer = make_choice(opening_options)
    if opening_answer == "1":  # Respectfully.
        p_d("You bow. “Prefect. How may I serve?”\n")
        p_d("The Prefect nods. “You ask precisely the right question.")
        p_d("I called you here for a very important reason.”")
        # Prefect's Trust + 1
    elif opening_answer == "2":  # Neutrally.
        p_d("You give a small nod. “Prefect.”\n")
        p_d("She meets your eyes directly. “I called you here for a reason.”")
    elif opening_answer == "3":  # Playfully.
        p_d("“Prefect. This is my first nocturnal invitation to the Palace.")
        p_d("Forgive me if I don't quite know what to do.” You smile.\n")
        p_d("The Prefect frowns, unamused. “My time is precious, Adjunct.")
        p_d("Don’t waste it. I called you here for a reason, after all.”")
        # Prefect's Trust - 1
    p_d("The Prefect gestures to the empty desk behind her.")
    p_d("“By the will of Xeth, Emperor of the Khell and their subjects...")
    p_d("...the Governor has been recalled. The new one comes tomorrow.”\n")
    p_d("Imperial Governors are rarely replaced, and never so quickly.")
    p_d("Your mind races as you wonder what to make of this.\n")
    p_d("“This is where you come in,” the Prefect states.")
    p_d("“The new Governor, Ekkano, has requested... a cultural advisor.")
    p_d("It’s not my place to question his wishes.")
    p_d("It merely falls on me to choose someone. I choose you.”\n")
    p_d("What do you say?")
    advisor_options = [
        "  1. “I am honoured, Prefect. Of course I accept.”",
        "  2. “I don’t understand. Why me?”",
        "  3. “I cannot do this.”"
    ]
    advisor_answer = make_choice(advisor_options)
    if advisor_answer == "1":  # Of course I accept.
        p_d("You think you glimpse a predatory gleam in her eyes.")
        p_d("“Excellent. I’m glad you didn’t disappoint me.”\n")
    elif advisor_answer == "2":  # Why me?
        p_d("“I hope you’re merely being polite,” she says.")
        p_d("“It should be obvious. You’re the only trustworthy servant...")
        p_d("...of the Imperium who fosters Adari traditions.")
        p_d("Others with such knowledge and skills are dangerous rebels.")
        p_d("Would you have me scour our prisons for an advisor?")
        p_d("I can’t inflict a ruffian on Governor Ekkano.”")
        p_d("It’s clear that she means for you to play this role.")
        p_d("She won’t take no for an answer.\n")
    elif advisor_answer == "3":  # I cannot do this.
        p_d("She shakes her head. “You can. And you will.")
        p_d("As we are commanded, so we all must obey.”")
        p_d("She won’t take no for an answer.\n")
    p_d("For a moment, in silence, you reflect on your new orders.")
    p_d("Working at a Governor’s side will be dangerous.")
    p_d("But it’s an unprecedented chance to gain vital information.\n")
    p_d("Then the Prefect says: “There is... one other thing.”")
    p_d("“A Governor’s life is dangerous. We Runeguards do what we can...")
    p_d("...but we fight an uphill battle. The Imperium has many foes.”\n")
    p_d("You make your face the blankest possible mask.\n")
    p_d("“I need your help, Adjunct,” she says. “To protect the Governor.")
    p_d("Report to me on every detail you witness in his company.")
    p_d("No matter how inconsequential.”\n")
    p_d("And, with that, all the pieces click into place.\n")
    p_d("You’ve been in the spy game long enough to know what’s happening.")
    p_d("Governors are second only to the Emperor in authority...")
    p_d("...yet the Prefect is demanding that you spy on Ekkano for her.")
    p_d("This has... implications.\n")
    p_d("Of course, you would have spied on him for the Adari.")
    p_d("But the Prefect too? That’s a dangerous dance.")
    p_d("It’s hard enough being an agent, without being a double agent.\n")
    p_d("What do you say?")
    spy_questioned = False
    spy_refused = False
    spy_refuse_again = False
    spy_options = [
        "  1. “I fully understand. I will do as you command.”",
        "  2. “Will Governor Ekkano know I’m reporting to you?”",
        "  3. “You’re asking me to be a spy. I won’t do that.”"
    ]
    spy_answer = make_choice(spy_options)
    if spy_answer == "1":  # I will do it.
        p_d("She nods. “Good. Your obedience will be rewarded.”\n")
        # Prefect's Trust + 1
    elif spy_answer == "2":  # Will he know?
        p_d("“No,” she says flatly. Then, grimacing, she elaborates.")
        p_d("“He’s a proud man. And why not? Spells can handle most threats.")
        p_d("But not everything. Those concerns fall to the Runeguard.")
        p_d("We don’t trouble Governors with minor security matters.")
        p_d("And neither should you.”")
        p_d("Although you’re alone, she lowers her voice.")
        p_d("“Keep your observations strictly secret.")
        p_d("Tell no one but me.”\n")
        spy_questioned = True
    elif spy_answer == "3":  # I will not be a spy.
        p_d("Her lip curls in contempt. “Be careful what you say, Adjunct.")
        p_d("I have asked no such thing. My order is perfectly legitimate.”\n")
        spy_refused = True
        # Prefect's Trust - 1
    if spy_questioned:
        print("What do you say?")  # Following spy answer 2
        spy_query_options = [
            "  1. “I fully understand. I will do as you command.”",
            "  2. “You’re asking me to be a spy. I won’t do that.”"
            ]
        spy_query_answer = make_choice(spy_query_options)
        if spy_query_answer == "1":  # I will do it.
            p_d("She nods. “Good. Your obedience will be rewarded.”\n")
            # Prefect's Trust + 1
        elif spy_query_answer == "2":  # I will not be a spy.
            p_d("Her lip curls in contempt. “Mind what you say, Adjunct.")
            p_d("I’ve asked no such thing. My order is fully legitimate.”\n")
            spy_refused = True
            # Prefect's Trust - 1
    if spy_refused:
        print("What do you say?")  # Following spy_answer 3, spy_query_answer 2
        spy_refused_options = [
            "  1. “Forgive me, Prefect. I misspoke. I’ll do as you command.”",
            "  2. “I said I won’t do it.”"
            ]
        spy_refused_answer = make_choice(spy_refused_options)
        if spy_refused_answer == "1":  # Accept after all.
            p_d("She frowns. “See that you do. I’ll accept no mistakes.”\n")
            # Prefect's Trust + 1 - or not?
        elif spy_refused_answer == "2":  # Continue to refuse.
            p_d("She sighs. “What a shame. I hope you understand...")
            p_d("...your career is over if you refuse.”\n")
            spy_refuse_again = True
            # Prefect's Trust - 1
    if spy_refuse_again:
        print("What do you do?")  # Following spy_refused_answer 2
        spy_refuse_final_options = [
            "  1. Change you mind and accept.",
            "  2. Refuse nonetheless."
            ]
        spy_refuse_final_answer = make_choice(spy_refuse_final_options)
        if spy_refuse_final_answer == "1":  # Accept after all.
            p_d("You need to stay in your post, to keep serving your people.")
            p_d("Whatever her game is, you’ll have to play it.")
            p_d("“Forgive me, Prefect. I misspoke. I’ll do as you command.”\n")
            p_d("“See that you do,” she says. “I’ll be watching you.”\n")
            # No Prefect's Trust regained, she knows she had to force you
        if spy_refuse_final_answer == "2":  # Continue to refuse.
            p_d("In your career, you’ve gathered plenty of information...")
            p_d("...without actually helping the Imperium too much.")
            p_d("If you do what the Prefect wants, that’ll come to an end.")
            p_d("Helping her, or the Governor, or both of them...")
            p_d("...might undo everything your people have worked for.")
            p_d("You can’t let that happen.\n")
            p_d("If refusing ends your career, perhaps it’s for the best.")
            p_d("Maybe you’ve had enough of the spy game anyway.")
            p_d("Reaching your decision, you meet her eyes and say:")
            p_d("“So be it.”\n")
            p_d("The Prefect regards you with cold rage.")
            p_d("“You think you can refuse me and live, Adjunct?”")
            p_d("Before you can answer, she goes on:")
            p_d("“Perhaps you’re fool enough not to care for your own life.")
            p_d("But my reach is vast. If you think only you will suffer...")
            p_d("...for this disobedience, you can think again.”")
            p_d("She’ll kill you if you don’t do this. And not just you.\n")
            plot["spy_under_duress"] = True
            # Prefect's Trust reduced to nothing, can only be raised to 1 after
    if plot["spy_under_duress"]:
        print("What do you do?")  # Following spy_refused_final answer 2
        spy_try_not_to_die_options = [
            "  1. Capitulate, to save yourself and others.",
            "  2. Pretend to agree, but flee at the first oppportunity."
            ]
        spy_try_not_to_die_answer = make_choice(spy_try_not_to_die_options)
        if spy_try_not_to_die_answer == "2":  # Pretend.
            plot["spy_try_to_flee"] = True
        p_d("“I see I have no choice. As you wish, Prefect.”\n")
        p_d("“It didn’t have to come to this, Adjunct,” she says.")
        p_d("“You could have cooperated freely.”\n")
        p_d("Ah, yes. That’s what freedom means, isn’t it?")
        p_d("The freedom to serve the Khell. Nothing else.\n")
        p_d("She continues: “Some guards will escort you home.")
        p_d("And back here at noon. Don’t think you can escape your duty.”\n")
        if plot["spy_try_to_flee"]:  # Because you want to attempt escape.
            p_d("So much for fleeing at the first opportunity.")
            p_d("It looks like the Prefect’s not taking any chances.")
            p_d("Still, you know how to be patient.")
            p_d("You can wait.\n")
        p_d("The Prefect calls her Runeguards from outside.")
        p_d("They line up on either side of you.")
        p_d("For now, it seems, your audience is at an end.\n")
    if not plot["spy_under_duress"]:  # Explaining the accompanying guards
        p_d("The Prefect calls her Runeguards from outside.")
        p_d("They line up on either side of you.\n")
        p_d("“For your safety, Adjunct,” she murmurs.\n")
        p_d("It seems you’ll be under more scrutiny from now on.")
        p_d("With that, it seems, your audience is at an end.\n")
    p_d("The Runeguards escort you home.")
    p_d("They stay outside while you prepare for what lies ahead.")
    p_d("You can’t use your emergency channel to Adar’s hidden leaders.")
    p_d("The guards might come in at any moment, or simply overhear.")
    p_d("So you write a message with invisible ink...")
    p_d("...and leave it in your wastepaper basket.")
    p_d("A contact should collect it within a few days.\n")
    first_morning()


def first_morning():
    """
    Lets the user choose inventory items on the first day.
    """
    global inventory
    print("┌───── •✧✵✧• ─────┐")
    print("    DAY 1: DAWN ")
    p_d("└───── •✧✵✧• ─────┘\n")
    p_d("The sun rises on your first day as a double agent.")
    p_d("You spend two hours on last-minute research, then take a timed nap.")
    p_d("When you wake, you take a stim shot and make yourself presentable.\n")
    p_d("What will you wear to the Palace?")
    clothing_options = [
        "  1. Imperial uniform.",
        "  2. Adari clothing."
    ]
    clothing_answer = make_choice(clothing_options)
    if clothing_answer == "1":  # Khell.
        p_d("The uniform is appropriate to your bureaucratic rank.")
        p_d("You wear one every work day - which is most days.")
        p_d("It signals your “loyalty” to the Khell. Or so you hope.\n")
        inventory["khell_uniform"] = 1  # Gives you a uniform
    elif clothing_answer == "2":  # Adari.
        p_d("The flowing cloth and intricate prints of the Adari...")
        p_d("...are the antithesis of the rigid formality of the Khell.")
        p_d("The new Governor wants an Adari cultural advisor.")
        p_d("Dressed like this, you’ll look the part.\n")
        inventory["adari_outfit"] = 1  # Gives you Adari clothing
    poison_query = False
    p_d("Will you bring any lethal force?")
    inventory_options = [
        "  1. None whatsoever.",
        "  2. Special poisons, disguised as fragrance sachets.",
        "  3. A traditional Adari knife, worn openly."
    ]
    inventory_answer = make_choice(inventory_options)
    if inventory_answer == "1":  # Nothing
        p_d("To seem harmless, this may be the safest option.\n")
    elif inventory_answer == "2":  # Poison
        p_d("It’s normal among Khell and Adari to wear a fragrance sachet...")
        p_d("...in an inner clothing pocket.  But more than one is unusual.")
        p_d("If searched, you may be able to pass off two as eccentricity.")
        p_d("Or maybe not.\n")
        poison_query = True  # This will later prompt poison selection
    elif inventory_answer == "3":  # Knife.
        p_d("A striking choice. It may seem fitting for your new role.")
        p_d("You attach the ceremonial sheath to your belt.\n")
        inventory["adari_knife"] = 1  # Gives you Adari knife
    if inventory["adari_knife"] == 1:
        p_d("Will you bring any other lethal force?")
        knife_chosen_options = [
            "  1. No, nothing else.",
            "  2. Special poisons, disguised as fragrance sachets."
            ]
        knife_chosen_answer = make_choice(knife_chosen_options)
        if knife_chosen_answer == "1":  # Nothing else
            p_d("So be it.\n")
        elif knife_chosen_answer == "2":  # Poison
            p_d("Many Khell and Adari wear a fragrance sachet...")
            p_d("...in an inner pocket.  But more than one is unusual.")
            p_d("If searched, you may be able to pass off two as whimsy.")
            p_d("Or maybe not.\n")
            poison_query = True  # This will later prompt poison selection
    if poison_query:
        p_d("What do you bring?")
        poison_options = [
            "  1. One sachet of poison that only works on Adari.",
            "  2. One sachet of poison that only works on Khell.",
            "  3. Two sachets of poison, one of each type.",
            "  4. On second thoughts, you don’t bring any poison."
            ]
        poison_answer = make_choice(poison_options)
        if poison_answer == "1":  # Adari poison
            p_d("Your people developed this substance in secret.")
            p_d("A little causes illness; half or more causes death.")
            p_d("You think the Khell don't even know targeted poisons exist.")
            p_d("You handle it carefully, hoping you won’t need it.\n")
            inventory["adari_poison"] = 1  # Gives you Adari poison
        elif poison_answer == "2":  # Khell poison
            p_d("Your people developed this substance in secret.")
            p_d("A little causes illness; half or more causes death.")
            p_d("You think the Khell don't even know targeted poisons exist.")
            p_d("You don’t know if you’ll need to use this against them.")
            p_d("But better to have it than want it.\n")
            inventory["khell_poison"] = 1  # Gives you Khell poison
        elif poison_answer == "3":  # Both poisons
            p_d("Your people developed these substances in secret.")
            p_d("A little causes illness; half a sachet or more causes death.")
            p_d("You think the Khell don't even know targeted poisons exist.")
            p_d("With both Khell and Adari poisons in your possession...")
            p_d("...interesting options for trickery open up.")
            p_d("You’ll just have to make sure you’re not caught.\n")
            inventory["adari_poison"] = 1  # Gives you Adari poison
            inventory["khell_poison"] = 1  # Gives you Khell poison
        elif poison_answer == "4":  # No poison
            p_d("Perhaps you’re better off without such things.\n")
    if poison_query and inventory["adari_knife"] != 1:  # Want poison & knife?
        p_d("Will you bring any other lethal force?")
        poison_chosen_options = [
            "  1. No, nothing else.",
            "  2. A traditional Adari knife, worn openly."
            ]
        poison_chosen_answer = make_choice(poison_chosen_options)
        if poison_chosen_answer == "1":  # Nothing else
            p_d("So be it.\n")
        elif poison_chosen_answer == "2":  # Knife.
            p_d("A striking choice. It may seem fitting for your new role.")
            p_d("You attach the ceremonial sheath to your belt.\n")
            inventory['adari_knife'] = 1  # Gives you Adari knife
    p_d("Your preparations complete, you walk to your door...")
    p_d("...before the Runeguards can summon you.\n")
    governor_arrives()


def governor_arrives():
    """
    Story content for the Governor's arrival.
    """
    global inventory
    global plot
    print("┌───── •✧✵✧• ─────┐")
    print("    DAY 1: NOON ")
    p_d("└───── •✧✵✧• ─────┘\n")
    p_d("You arrive at the Governor’s Palace as the sun reaches its zenith.")
    p_d("This day is only half over. It’s already the longest of your life.")
    p_d("Runeguards escort you to the teleportation circle in the main hall.")
    p_d("Only Khell sorcerers are capable of using such things.\n")
    # Checks for Khell uniform, but no knife
    if inventory["khell_uniform"] == 1 and inventory["adari_knife"] == 0:
        if not plot["spy_under_duress"]:
            p_d("The Prefect gives you a small nod, but says nothing.")
        else:
            p_d("The Prefect looks at you disdainfully, but says nothing.")
    # Checks for Adari clothing, but no knife
    elif inventory["adari_outfit"] == 1 and inventory["adari_knife"] == 0:
        if not plot["spy_under_duress"]:
            p_d("The Prefect frowns at your Adari clothing, but says nothing.")
        else:
            p_d("The Prefect looks at your Adari clothing with disgust.")
            p_d("But she has no time to do anything about it.")
    # Checks for Khell uniform and Adari knife
    elif inventory["khell_uniform"] == 1 and inventory["adari_knife"] == 1:
        p_d("The Prefect stares at your knife. “You cannot wear that.”\n")
        p_d("What do you say?")
        knife_uniform_options = [
            "  1. “If you wish, Prefect, I’ll remove it.”",
            "  2. “What if I need it to protect the Governor?”",
            "  3. “This is a cultural symbol, worn as a gesture of respect.”",
            "  4. “Imperial uniform code permits a side-weapon.”"
            ]
        knife_uniform_answer = make_choice(knife_uniform_options)
        if knife_uniform_answer == "1":  # Acquiesce.
            p_d("“I do wish,” she says. “Hand it over, Adjunct.”")
            plot["knife_taken"] = True
            inventory["adari_knife"] = 0
        elif knife_uniform_answer == "2":  # Cite the Governor's safety.
            p_d("“You won’t,” she says. “That’s our job. Hand it over.”")
            plot["knife_taken"] = True
            inventory["adari_knife"] = 0
        elif knife_uniform_answer == "3":  # Cite culture.
            p_d("“Irrelevant,” she says. “Hand it over, Adjunct.”")
            plot["knife_taken"] = True
            inventory["adari_knife"] = 0
        elif knife_uniform_answer == "4":  # Ojbect on a technicality.
            p_d("The Prefect blinks in seeming disbelief. Then she says:")
            p_d("“Code envisages a Khell weapon. Not some trinket.”\n")
            if not plot["spy_under_duress"]:
                p_d("You reply: “Respectfully, that’s not specified.”")
                p_d("Then, daringly, you add: “I humbly submit...")
                p_d("...that such weapons, worn with Imperial dress...")
                p_d("...represent the Adari in loyal service of the Khell.”\n")
                p_d("The Prefect looks at you for a long moment.")
                p_d("Then she shrugs. “Very well. You may wear it.")
                p_d("But do not test me again, Adjunct.”")
            else:
                p_d("You reply: “Respectfully, that’s not specified.”\n")
                p_d("With a cold glare, the Prefect steps close to you.")
                p_d("Lowering her voice for your ears only, she says:")
                p_d("“You made me force this duty upon you, Adjunct.")
                p_d("Do not try to teach me the meaning of respect.”\n")
                plot["knife_taken"] = True
                inventory["adari_knife"] = 0
    # Checks for Adari clothing and Adari knife, 1 fewer option vs. uniform
    elif inventory["adari_outfit"] == 1 and inventory["adari_knife"] == 1:
        p_d("The Prefect stares at your knife. “You cannot wear that.”\n")
        p_d("What do you say?")
        knife_uniform_options = [
            "  1. “If you wish, Prefect, I’ll remove it.”",
            "  2. “What if I need it to protect the Governor?”",
            "  3. “This is a cultural symbol, worn as a gesture of respect.”"
            ]
        knife_uniform_answer = make_choice(knife_uniform_options)
        if knife_uniform_answer == "1":  # Acquiesce.
            p_d("“I do wish,” she says. “Hand it over, Adjunct.”")
            plot["knife_taken"] = True
        elif knife_uniform_answer == "2":  # Cite the Governor's safety.
            p_d("“You won’t,” she says. “That’s our job. Hand it over.”")
            plot["knife_taken"] = True
        elif knife_uniform_answer == "3":  # Cite culture.
            p_d("“Irrelevant,” she says. “Hand it over, Adjunct.”")
            plot["knife_taken"] = True
    if plot["knife_taken"]:
        p_d("You have no choice but to give her the knife.")
        p_d("She hands it to a subordinate.\n")
    p_d("You gather around the teleportation circle.")
    p_d("A ripple distorts the air. Then a radiant rift opens.")
    p_d("A man steps through the portal and closes it behind him.\n")
    p_d("By his patrician Khell features and his use of magic...")
    p_d("...you know this must be Governor Ekkano.")
    p_d("But you're surprised that he comes alone.")
    p_d("You expected someone of his rank to bring a vast entourage.\n")
    p_d("Ekkano’s gaze sweeps past you all.")
    p_d("Speaking formally, he proclaims:")
    p_d("“I come to claim dominion over Adar, as granted by Xeth...")
    p_d("...Emperor of the Khell and all their subjects.”")
    p_d("He pauses, as if to let his power rest over your land.")
    p_d("Then he turns his attention to those who await him.\n")
    p_d("“Greetings, Prefect,” Ekkano says.")
    p_d("“Loyal warriors of the Runeguard...")
    p_d("...I will count on your service in the years to come.”")
    p_d("He glances at you, then back to the Prefect. “This is the one?”\n")
    p_d("“Yes, Ekkano,” she replies.\n")
    p_d("“Good,” he says.  “I’ll meet the bureaucracy tomorrow.”")
    p_d("Then he gestures in your direction. “Counsellor, with me.”")
    p_d("With that, he strides off.\n")
    p_d("“Adjunct,” the Prefect says sharply - not to you, but to Ekkano.\n")
    p_d("He stops, then slowly turns back.\n")
    p_d("“Your advisor is an Adjunct,” the Prefect clarifies.")
    p_d("You think you hear a note of fear in her voice.\n")
    p_d("Ekkano simply looks at her.\n")
    p_d("The silence stretches uncomfortably.")
    p_d("At length, the Prefect lowers her head.")
    p_d("“Was an Adjunct,” she murmurs. “But is now a Counsellor.”\n")
    knife_chat_guard = False
    knife_chat_gov = False
    knife_chat_pref = False
    if not plot["knife_taken"]:
        p_d("Ekkano nods. “Come,” he tells you, then turns to leave.")
        p_d("You follow him out.")
    else:
        p_d("Ekkano nods. Turning back, he spots the guard with your knife.")
        p_d("Looking at the weapon, he asks: “Is this Adari work?”\n")
        p_d("“Yes, Ekkano.” Bowing, the guard holds out your knife.\n")
        p_d("The Governor doesn’t take it. “Is it yours?”\n")
        p_d("“No, Ekkano. It belongs to the, uh, Counsellor.”\n")
        p_d("“I see. Then return it to the Counsellor.”\n")
        p_d("The guard bows again - and, without seeking...")
        p_d("...the Prefect’s approval, gives you back your weapon.")
        p_d("Do you say anything?\n")
        knife_back_options = [
            "  1. No - stay silent.",
            "  2. Speak to the guard who had your knife.",
            "  3. Speak to the Governor.",
            "  4. Speak to the Prefect."
            ]
        knife_back_answer = make_choice(knife_back_options)
        if knife_back_answer == "1":  # No further knife chat.
            p_d("“Come, Counsellor,” Ekkano tells you.")
            p_d("You follow him out.")
        elif knife_back_answer == "2":  # Guard.
            p_d("What do you say to the guard?")
            knife_chat_guard = True
        elif knife_back_answer == "3":  # Governor.
            p_d("What do you say to Ekkano?")
            knife_chat_gov = True
        elif knife_back_answer == "4":  # Prefect.
            p_d("What do you say to the Prefect?")
            knife_chat_pref = True
    if knife_chat_guard:
        guard_chat_options = [
            "  1. “Thank you.”",
            "  2. “As it should be.”",
            "  3. “Keep it if you wish.”"]
        guard_chat_answer = make_choice(guard_chat_options)
        if guard_chat_answer == "1":  # Thank the guard.
            p_d("The guard acknowledges you with a nod.")
            p_d("“Come, Counsellor,” Ekkano says. “There’s much to do.”")
            p_d("He turns to leave. You follow him out.")
        elif guard_chat_answer == "2":  # Be smug.
            p_d("Out of the corner of your eye, you see the Prefect twitch.")
            p_d("“Come, Counsellor,” Ekkano says. “There’s much to do.”")
            p_d("He turns to leave. You follow him out.")
        elif guard_chat_answer == "3":  # Offer knife back.
            p_d("“We’ve no time for this,” Ekkano says, turning to leave.")
            p_d("You hesitate for a moment.")
            p_d("Then you return the knife to your belt and follow him out.")
    elif knife_chat_gov:
        gov_chat_options = [
            "  1. “Thank you, Ekkano.”",
            "  2. “Thank you, Governor.”",
            "  3. “As it should be.”",
            "  4. “Far be it from me to take a weapon from the Runeguard.”"]
        gov_chat_answer = make_choice(gov_chat_options)
        if gov_chat_answer == "1":  # Use Gov name, correct protocol.
            p_d("Waving off your thanks, he turns to leave.")
            p_d("“With me, Counsellor.”\n")
            p_d("You follow him out.")
        elif gov_chat_answer == "2":  # Fail to call Gov by his name.
            p_d("You hear sharp intakes of breath all around you.\n")
            p_d("Ekkano’s gaze turns icy.")
            p_d("“I have the right to my Name. Counsellor.”\n")
            offended_gov = True
        elif gov_chat_answer == "3":  # Be smug.
            p_d("Out of the corner of your eye, you see the Prefect twitch.")
            p_d("“Come, Counsellor,” Ekkano says. “There’s much to do.”")
            p_d("He turns to leave. You follow him out.")
        elif gov_chat_answer == "4":  # Vaguely offer knife back.
            p_d("“They have enough,” he replies. “Come, there’s much to do.”")
            p_d("He turns to leave. You follow him out.")
    elif knife_chat_pref:
        pref_chat_options = [
            "  1. “My apologies, Prefect.”",
            "  2. “I’m glad we could resolve this, Prefect.”",
            "  3. “This knife will serve Ekkano well, Prefect. I promise.”"]
        pref_chat_answer = make_choice(pref_chat_options)
        if pref_chat_answer == "1":  # Say sorry to Prefect.
            p_d("“Doing Ekkano’s will requires no apology,” she replies.")
            p_d("You could almost believe she didn’t ask you to spy on him.\n")
            p_d("“Indeed,” the Governor says. “Now, Counsellor, come.”")
            p_d("He turns to leave. You follow him out.")
        elif pref_chat_answer == "2" or pref_chat_answer == "3":  # Mind-games.
            p_d("She gives you a nod that almost looks gracious.")
            p_d("But you know what’s underneath.")
            p_d("“Come,” Ekkano tells you, turning to leave.")
            p_d("You follow him out.")
    if offended_gov:
        offended_options = [
            "  1. “Of course, Ekkano. I misspoke.”",
            "  2. “Forgive me. I’ve never been in the presence of a Name.”",
            "  3. “Do you?”"]
        offended_answer = make_choice(offended_options)
        if offended_answer == "1":  # You salvage the situation.
            p_d("He nods. “Very well. Now, with me.”")
            p_d("He turns to leave, and you follow him out.")
        elif offended_answer == "2":  # Not terrible, not great.
            p_d("He doesn’t quite seem appeased. Yet he doesn’t gainsay you.")
            p_d("“We’ll speak of this later.  Now, with me.”")
            p_d("He turns to leave, and you follow him out.")
        elif offended_answer == "3":  # This is the worst thing you can say.
            p_d("Anger sweeps over his face.")
            p_d("Some of the Runeguards reach for their weapons.")
            p_d("But the Governor looks at the Prefect...")
            p_d("...and gives her a firm shake of his head.")
            p_d("She raises her hand, and the guards relax.\n")
            p_d("Ekkano says: “I hope you’re not as ignorant of Adari ways...")
            p_d("...as you are of the Khell. Or I will have no use for you.”")
            p_d("He tells the Prefect: “Assemble a list of other candidates.”")
            p_d("Then he sweeps out of the room.\n")
            p_d("For a moment, you pause, frozen.")
            p_d("Then you follow him, lengthening your stride to keep up.")
            # Gov Trust -2
            # Legitimacy -1
            # To some, the governor seems weak for not punishing this insult
    cultural_advice()


def cultural_advice():
    """
    Story content in which the Governor seeks cultural advice
    """
    p_d("As far as you know, Ekkano has never been in Adar...")
    p_d("...let alone in the Governor’s Palace.")
    p_d("Yet he walks straight to his quarters, without needing directions.\n")
    p_d("On arriving, he shuts the door behind you with a minor spell.")
    p_d("You try not to let his casual use of magic unsettle you.")
    p_d("He pauses for a moment, as if listening to something you can’t hear.")
    p_d("Then he nods, seeming satisfied.")
    p_d("")
    p_d("")
    p_d("")


def start_game():
    """
    Begins a new game, called at the end of run.py.

    Prints the game logo.
    Lets the user choose whether to play the game.
    If the user declines: acknowledges this.
    If the user chooses to play: asks for the user's name;
    lets the user choose whether to read establishing text;
    lets the user choose where to read gameplay info;
    and begins the story proper.
    """
    print('''\033[38;2;104;95;143m
██████╗  ██████╗ ██╗   ██╗██████╗ ██╗     ███████╗ \033[38;2;114;117;160m
██╔══██╗██╔═══██╗██║   ██║██╔══██╗██║     ██╔════╝ \033[38;2;124;139;176m
██║  ██║██║   ██║██║   ██║██████╔╝██║     █████╗   \033[38;2;134;154;178m
██║  ██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝   \033[38;2;144;169;180m
██████╔╝╚██████╔╝╚██████╔╝██████╔╝███████╗███████╗ \033[38;2;194;224;233m
╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝ \033[38;2;194;224;233m
                                                   \033[38;2;170;198;208m
     █████╗  ██████╗ ███████╗███╗   ██╗████████╗   \033[38;2;144;169;180m
    ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝   \033[38;2;134;154;178m
    ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║      \033[38;2;124;139;176m
    ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║      \033[38;2;114;117;160m
    ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║      \033[38;2;104;95;143m
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝\033[0m\n''')
    play_chosen = False
    game_declined = False
    while not play_chosen and not game_declined:
        play_choice = get_string("Agent, do you wish to play? (Y/N):")
        if play_choice.lower() == 'yes' or play_choice.lower() == "y":
            p_d("Welcome to a game of swords, sorcery, and spies.")
            play_chosen = True
        elif play_choice.lower() == 'no' or play_choice.lower() == "n":
            p_d("Acknowledged.")
            p_d("If you cannot say no, then your yes has no meaning.")
            p_d("Farewell, Agent.")
            play_chosen = True
            game_declined = True
        else:
            print("It’s a yes or no question.")
    global NAME
    name_chosen = False
    while not name_chosen and not game_declined:
        NAME = get_string("Agent, what is your name?")
        if NAME:
            print("")
            p_d(f"{NAME}, you come to the crossroads of your life.")
            p_d("Tread carefully or boldly. See where your steps take you.\n")
            name_chosen = True
    read_brief = False
    while not read_brief and not game_declined:
        brief_choice = get_string("Do you wish to read a briefing? (Y/N):")
        if brief_choice.lower() == 'yes' or brief_choice.lower() == "y":
            show_briefing()
            read_brief = True
        elif brief_choice.lower() == 'no' or brief_choice.lower() == "n":
            read_brief = True
            p_d("Briefing declined.\n")
        else:
            print("It’s a yes or no question.")
    read_gameplay = False
    while not read_gameplay and not game_declined:
        info_choice = get_string("Do you wish to know how to play? (Y/N):")
        if info_choice.lower() == 'yes' or info_choice.lower() == "y":
            show_how_to_play()
            read_gameplay = True
        elif info_choice.lower() == 'no' or info_choice.lower() == "n":
            read_gameplay = True
            p_d("Information declined.\n")
        else:
            print("It’s a yes or no question.")
    if not game_declined:
        opening_scene()


start_game()
