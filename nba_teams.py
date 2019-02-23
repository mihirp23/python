#!/usr/bin/env python2

## Mihir Patel
## 2/23/19
## Program that uses NBA API to print information
## about all of the teams.
## File : nba_teams.py

from nba_api.stats.static import teams as Teams

############################################################
def main():
############################################################

    teams = Teams.get_teams()

    # go through each team
    for team in sorted(teams):
        print "-" * 60
        for key, value in team.items():
            # print all key value information
            # pertaining to teams(except id)
            if key != 'id':
                print "%-15s" % (str(key),) + ": " + str(value)

# main()

if __name__ == "__main__":
    main()
