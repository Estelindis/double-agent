"""
Project Portfolio 3 (Python): "Double Agent"
Developed and written by Siobhán Mooney, April 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
"""

import time

delay_time = 1

stats = {
    "information": 0,
    "legitimacy": 3,
    "trust_gov": 5,
    "trust_pref": 5
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
    Print a line of text, then delay for delay_time.

    The function name is abbreviated to permit longer text strings.
    For clarity: p_d stands for "print, delay."
    Standard delay, as stored in the global variable delay_time, is 2 seconds.
    This delay can be quickened or slowed via Settings.
    Adapted from a function by Deanna Carina:
    https://github.com/DeannaCarina/StarTrekTimeLoop
    """
    print(text)
    delay = delay_time
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
        if input_string:
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
    p_d("...doesn’t mean openly disavowing their past.")
    p_d("On free days, you wear Adari clothes, not the Imperial style.")
    p_d("You also let yourself be seen reading Adari books.")
    p_d("This has occasioned questions from the Khell, some of them sharp.")
    p_d("But your service is exceptionally competent.")
    p_d("You seem loyal to the Imperium in every other way.")
    p_d("As such, your strange proclivities haven’t landed you in jail...")
    p_d("...with the few remaining Adari dissidents.")
    p_d("However, your career has advanced slowly.")
    p_d("You've been limited to serving lesser Khell.")
    p_d("Until now.\n")


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


def opening_scene():
    """
    Called from within start_game to begin the story proper.
    """
    p_d("MISSION START...\n")
    p_d("DAY 1: MIDNIGHT")
    p_d("    ﾟ°*★*°ﾟ    ")
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
    p_d("...which may tell you everything you need to know about her.\n")
    p_d("At a gesture, her subordinates leave, and the two of you are alone.")
    p_d("“Adjunct,” she greets you crisply.")
    p_d("That’s all anyone’s allowed to call you now.")
    p_d("In the Imperium, only the sorcerous ruling class are granted names.")
    p_d("Everyone else, including the Prefect herself, has only a title.")
    p_d("Of course, your parents did name you in secret.")
    p_d(f"In the privacy of your mind, you always call yourself {NAME}.")
    p_d("But the Khell must never know that.")
    p_d("How do you greet the Prefect?")
    opening_options = [
        "  1. Respectfully.",
        "  2. Neutrally.",
        "  3. Playfully."
    ]
    opening_answer = make_choice(opening_options)
    if opening_answer == "1":  # Respectfully.
        p_d("You bow. “Prefect. How may I serve?”")
        p_d("The Prefect nods. “You ask precisely the right question.")
        p_d("I called you here for a very important reason.”")
        # Prefect's Trust + 1
    if opening_answer == "2":  # Neutrally.
        p_d("You give a small nod. “Prefect.”")
        p_d("She meets your eyes directly. “I called you here for a reason.”")
    if opening_answer == "3":  # Playfully.
        p_d("“Prefect. This is my first nocturnal invitation to the Palace...")
        p_d("...Forgive me if I don't quite know what to do.” A slight smirk.")
        p_d("The Prefect frowns, unamused. “My time is precious, Adjunct...")
        p_d("...Make sure you don’t waste it.")
        p_d("I called you here for a reason, after all.”")
        # Prefect's Trust - 1
    p_d("The Prefect gestures to the empty desk behind her.")
    p_d("“By the will of Xeth, Emperor of the Khell and their subjects...")
    p_d("...the old Governor has been recalled. The new one comes tomorrow.”")
    p_d("Imperial Governors are rarely replaced, and never so quickly.")
    p_d("Your mind races as you wonder what to make of this.")
    p_d("“This is where you come in,” the Prefect states.")
    p_d("“The new Governor, Ekkano, has requested... a cultural advisor.")
    p_d("It’s not my place to question his wishes.")
    p_d("It merely falls on me to choose someone. I choose you.”")
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
    if advisor_answer == "2":  # Why me?
        p_d("“I hope you’re merely being polite,” she says.")
        p_d("“It should be obvious. You’re the only trustworthy servant...")
        p_d("...of the Imperium with the necessary knowledge and skills.")
        p_d("Others who foster Adari traditions are dangerous rebels.")
        p_d("I can’t inflict such ruffians on Governor Ekkano.”")
        p_d("It’s clear that she means for you to play this role.")
        p_d("She won’t take no for an answer.\n")
    if advisor_answer == "3":  # I cannot do this.
        p_d("She shakes her head. “You can. And you will.")
        p_d("As we are commanded, so we all must obey.”")
        p_d("She won’t take no for an answer.\n")
    p_d("For a moment, in silence, you reflect on your new orders.")
    p_d("Working at a Governor’s side will be dangerous.")
    p_d("But it’s an unprecedented chance to gain vital information.\n")
    p_d("Then the Prefect says: “There is... one other thing.”")
    p_d("You listen, carefully controlling your expression.")
    p_d("“A Governor’s life is dangerous. We Runeguards do what we can...")
    p_d("...but we fight an uphill battle. The Imperium has many foes.”")
    p_d("You make your face the blankest possible mask.\n")
    p_d("“I need your help, Adjunct,” she says. “To protect the Governor.")
    p_d("Report to me on every detail you witness in his company.")
    p_d("No matter how inconsequential.”\n")
    p_d("And, with that, all the pieces click into place.\n")
    p_d("You’ve been in the spy game long enough to know what’s happening.")
    p_d("Governors are second only to the Emperor in authority...")
    p_d("...yet the Prefect is demanding that you spy on Ekkano for her.")
    p_d("This has... implications.\n")
    p_d("Of course, you were already going to spy on him for the Adari.")
    p_d("But the Prefect too? That’s a dangerous dance.")
    p_d("It’s hard enough being an agent, without being a double agent.\n")
    p_d("What do you say?")
    spy_questioned = False
    spy_refused = False
    spy_refuse_again = False
    spy_under_duress = False
    spy_options = [
        "  1. “I fully understand. I will do as you command.”",
        "  2. “Will Governor Ekkano know I’m reporting to you?”",
        "  3. “You’re asking me to be a spy. I won’t do that.”"
    ]
    spy_answer = make_choice(spy_options)
    if spy_answer == "1":  # I will do it.
        p_d("She nods. “Good. Your obedience will be rewarded.”")
        # Prefect's Trust + 1
    if spy_answer == "2":  # Will he know?
        p_d("“No,” she says flatly. Then, grimacing, she elaborates.")
        p_d("“He’s a proud man. And why not? Spells can handle most threats.")
        p_d("But not everything. Those concerns fall to the Runeguard.")
        p_d("We don’t trouble Governors with minor security matters.")
        p_d("And neither should you.”")
        p_d("Although you’re alone, she lowers her voice.")
        p_d("“Keep your observations strictly secret.")
        p_d("Tell no one but me.”")
        spy_questioned = True
    if spy_answer == "3":  # I will not be a spy.
        p_d("Her lip curls in contempt. “Be careful what you say, Adjunct.")
        p_d("I have asked no such thing. My order is perfectly legitimate.”")
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
            p_d("She nods. “Good. Your obedience will be rewarded.”")
            # Prefect's Trust + 1
        if spy_query_answer == "2":  # I will not be a spy.
            p_d("Her lip curls in contempt. “Mind what you say, Adjunct.")
            p_d("I’ve asked no such thing. My order is perfectly legitimate.”")
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
            p_d("She frowns. “See that you do. I’ll accept no mistakes.”")
            # Prefect's Trust + 1 - or not?
        if spy_refused_answer == "2":  # Continue to refuse.
            p_d("She sighs. “What a shame. I hope you understand...")
            p_d("...your career is over if you refuse.”")
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
            p_d("“Forgive me, Prefect. I misspoke. I’ll do as you command.”")
            p_d("“See that you do,” she sneers. “I’ll be watching you.”")
            # No Prefect's Trust regained, she knows she had to force you
        if spy_refuse_final_answer == "2":  # Continue to refuse.
            p_d("In your career, you’ve gathered plenty of information...")
            p_d("...without actually helping the Imperium too much.")
            p_d("If you do what the Prefect wants, that’ll come to an end.")
            p_d("Helping her, or the Governor, or both of them...")
            p_d("...might undo everything your people have worked for.")
            p_d("You can’t let that happen.\n")
            p_d("If refusing ends your career, perhaps it’s for the best.")
            p_d("Maybe you’ve had enough of the spy game anyway.\n")
            p_d("Reaching your decision, you look straight in her eyes.")
            p_d("“So be it.”\n")
            p_d("The Prefect regards you with cold rage.")
            p_d("“You think you can refuse me and live, Adjunct?”")
            p_d("Before you can answer, she goes on:")
            p_d("“Perhaps you’re fool enough not to care for your own life.")
            p_d("But my reach is vast. If you think only you will suffer...")
            p_d("...for this disobedience, you can think again.”")
            p_d("She’ll kill you if you don’t do this. And not just you.")
            spy_under_duress = True
            # Prefect's Trust reduced to nothing, can only be raised to 1 after
    if spy_under_duress:
        print("What do you do?")  # Following spy_refused_final answer 2
        spy_try_not_to_die_options = [
            "  1. Capitulate, to save yourself and others.",
            "  2. Pretend to agree, but flee at the first oppportunity."
            ]
        spy_try_not_to_die_answer = make_choice(spy_try_not_to_die_options)
        if spy_try_not_to_die_answer == "2":  # Pretend.
            global SPY_TRY_TO_FLEE
            SPY_TRY_TO_FLEE = True
        p_d("“I see I have no choice. As you wish, Prefect.”")
        p_d("“It didn’t have to come to this, Adjunct,” she sneers.")
        p_d("“You could have cooperated freely.”")
        p_d("Ah, yes. That’s what freedom means, isn’t it?")
        p_d("The freedom to serve the Khell. Nothing else.")
        p_d("She continues: “Some guards will escort you home.")
        p_d("And back here at noon. Don’t think you can escape your duty.”\n")
        if SPY_TRY_TO_FLEE:  # Because you chose to attempt escape.
            p_d("So much for fleeing at the first opportunity.")
            p_d("It looks like the Prefect’s not taking any chances.")
            p_d("Still, you know how to be patient.")
            p_d("You can wait.\n")
        p_d("The Prefect calls her Runeguards from outside.")
        p_d("They line up on either side of you.")
        p_d("For now, it seems, your audience is at an end.\n")
    if not spy_under_duress:  # Explaining the accompanying guards
        p_d("The Prefect calls her Runeguards from outside.")
        p_d("They line up on either side of you.")
        p_d("“For your safety, Adjunct,” she murmurs.")
        p_d("It seems you’ll be under more scrutiny from now on.")
        p_d("With that, it seems, your audience is at an end.\n")
    p_d("The Runeguards escort you home.")
    p_d("They stay outside while you prepare for what lies ahead.\n")
    first_morning()


def first_morning():
    """
    Lets the user choose inventory items on the first day.
    """
    p_d("DAY 1: DAWN")
    p_d("    ﾟ°*★*°ﾟ    ")
    p_d("The sun rises on your first day as a double agent.")
    p_d("With the Runeguards outside, your options are limited.")
    p_d("")
    p_d("")
    p_d("")
    p_d("")
    p_d("")
    p_d("")
    p_d("")
    p_d("")
    p_d("")


def governor_arrives():
    """
    Story content for the Governor's arrival.
    """
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
            p_d("Briefing finished.")
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
            p_d("Information finished.\n")
        elif info_choice.lower() == 'no' or info_choice.lower() == "n":
            read_gameplay = True
            p_d("Information declined.\n")
        else:
            print("It’s a yes or no question.")
    if not game_declined:
        opening_scene()


start_game()
