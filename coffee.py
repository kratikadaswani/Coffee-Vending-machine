avail={'coffee':100 , 'milk':200, 'water':150}
latte={'coffee':30 , 'milk':200, 'water':100}
cappuccino={'coffee':20 , 'milk':120, 'water':50}
espresso={'coffee':20 , 'milk':100, 'water':50}


latte_list=list(latte.values())
avail_list=list(avail.values())
cappuccino_list=list(cappuccino.values())
espresso_list=list(espresso.values())
avail_money=0
latte_money=70
espresso_money=70
cappuccino_money=70
game_on=True
secret_code=32144

def available_res(str):
    if(str=="espresso"):
        for i in range(len(espresso_list)):
         if(espresso_list[i]>avail_list[i]):
             return False
    elif(str=="cappuccino"):
        for i in range(len(cappuccino_list)):
         if(cappuccino_list[i]>avail_list[i]):
             return False    
    elif(str=="latte"):
        for i in range(len(latte_list)):
         if(latte_list[i]>avail_list[i]):
             return False 
    return True 
while game_on:
    inp=input("Hey! What would you like to have today? cappuccino/ espresso/ latte (or off to turn off the machine)\n")
    if(inp=="espresso"):
        if not available_res("espresso"):
            print("Sorry,Insufficient resources!")
            # game_on=False
        else:
            print("PLEASE,ENTER COINS")
            fifty=int(input("how many fifty coins do you have?"))
            twenty=int(input("how many twenty coins do you have?"))
            ten=int(input("how many ten coins do you have?"))
            money=(fifty*50)+(twenty*20)+(ten*10)
            if(money<espresso_money):
                print("Insufficient amount")
            else:
                avail_money+=espresso_money
                diff=money-espresso_money
                if(diff!=0):
                    print(f"here is your change {diff}coins")
                print("Here,is your Espresso. Enjoy!")
                for i in range(len(espresso_list)):
                    avail_list[i]-=espresso_list[i]
    elif(inp=="cappuccino"):
        if not available_res("cappuccino"):
            print("Sorry,Insufficient resources!")
            # game_on=False
        else:
            print("PLEASE,ENTER COINS")
            fifty=int(input("how many fifty coins do you have?"))
            twenty=int(input("how many twenty coins do you have?"))
            ten=int(input("how many ten coins do you have?"))
            money=(fifty*50)+(twenty*20)+(ten*10)
            if(money<cappuccino_money):
                print("Insufficient amount")
            else:
                avail_money+=cappuccino_money
                diff=money-cappuccino_money
                if(diff!=0):
                    print(f"here is your change {diff}coins")
                print("Here,is your cappuccino. Enjoy!")
                for i in range(len(cappuccino_list)):
                    avail_list[i]-=cappuccino_list[i]
    elif(inp=="latte"):
        if not available_res("latte"):
            print("Sorry,Insufficient resources!")
            # game_on=False
        else:
            print("PLEASE,ENTER COINS")
            fifty=int(input("how many fifty coins do you have?"))
            twenty=int(input("how many twenty coins do you have?"))
            ten=int(input("how many ten coins do you have?"))
            money=(fifty*50)+(twenty*20)+(ten*10)
            if(money<latte_money):
                print("Insufficient amount")
            else:
                avail_money+=latte_money
                diff=money-latte_money
                if(diff!=0):
                    print(f"here is your change {diff}coins")
                print("Here,is your latte. Enjoy!")
                for i in range(len(latte_list)):
                    avail_list[i]-=latte_list[i]        
    elif(inp=="report"):
        print(f"here is the report \ncoffee: {avail_list[0]}gm \nmilk: {avail_list[1]}ml \nwater: {avail_list[2]}ml")
    elif(inp=="off"):
        code=int(input("enter the secret code to turn it off!"))
        if(code==secret_code):
            game_on=False
        
        else:
            print("You cannot turn it off!")
    elif(inp=="refill"):
        coffee=int(input("Enter the amount of coffee you want to add in gm (numbers only)"))
        milk=int(input("Enter the amount of milk you want to add in ml (numbers only)"))
        water=int(input("Enter the amount of water you want to add in ml (numbers only)"))

        avail_list[0]+=coffee
        avail_list[1]+=milk
        avail_list[2]+=water

    else:
        print("Out of the menu!")



    

