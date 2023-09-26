print("Hi, welcome to anar helpdesk bot")
# input("Hi, may I know your name?")
print("How may I help you today?")
print('''
1. My WiFi is too slow
2. My system is lagging
3. I need help with Python
4. Something else
''')
option_selected = input()

if option_selected == "1": 
    print("Please restart your router")
elif option_selected == "2":
    print("clear your temp directory then restart your system")
elif option_selected == "3":
    print("ask in the comments of this post :)")
elif option_selected == "4": 
    print("error404")
