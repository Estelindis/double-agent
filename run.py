"""
Project Portfolio 3 (Python): "Double Agent"
Developed and written by Siobhán Mooney, April 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
"""

import time

delay_time = 2

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


def start_game():
    """
    Begins a new game, called at the end of run.py.

    Lets the user choose whether to play the game.
    If the user chooses to play: asks for the user's name;
    lets the user choose whether to read establishing text;
    and informs the user about Settings and Dev Tools.
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
    global name
    name = input("What is your name? \n")
    p_d("An empire led by evil sorcerers has conquered most of your world.")
    p_d("The Khell Imperium defeated every nation that resisted its advance.")
    p_d("Faced with conquest, your nation, Adar, took an unprecedented step.")
    p_d("You surrendered without a fight.")
    p_d("The reason why is a tightly-guarded secret.")
    p_d("To gain the Imperium’s trust, your leaders sacrificed their pride.")
    p_d("Trusted as collaborators, chosen Adari would rise in Imperial ranks.")
    p_d("In time, they would strike decisively from within.")
    p_d("Now, perhaps, that time has come.")
    p_d("You are one of Adar’s secret agents.")
    p_d("Until today, you’ve served minor Khell bureaucrats.")
    p_d("Spying in the shadows. Reporting to the hidden leaders of Adar.")
    p_d("From the Imperial perspective, your record has been excellent.")
    p_d("But one thing always held you back in the eyes of the Khell.")
    p_d("Your open interest in the language and customs of your own people.")
    p_d("The ruling sorcerers profess the superiority of their culture.")
    p_d("All official business takes place in the Khell language.")
    p_d("Knowledge of Adari ways is disdained in the Imperial bureaucracy...")
    p_d("...so most infiltrators hide their interest in such things.")
    p_d(f"But you, {name}... You’re different.")
    p_d("You feel that serving your people in secret...")
    p_d("...doesn’t mean you have to openly disavow their past.")
    p_d("On free days, you wear Adari clothes, not the Imperial style.")
    p_d("You also let yourself be seen reading Adari books.")
    p_d("This has occasioned questions, some of them sharp.")
    p_d("But your service is exceptionally competent.")
    p_d("You seem loyal to the Imperium in every other way.")
    p_d("As such, your strange proclivities haven’t landed you in jail...")
    p_d("...with the few remaining Adari dissidents.")
    p_d("But your career was slowed, limited to serving minor Khell.")
    p_d("Until now.")


start_game()
