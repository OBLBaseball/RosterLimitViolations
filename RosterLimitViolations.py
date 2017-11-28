#!/user/bin/python
# -*- coding: utf-8 -*_
# Title: Roster Limit Violations
# Description: Alerts runner to any teams
# violating the roster limit rule
# Date: 6/17/17
# Author: Jeffrey Zic

import csv
import fileinput
import sys

teamsByID = { '31' : 'Diamondbacks',
            '32' : 'Braves',
            '33' : 'Orioles',
            '34' : 'Red Sox',
            '35' : 'White Sox',
            '36' : 'Cubs',
            '37' : 'Reds',
            '38' : 'Indians',
            '39' : 'Rockies',
            '40' : 'Tigers',
            '42' : 'Astros',
            '43' : 'Royals',
            '44' : 'Angels',
            '45' : 'Dodgers',
            '41' : 'Marlins',
            '46' : 'Brewers',
            '47' : 'Twins',
            '48' : 'Yankees',
            '49' : 'Mets',
            '50' : 'Athletics',
            '51' : 'Phillies',
            '52' : 'Pirates',
            '53' : 'Padres',
            '55' : 'Giants',
            '54' : 'Mariners',
            '56' : 'Cardinals',
            '57' : 'Rays',
            '58' : 'Rangers',
            '59' : 'Blue Jays',
            '60' : 'Nationals'}

class Team:

    """A holder for team info"""

    def __init__(self,id,name,rosterSize,level,mlbAsso):
        """Initializes a Team.

        :param id: the team ID, mathces with team name
        :param name: the team name, matches with team id
        :param rosterSize: the current number of players on the team
        :param level: The team's level in the organization (MLB, A, etc.)
        :type id: int
        :type name: str
        :type rosterSize: int
        :type level: str
        """

        self.id = id
        self.name = name
        self.size =-rosterSize
        self.level = level
        self.mlbAsso = mlbAsso

    def display(self):
        """Displays the team info"""

        print('Name: ' + self.name)
        print('ID: ' + self.id)
        print('Size: '+ str(self.size))
        print('Level: ' + self.level)
        print('\n')

    def displayViolation(self):
        """Displays the team info if it is under violaton"""

        levels = ['MLB','AAA','AA','A+','A','A-','R']

        index = levels.index(self.level)

#        if ((index <= 4 and self.size > 27) or (index >4 and self.size > 35)) and self.level != 'MLB':
#            print('Name: ' + self.name)
#            print('ID: ' + self.id)
#            print('Size: '+ str(self.size))
#            print('Level: ' + self.level)
#            print('\n')

        if ((index <= 4 and self.size > 27) or (index >4 and self.size > 35)) and self.level != 'MLB':
            if (self.mlbAsso not in mentioned_teams):
                print('Team: ' + teamsByID[self.mlbAsso])
                mentioned_teams.append(self.mlbAsso)

teams = {}

def readTeams(file,league):
    """reads team info from csv files and stores it

    :param files: file to read with team Ids
    :param league: list of teams
    :type files: str
    :type league: Team{}
    :rtype: Team{}
    """

    levels = ['MLB','AAA','AA','A+','A','A-','R']

    with open(file, 'rb') as f:
        teamReader = csv.reader(f)

        header = teamReader.next()

        currentMLB = 0
        level = 0

        for row in teamReader:

            if int(row[0]) <= 60:
                if row[0] != currentMLB:
                    level = 0
                    currentMLB = row[0]
                    league[row[0]] = Team(row[0].rstrip('\r\n'),'',0,levels[level],row[0])
                    level += 1

                league[row[1]] = Team(row[1].rstrip('\r\n'),'',0,levels[level],row[0])

            if level < 6:
                level += 1

    return league

def nameTeams(file,league):
    """Adds name to teams

    :param file: files to read with team names
    :param league: list of teams
    :type file: str
    :type league: Team{}
    :rtype: Team{}
    """

    for i in range(len(league)):

        with open(file, 'rb') as f:
            teamReader = csv.reader(f)

            header = teamReader.next()

            for row in teamReader:

                if league.has_key(row[0]):
                    league[row[0]].name = row[1].strip('"') + ' ' + row[3].strip('"')

    return league

def countPlayers(file,league):
    """Counts number of players on each team

    :param file: file to read with players and their team
    :param league: list of teams
    :type file: str
    :type league: Team{}
    :rtype: Team{}
    """

    with open(file, 'rb') as f:

        teamReader = csv.reader(f)

        header = teamReader.next()

        for row in teamReader:

            if league.has_key(row[0]):
                if(row[2] == '1'):
                    league[row[0]].size += 1

    return league

if __name__ == '__main__':
    teams = readTeams('./team_affiliations.csv',teams)
    teams = nameTeams('./teams.csv',teams)
    teams = countPlayers('./team_roster.csv',teams)

    mentioned_teams = []

    for team in teams:
        teams[team].displayViolation()
