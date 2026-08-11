#Tip calculator
print("welcome to the tip calcucator ")
bill=int(input("enter the totel amount of the bill :"))
tip=int(input("how much tip you want to give : (10%,15%,20%)"))
per=(float(tip)/100)*bill
print(float(per))
totel_bill=bill+per
print(f"totel bill=\n {bill}+{per}={totel_bill}")

