import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])

#TODO: Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
    
