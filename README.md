# Double Agent - Project Portfolio 3 - Python
## by Siobhán Mooney

### [Click here to view the deployed app.](https://double-agent.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/double-agent)

![Initial screenshot.](/assets/image-readme/screenshot01.jpg)

# Table of Contents:
1. [About the project](#about-the-project)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [Narrative and Visual Design](#design-and-visual-design)
    1. [Narrative](#narrative)
    2. [Typography](#typography)
    3. [Colours](#colours)
3. [Code Design](#code-design)
    1. [Text Input and Display](#text-input-and-display)
    2. [Story Functions](#story-functions)
    3. [Savegame System](#savegame-system)
4. [Data Model](#data-model)
5. [Testing, Bugs, and Fixes](#testing-bugs-and-fixes)
6. [Future Features](#future-features)
7. [Deployment](#deployment)
8. [Used technologies and credits](#used-technologies-and-credits)
    1. [Languages](#languages)
    2. [Python Libraries](#python-libraries)
    3. [Other Technologies](#other-technologies)
    4. [Credits](#credits)


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
As the project is intended to demonstrate Python principles, only minor edits have been made to the standard visual styling of the terminal's webpage. More time and attention have been dedicated to the principles of narrative design that emerge through the game's story.

## Narrative
- Design text here.

## Typography
- The most striking visual element of the game is the starting logo. The ascii art was generated via [http://patorjk.com/](http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Double%0A%20Agent). This particular ascii "font" was chosen for its readability and because the shadow effect evokes the "double" aspect of the "Double Agent" title.

## Colours
- A gradient for the logo was generated via patorjk.com's [text colour fader utility](http://patorjk.com/text-color-fader/). As this utility generates HTML gradients, it was converted to Python manually, changing HEX values to RGB and following the guidelines under the heading ["ALL THE COLOURS" on Stack Overflow](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences). The particular colours of the gradient were chosen to suggest a metallic gleam, lit by purple light.  This combination unifies the cold hardness of the espionage genre with the otherworldly aura of the fantasy genre, as appropriate to a story of "swords, sorcery, and spies."
- The colour of the "run program" button was changed to match the purple part of the game logo gradient.
- The background colour of the webpage was changed to a dark grey to reduce eye strain and complement the other game colours. A pure black background was not used, to ensure that the black terminal does not seem to merge with the background. It is intended the the user's attention should be drawn to the terminal rather than wandering around the page. A background graphic, edited to match the colours of the logo, was tested. This graphic was not retained in the final version, as it was deemed distracting - literally, but also in a broader game design sense, as time could be spent on code than improving the background graphic. In a scenario with more development time, this decision could be revisited.

![Initial screenshot.](/assets/image-readme/background_test.jpg)

# Code Design
Functions are designed with a view to forwards and backwards compatibility. Returning users with savegames from previous versions should be able to continue their story from where they left (or close). Future developers should be able to add further story content without writing new non-story functions.

## Text Input and Display
- The "get_string" function performs the first step in validating user input, screening for empty strings and excessive whitespace.
- The "make_choice" function uses "get_string" while further validating user input. It continues to run until it can return an input number associated with a option. Valid input depends on how many options are offered. See [below](#story-functions) for further comments on this function.
- The "p_d" function (which stands for "print, delay") prints a string followed by a delay. The conventionally suboptimal choice of a very short function name was made to enable longer text strings to be printed, as line lengths in Python (and the dimensions of the terminal) are quite restrictive for a text-based game. The idea to abbreviate the name of the function came from [Star Trek: Time Loop](https://github.com/DeannaCarina/StarTrekTimeLoop) by DeannaCarina. However, DeannaCarina's "P_S" function accepts two parameters: text and delay. Each string to be printed has its own individual delay. "Double Agent" instead controls the delay via a single value: "text_speed" in the "game" dictionary. This value is easily changed, after which all print-delayed strings use the new speed. As well as offering central control, this approach reduces the work that developers need to do when writing print-delayed strings.
- The "change_speed" function allows the user to choose one of four speeds for the print delay implemented by "p_d". The first three speed options are intended for text that is read as it is printed, offering a comfortable experience for users with a variety of reading speeds. The final speed option, for a 0.1 second delay, can be used to speed-run the game for testing purposes. It also offers a different way of reading story text: the text is printed extremely quickly, then read. The "pause" function is crucial to making this setting useful to ordinary users, as it would be irritating to have to scroll back up every time more than a terminal's worth of text is printed between user choices.
- The "pause" function allows the user to decide when to let the text resume scrolling.  As the pause is implemented via the "getpass" library, any input except Enter is not displayed. When Enter is displayed, the pause ends.  The "delete_line" function is then called to remove the pause prompt text, for a cleaner look in the terminal.
- Via the "start_game" function, the input username can optionally be capitalized. This is optional so that any intended unusual capitalization can be preserved, if desired. When requesting the opinions of potential users on this feature, one person commented: "I would prefer not to be corrected - not because I'd particularly want to not capitalize, but because I have grown to be deeply cranky about technology trying to pre-empt and assume what I want when I didn't ask for it. I may also have just had a long afternoon of fighting with Microsoft Word." In this context, a graphic comparing product features with user needs teaches a valuable lesson. Much time can be spent on features that users do not desire - and, indeed, may actively dislike. Designers should always bear user opinions in mind (while acknowledging that users can't offer opinions about features they haven't yet imagined or encountered).

![Initial screenshot.](/assets/image-readme/features_vs_needs.jpg)

## Story Functions
- With a view to narrative cohesion, the "make_choice" function is designed for developers writing and reading user options in the story context in which said options are offered. For a game with a very short plot, story content can usefully be stored in a dictionary. However, "Double Agent" takes a different approach. Significant blocks of story text are written in addition to the choices offered to the user. It would be harder for developers to follow the flow of this story if text blocks and user choices were separated. Rather, story content is (mostly) written in the order in which the user encounters it (situations like equipment choice being the exceptions). Taking this approach, the flow of the story can be followed with ease. 
- Functions that display story text are listed in the order in which they are displayed, again to help developers track the flow of the story. With the array of functions provided, it should be possible for developers to extend the story significantly while only adding functions that display story content (following the examples established by existing story text functions).
- The function "start_game" handles whether the user wants to play the game. If the user chooses to play, the function then offers the chance to change text speed and view setting and/or gameplay info. It then calls the first story function, "opening_scene," which begins the story proper. Each subsequent story function then calls the next. The "start_game" function is called at the end of run.py. This call can easily be commented out to test other code, without starting the game.
- The "inc_game_value" function allows developers to increment (or decrement) the value of any key in the "game" dictionary, where all persistent plot info should be stored. If future versions of the game add extra key-value pairs to the "game" dictionary, developers will still be able to use this function to apply new values to the new keys. 

## Savegame System
- "Double Agent" stores plot information in the "game" dictionary. Its savegame system reads and writes these values to and from a Google Sheet. Comments on the sheet and its structure are provided [below](#data-model).
- In the functions that implement the savegame system, the number of columns to read and write is not a static range. Rather, it is determined dynamically by the number of key-value pairs in the "game" dictionary. If further key-value pairs are later added to the game, the savegame functions will not need to be updated. They will continue to read and write data from the Sheet in accordance with the newly enlarged dictionary.
- Of particular note: when a returning user chooses to load a game, the "game" dictionary is updated with their savegame data. This functionality will not be broken if the dictionary is enlarged later. Imagine a new version of the game with 22 pairs in the dictionary. If the new version loads a save that was created by the present version (which has 18 pairs), it will transfer 18 values to "game" - but the other four will remain, as defined by their default values. They will not be deleted or overwritten. 
- To ensure that version compatibility does not break, any new pairs must always be added to the end of the "game" dictionary, not inserted between existing pairs. 

# Data Model
The Google Sheet "double-agent" was used to store savegame data for "Double Agent." Data from the "game" dictionary was sent to and rewritten from "savegame," this sheet's one worksheet. Each username is assigned one row in the "name" column of the worksheet, with the user's data being stored to the columns corresponding to that row. 

![Initial screenshot.](/assets/image-readme/data_model.jpg)

![Initial screenshot.](/assets/image-readme/data_model_cropped.jpg)

# Testing, Bugs, and Fixes
Text.

# Future Features
Text.

# Deployment
Text.

# Used technologies and credits

## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Google Sheets](https://www.google.co.uk/sheets/about/)

## Python Libraries

* [GSpread](https://pypi.org/project/gspread/)
* [Time](https://docs.python.org/3/library/time.html)
* [Sys](https://docs.python.org/3/library/sys.html)

## Other Technologies
- [GitHub](https://github.com/)

## Credits
- Individal code I used.
- Individal code I used.
- Individal code I used.
- [Code Institute Slack](https://slack.com/) Fellow members of the Code Institute on Slack provided an invaluable database of information and community of support.  I am particularly grateful to the msletb-nov-2021 cohort, our facilitator Kasia, and my mentor Darío.
