def drunk():
    print("Hello, my name is Officer Rogers.")
    name=input("What is your name?")
    print(name,"do you know why I pulled you over? You were over the speed limit.")
    speed=int(input("Can you tell me the speed limit?"))
    driverspeed=int(input("Correct. So, can you tell me what was your speed?"))
    print(driverspeed, "Wow","that is obviously over the speed limit...and since I've pulled you over, I know the reason why.")
    print("I believe you are under the influence of alcohol. Let me get my BAC tester...here we go.")
    print("Now, after you breath into the BAC tester, tell me your BAC please.")
    BACnumber=input("What is the BAC number displayed on the tester?")
    print("Ah,", BACnumber, ".It is confirmed that you are under the influence, so I must write you a speeding ticket & charge you for your DUI.")
    print("For PA, the fine for speeding is $45 plus $2 for each mile per hour over the limit.")
    print("Since I believe this is your first DUI offense, there is an additional fine of $300. Please do not drive while being drunk again.")
    print("Have a good day.")
drunk()
