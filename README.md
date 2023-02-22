# Daily Chooser
 
This is a script designed to randomly select a person to run the daily in your team. The script file is located in the `src/daily-chooser.py` directory, and the `requirements.txt` file located in the project root directory contains a list of necessary dependencies needed to execute the script.

## Basics

This script implements a random selection process where each member has a probability of being chosen, with all probabilities summing up to 100%. The script provides the functionality to remove a member from the selection process, and when a member is removed, their probability is redistributed among the remaining members. The selected member has their probability set to zero, and their share of probability is distributed among the remaining members.

During the draw, the program displays an animation with the odds of each member, and at the end, the name of the chosen one is displayed. After that, the user has the option to validate the draw or restart it.

## Settings Menu

The script includes a settings menu with the following options:

- Reset Odds - Resets the odds for each member based on the number of active members (those who are not on vacation).
- Put Member on Vacation - Marks a member as being on vacation, which removes them from being selected.
- Mark a Member as Not on Vacation - Marks a member as not being on vacation, which adds them back into being selected.
- Return to the Main Menu - Returns to the main menu to select a person.

To access the settings menu, run the script and select the "Settings" option from the main menu.

For more information or suggestions, please contact the author:

E-mail: gss214@hotmail.com
