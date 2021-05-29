#First Bank USSD
print ("Kindly enter your bank USSD")
option= input("")
if (option== "*894#"):
    print("1.Quick Banking\n2.Open an Account\n3.Loans\n4.First Monie. Next")
else: print("It's like you dialed a Wrong code!\n'*894#' is the First Bank USSD code")
option = input("")
if (option == "1"):
	print("1.Transfer Money\n2.Airtime self\n3.Airtime others\n4.Enquiry Services\n5.Data\n6.Pay Bills\n7.Next Page")
if(option=="2"):
	print("You have a FirstBank Account")
if(option=="3"):
	print("First Advance")
if(option=="4"):
	print("Link Account to FirstMonie wallet")
option=input("")
if(option=="1"):
	print("Enter Amount")
if(option=="2"):
	print("Enter Amount")
if(option=="3"):
	print("Enter Amount")
if(option=="4"):
	print("1.Balance enquiry\n2.BVN enquiry\n3. Account Number enquiry\n4.Mini statement")
if(option=="5"):
	print("1.Self\n2.Third party")
if(option=="6"):
	print("1.CableTV\n2.Electricity\n3.Renewable Energy\n4.Gifts and Reward\n5.Inveatment and Insurance\n6.Next page")
if(option=="7"):
	print("1.Insurance\n2.Other Services\n3.Merchant Services\n4.Card control\n5.Reserve cash\n6.Prev page")