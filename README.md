# Daily Chooser
 
Daily chooser is a script to select who from the team will command the daily on the day.

## How to run

```
$ git clone https://github.com/gss214/Daily-Chooser
$ cd Daily-Chooser
$ pip install -r requirements.txt
$ python daily-chooser.py
```

## How it works

First the script has an initialization to assemble the data.json file that contains data for each person on your team. The script allows you to remove people from the draw by zeroing your probability of being drawn. At each draw the odds are constrained with the probability of the winner among the people on the team for the next draw.

The settings menu allows probabilities to be reset.