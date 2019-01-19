#!/usr/bin/env python3

import requests, bs4

def main():
    print("connecting to slickdeals frontpage...")
    req_obj = requests.get("https://slickdeals.net/")
    req_obj.raise_for_status()

    # passing the features argument to avoid warning
    soup_obj = bs4.BeautifulSoup(req_obj.text, features="html.parser")

    front_page_list = soup_obj.select('.itemTitle')
    for item in front_page_list:
        print (item.get('title'))

if __name__ == "__main__":
    main()

