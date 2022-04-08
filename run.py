# Project Portfolio 3 (Python): Double Agent
# Developed and written by Siobhán Mooney, April 2022.
# Code is for a terminal of 80 characters wide and 24 rows high.

import time

delay_time = 2


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
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝      
    \033[0m\n''')
