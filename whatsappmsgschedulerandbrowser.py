import pywhatkit as pywk
print("")
print("WELCOME!")
print("")
print("Here are some Functions that we provide:")
print("    Functions:           Function No.")
print ("Search on YouTube           - 1")
print ("Search on Browser           - 2")
print ("Send WhatsApp message now   - 3")
print ("Schedule WhatsApp message   - 4")
print("")
while True:
    num = input("Enter the Function Number to proceed: ")

    if num == "1":
        command = input("Enter video topic to search: ")
        pywk.playonyt(command)
    elif num == "2":
        command = input("Search something online: ")
        pywk.search(command)
    elif num == "3":
        phone = input("To send a message, enter WhatsApp number (+country code): +")
        msg = input("Enter message to send: ")
        pywk.sendwhatmsg_instantly("+" + phone, msg) 
    elif num == "4":
        phone = input("To schedule a message, enter WhatsApp number (+country code): +")
        msg = input("Enter message to send: ")
        hour = int(input("Enter Hours (time - 24hr format): "))
        minute = int(input("Set Minutes: "))
        pywk.sendwhatmsg("+" + phone, msg, hour, minute)
    else:
        print("Invalid Choice! Choose from 1, 2, 3 or 4")
        continue

 

