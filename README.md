# RosterLimitViolations
Checks for violations on roster limits

## Synopsis
This tool is used to check for roster size violations in the OBL.
Running it will print out a list of teams with too many players, that being:

- Teams at A-level or above with more than 27 players
- Teams below A level with more than 35 players

## Installing
To run it you need to run RosterLimitViolations.py, but you also need 3 csv
files exported from OOTP 17 and placed in the same folder:

- teams.csv
- players.csv
- team_afiliations.csv


## TODO

- Fix bug where MLB level players are overcounted
- Only display teams in MLB/MiLB
- Not all organizations have all levels down to Rookie (for example, LAA are missing
A- level)
