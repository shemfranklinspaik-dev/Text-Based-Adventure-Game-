# Text-Based-Adventure-Game 
Text-Based Adventure Game is a console game written in Python 3. The player starts in a forest with 100 Health and 0 Score, and chooses from a menu: 1 for the Cave, 2 for the River, or 3 to Quit.

Cave: a monster attacks for random damage between 10 and 40. If the player survives, they find a key worth +20 score.
River: the player finds a treasure worth +50 score.
Game end: the game finishes when the player quits or Health reaches 0, and the final score is shown.

Every menu choice is validated. Wrong input such as 7 or abc shows an error message and costs no health.
