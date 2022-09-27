Blance=20000
print("******* Manu ********\n\n")

print("1.Deposite")
print("2.Withdraw\n\n")

CH=int(input("Enter Choice"))

if(CH==2):
    Login=int(input("\n\nEnter Logine Password"))

    if(Login==1234):
      profile=int(input("\n\nEnter Profile Password"))

        if(profile==5678):
            trasaction=int(input("\n\nEnter Trasaction Password"))
            if(trasaction==8910):
                debite=int(input("\n\nEnter The Amount"))
                Blance-=debite
                print("\n\n******Debited Succesfully********")
            else:
                print("Wrong Trasaction Password")
        else:
            print("Your Profile Password Is Worng")
    else:
        print("The Logine Password Is Worng")
else:
    add=int(input("\n\nEnter The Amount You Want To Amount"))
    Blance+=add
