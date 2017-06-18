#!/user/bin/python
# -*- coding: utf-8 -*_
# Title: Roster Limit Violations
# Description: Alerts runner to any teams
# violating the roster limit rule
# Date: 6/17/17
# Author: Jeffrey Zic


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
