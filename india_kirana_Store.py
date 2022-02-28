
sum =0
print("If you want Quit calculation press 'Q' ! ")
while(True):
    UserInput = input("\nEnter item price :")
    if UserInput.lower() == 'q':
        print("Thank you for shopping with us.")
        quit()
    

    else:
        sum = sum+ float(UserInput)
        print (f"Total bill : {sum}.")
   
