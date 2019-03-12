#! python3

## Mihir 
## 3/12/19
## File : mapit.py

#mapIt.py - Launches a map in the browser using an address
# from command line or clipboard

import webbrowser, sys

url = "https://www.google.com/maps/place/"

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open(url + address)
