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
    p_d(f"But you, {name}... You’re different.")
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
    p_d("NOW YOUR MISSION BEGINS...\n")


def opening_scene():
    """
    Called from within start_game to begin the story proper.
    """
    p_d("It begins on a quiet night, before second moonrise.")
    # p_d("You’re working late, searching for secrets.")
    # p_d("Then you hear a band of Runeguards at the door.")
    # p_d("For a moment, you wonder if you’ve been discovered.")
    # p_d("Then you bury your doubts, hide your snooping, and greet them.\n")
    # p_d("The Runeguards escort you to the Governor’s Palace.")
    # p_d("From here, a sorcerer rules your people on the Emperor’s behalf.")
    # p_d("This building was once the seat of Adari democracy.")
    # p_d("One day, you hope, it will be again.\n")
    # p_d("When you arrive, the Governor is nowhere to be seen.")
    # p_d("Instead, the Prefect of the Runeguard awaits you.\n")
    # p_d("The Runeguard protects the Emperor and his Governors.")
    # p_d("Bestowed with imbued magic items by the sorcerers...")
    # p_d("...they don’t need brute strength to be deadly.")
    # p_d("Arms and raiment aside, most have the look of scholars.\n")
    # p_d("The Prefect is the leader of their local cohort.")
    # p_d("She carries a powerful blade granted by the Emperor himself.")
    # p_d("That she also has the build of a professional athelete...")
    # p_d("...tells you perhaps everything you need to know about her.\n")
    p_d("At a gesture, her subordinates leave, and the two of you are alone.")
    p_d("“Adjunct,” she greets you crisply.")
    p_d("That’s all anyone’s allowed to call you now.")
    p_d("In the Imperium, only the sorcerous ruling class are granted names.")
    p_d("Everyone else, including the Prefect herself, has only a title.")
    p_d("Of course, your parents did name you in secret.")
    p_d(f"In the privacy of your mind, you always call yourself {name}.")
    p_d("But the Khell must never know that.")
    p_d("How do you greet the Prefect?")
    opening_questions = [
        "  1. Respectfully.",
        "  2. Neutrally.",
        "  3. Playfully."
    ]
    opening_answer = make_choice(opening_questions)
    if opening_answer == "1":
        p_d("Answer 1 text.")
    if opening_answer == "2":
        p_d("Answer 2 text.")
    if opening_answer == "3":
        p_d("Answer 3 text.")
    p_d("This text is seen only after all choices are resolved.")
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
    and begins the game proper.
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
    global name
    name_chosen = False
    while not name_chosen and not game_declined:
        name = get_string("Agent, what is your name?")
        if name:
            print("")
            p_d(f"{name}, you come to the crossroads of your life.")
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
            p_d("Briefing declined.")
        else:
            print("It’s a yes or no question.")
    read_gameplay = False
    while not read_gameplay and not game_declined:
        info_choice = get_string("Do you wish to know how to play? (Y/N):")
        if info_choice.lower() == 'yes' or info_choice.lower() == "y":
            show_how_to_play()
            read_gameplay = True
            p_d("Information finished.")
        elif info_choice.lower() == 'no' or info_choice.lower() == "n":
            read_gameplay = True
            p_d("Information declined.")
        else:
            print("It’s a yes or no question.")
    if not game_declined:
        opening_scene()


start_game()
