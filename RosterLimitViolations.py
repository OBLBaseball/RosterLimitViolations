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

class Team:

    """A holder for team info"""

    def __init__(self,id,name,rosterSize,level):
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

    def display():
        """Displays the team info"""

        print('Name: ', self.name)
        print('ID: ', self.id)
        print('Size: ', self.size)
        print('Level: ', self.level)
        print('\n')

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

    with open(file) as f:

        teamReader = csv.reader(f,delimter=',')
        currentMLB = 0
        level = 0

        for row in f:
            if row[0] != currentMLB:
                level = 0
                currentMLB = row[0]
                league[row[0]](Team.Team(row[0],'',0,levels[level]))
                level += 1
            league[row[1]](Team.Team(row[1],'',0,levels[level]))
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

        with open(file) as f:

            teamReader = csv.reader(f,delimiter=',')

            for row in f:
                league[row[0]].name = row[1].strip('"') + row[2].strip('"')

    return league

def countPlayers(file,league):
    """Counts number of players on each team

    :param file: file to read with players and their team
    :param league: list of teams
    :type file: str
    :type league: Team{}
    :rtype: Team{}
    """

    with open(file) as f:

        teamReader = csv.reader(f,delimiter=',')

        for row in f:
            if league.has_key(row[1]):
                league[row[1]].rosterSize += 1

    return league
