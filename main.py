import Admin as ad
from User import Application
user=Application("rajit@gmail.com","rajit","0123456789","india","1234") #already registered user

temp1=1
temp2=True
temp3=True
while temp3 :

    inp=int(input("Where You Want to Login?? 1. Admin  2. User  3. User Registration 4. Exit "))
    if temp1 == 0:
        temp2=True

    if inp == 1:
       print("Login AS  Admin Panel..")
       username=input("Enter a Username ")
       password = input("Enter a Password ")
       if ad.admin_keys[username] == password:
        print("you Logged in .........Successfully..........")
        while temp3:
            admin_input = int(input(
                "Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW ITEM List 4.REMOVE ITEM 5.EXIT"))
            if admin_input == 1:
                ad.add_new_item()
            elif admin_input == 2:
                ad.edit_from_item()
            elif admin_input == 3:
                ad.show_inven()
            elif admin_input == 4:
                ad.remove_item()
            elif admin_input == 5:
                print(f"You're Exit to the admin panel   {username}")
                temp3 = False
            else:
                print("Wrong input")

       else :
           print("Invalid Credentials ")


    elif inp == 2 :
      print("Login As User ")
      email_enter = input("Enter a Email ")
      password = input("Enter a Password")

      if Application.login(email_enter,password):

        while temp2:
            choice_user = int(input(f"{email_enter},Enter the option 1. Place new order 2. Order history 3. Update Profile 4. Exit"))
            if choice_user == 1:
                user. place_new_order()

            elif choice_user == 2:
                user.order_history_see()

            elif choice_user ==3:
                user.update_profile()
                temp2=False
                temp1=0

            elif choice_user == 4:
                print("You're looged out")
                temp2 = False
                temp1 = 0



            else:
                print("Wrong input")

    elif inp == 3:

        new_email = input("Enter new  Email ")
        if new_email in user.login_info.keys():
            print("Email Already Registered")
        else :
           new_name = input("Enter Name ")
           new_phone_no = int(input("Enter Phone No "))
           new_Address = input("Enter Address ")
           new_password = input("Enter Password ")
           user=Application(new_email,new_name,new_phone_no,new_Address,new_password)

        print("Registration Successfully, Do login now")


    elif inp == 4:
        temp3=False
        exit()

    else :
      print("Enter valid input")












