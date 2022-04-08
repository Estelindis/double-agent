# Project Portfolio 3 (Python): Double Agent
# Developed and written by Siobhán Mooney, April 2022.
# Code is for a terminal of 80 characters wide and 24 rows high.

import time

delay_time = 2


def p_d(text):
    """
    p_d stands for "print, delay"
    Print a line of text.
    Delay before the next line is printed.
    Standard delay, as stored in the global variable delay_time, is 2 seconds.
    This can be quickened or slowed via Settings.
    Adapted from a function by Deanna Carina:
    https://github.com/DeannaCarina/StarTrekTimeLoop
    """
    print(text)
    delay = delay_time
    time.sleep(delay)

