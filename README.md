# Double Agent - Project Portfolio 3 - Python
## by Siobhán Mooney

### [Click here to view the deployed app.](https://double-agent.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/double-agent)

# Table of Contents:
1. [About the project](#about-the-project)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [Narrative and Visual Design](#design-and-visual-design)
    1. [Narrative](#narrative)
    2. [Colours](#colours)
    3. [Typography](#typography)
3. [Code Design](#code-design)
    1. [Text Input and Display](#text-input-and-display)
    2. [Story Functions](#story-functions)
    3. [Savegame System](#savegame-system)
4. [Future Development](#future-development)

# About the project
Double Agent is a text-based RPG about engaging an oppressive power structure covertly from within.

## User Goals
- Explore espionage tropes, especially those involving trust, loyalty, and hidden agendas.
- Make thematically interesting choices and experience the consequences of these choices. 
- Read story text at a comfortable speed.
- Be able to save game data, so a playthrough can be resumed later.

## Owner Goals
- Present espionage tropes, combining them with fantasy tropes in an engaging manner.
- Provide a range of choices, keeping the user guessing as to what the consequences of these choices might be.
- Give the user options for controlling the speed at which new lines of text are displayed. 
- If the terminal fills up with text, allow the user to read the text at leisure before continuing.
- Provide a savegame system, so returning users don't have to start from the beginning unless they wish.
- Create a range of Python functions that will remain useful if/when the story is expanded in future.

# Narrative and Visual Design
Overview text here.

## Narrative
- Design text here.

## Colours
- Design text here.

## Typography
- Design text here.

# Code Design
Functions are designed with a view to forwards and backwards compatibility. Returning users with savegames from previous versions of the game should be able to continue their story from where they left off. Future developers should be able to add further story content without needing to write new functions (except for the functions that display story content).

## Text Input and Display
- The "get_string" function performs the first step in validating user input, screening for empty strings and excessive whitespace.
- The "make_choice" function uses "get_string" while further validating user input. It continues to run until it can return an input number associated with a option. Valid input depends on how many options are offered. See [below](#story-functions) for further comments on this function.
- The "p_d" function (which stands for "print, delay") prints a string followed by a delay. The conventionally suboptimal choice of a very short function name was made to enable longer text strings to be printed, as line lengths in Python (and the dimensions of the terminal) are quite restrictive for a text-based game. The idea to abbreviate the name of the function came from [Star Trek: Time Loop](https://github.com/DeannaCarina/StarTrekTimeLoop) by DeannaCarina. However, DeannaCarina's "P_S" function accepts two parameters: text and delay. Each string to be printed has its own individual delay. "Double Agent" instead controls the delay via a single value: "text_speed" in the "game" dictionary. This value is easily changed, increasing or decreasing the delay after all "p_d" printed strings. As well as offering central control, this approach reduces the work that developers need to do when writing print-delayed strings.
- The "change_speed" function allows the user to choose one of four speeds for the print delay implemented by the function "p_d". The first three speed options are intended for text that is read as it is printed, offering a comfortable experience for users with a variety of reading speeds. The final speed option, for a 0.1 second delay, can be used to speed-run the game for testing purposes. It also offers a different way of reading story text: the text is printed extremely quickly, then read. The "pause" function is crucial to making this setting useful to ordinary users, as it would be irritating to have to scroll back up every time more than a terminal's worth of text is printed between user choices.
- The "pause" function allows the user to decide when to let the text resume scrolling.  As the pause is implemented via getpass, any input except Enter is not displayed. When Enter is displayed, the pause ends.  The "delete_line" function is then called to remove the pause prompt text, for a cleaner look in the terminal.

## Story Functions
- Design text here.
- With a view to narrative cohesion, the "make_choice" function is designed so that developers write (and later read) its option parameters in the story context in which said options are offered. For a game with a very short story, content can be stored in a dictionary. "Double Agent" takes a different approach, however. Significant blocks of story text are written in addition to the choices offered to the user. It would be harder for developers to follow the flow of the story if these text blocks and user choices were written as entries in lists and dictionaries. Rather, story content is (mostly) written in the order in which the user encounters it. Taking this approach, the flow of the story can be followed with each. 
- Functions that display story text are listed in the order in which they are displayed, again to help developers track the flow of the story. With the array of functions provided, it should be possible for developers to extend the story significantly while only adding functions that display story content, following the templates established by existing story text functions.

## Savegame System
- Design text here.
