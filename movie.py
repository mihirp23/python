#!/usr/bin/env python3

###################################################################
# Author : Mihir Patel
#   Date : January 19, 2019
#   Desc : Web Scrape the front page of slickdeals and output
#          the top deals.
###################################################################

import requests, bs4

###################################################################
def main():
###################################################################
    res = requests.get('https://www.atomtickets.com/theaters/amc-garden-state-16/10415')
    res.raise_for_status()

    # passing the features argument to avoid warning
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    movies = soup.select('.production-row__title')
    for movie in movies:
        print (movie.getText())

# main()


###################################################################
if __name__ == "__main__":
###################################################################
    main()
