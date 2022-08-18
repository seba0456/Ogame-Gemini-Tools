mode = input("Should program launch in scanning mode? (Yes or No)")
if mode ==str("Yes"):
    exec(open('Voyager.py').read())
elif mode ==str("No"):
    exec(open('Luna.py').read())
else:
    print("Unsupported")
