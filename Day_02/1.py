"""Take input for:
- Username
- Password
-OTP

Conditions-If username is correct,check the password
-if password is correct check the OPT
-if all three are correct,print("Login Successful".)
otherwise,Print exact raeson why login failed"""

Username = input("Enter the person name:")
Password = input("Enter the password")
Otp = input("Enter the OTP")
if (Username == "Aman"):
    if (Password == "Aman12345678"):
        if(Otp == "1234"):
            print("Login successful")
        else:
            print("the Otp is not correct")
    else:
        print("The Password is not correct")            
else:
    print("The Username is not correct")

 


    


