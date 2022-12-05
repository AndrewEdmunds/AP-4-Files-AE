Repeat = "YES"
f = ""

while Repeat == "YES":
    f = open("OSICDef.dat", "r")

    # Constants
    ClaimNum = int(f.readline())
    BasicPrem = float(f.readline())
    addPremRate = float(f.readline())
    XtraLibCost = float(f.readline())
    GlassCost = float(f.readline())
    LoanCarCost = float(f.readline())
    HSTRate = float(f.readline())
    ProcessFee = float(f.readline())

    # Collecting client information
    Fname = input('First Name: ').title()
    Lname = input("Last Name: ").title()
    StreetAdd = input("Street Address: ")
    City = input("City: ")
    Province = input("Province: ")
    PostCode = input("Postal Code: ")
    PhoneNum = input("Phone Number: ")
    CarsInsured = int(input("# of Cars to be Insured: "))
    XtraLib = input("Extra Liability up to $1,000,000?(Y/N): ").upper()
    Glass = input("Glass Coverage?(Y/N): ").upper()
    LoanCar = input("Loaner Car?(Y/N): ").upper()
    PayType = input("Pay in Full or in Monthly Payment?(F/M): ").upper()
    DspName = Fname[0] + ", " + Lname

    # writing client information to a policy file
    g = open("Policies.dat", "a")
    g.write("{}".format(Fname))
    g.write(", {}".format(Lname))
    g.write(", {}".format(StreetAdd))
    g.write(", {}".format(City))
    g.write(", {}".format(Province))
    g.write(", {}".format(PostCode))
    g.write(", {}".format(PhoneNum))
    g.write(", {}".format(CarsInsured))
    g.write(", {}".format(XtraLib))
    g.write(", {}".format(Glass))
    g.write(", {}".format(LoanCar))
    g.write(", {}".format(PayType))

    # Calculations
    StartingPrem = ""
    if CarsInsured == 1:
        StartingPrem = BasicPrem
    if CarsInsured > 1:
        StartingPrem = BasicPrem + (CarsInsured - 1) * (addPremRate * BasicPrem)
    FinalPrem = StartingPrem
    if XtraLib == "Y":
        FinalPrem += XtraLibCost * CarsInsured
    if Glass == "Y":
        FinalPrem += GlassCost * CarsInsured
    if LoanCar == "Y":
        FinalPrem += LoanCarCost
    FinalWithTax = FinalPrem + (FinalPrem * HSTRate)
    FullPrice = FinalWithTax
    MonthlyPrice = (FinalWithTax + ProcessFee) / 8

    g.write(", {}\n".format(FullPrice))
    g.close()

    # Receipt
    print()
    print(f"          One Stop Insurance Company")
    print(f"Insurance Policy for: {DspName:>24}")
    print("=" * 46)
    print(f"First Name: {Fname:>34}")
    print(f"Last Name: {Lname:>35}")
    print(f"Street Address: {StreetAdd:>30}")
    print(f"City: {City:>40}")
    print(f"Province: {Province:>36}")
    print(f"Postal Code: {PostCode:>33}")
    print(f"Phone Number: {PhoneNum:>32}")
    print(f"Cars Insured: {CarsInsured:>32}")
    if XtraLib == "Y":
        print("Extra Liability Coverage:             Included")
    if XtraLib == "N":
        print("Extra Liability Coverage:         Not Included")
    if Glass == "Y":
        print("Glass Coverage:                       Included")
    if Glass == "N":
        print("Glass Coverage:                   Not Included")
    if LoanCar == "Y":
        print("Loan Car:                             Included")
    if LoanCar == "N":
        print("Loan Car:                         Not Included")
    if PayType == "M":
        print("Payment Type:                          Monthly")
    if PayType == "F":
        print("Payment Type:                             Full")
    print("=" * 46)
    print("               Insurance Quote               ")
    FullPrice = "${:,.2f}".format(FullPrice)
    print(f"Full Amount: {FullPrice:>33}")
    MonthlyPrice = "${:,.2f}".format(MonthlyPrice)
    if PayType == "M":
        print(f"Monthly Payment: {MonthlyPrice:>29}")
    print()
    print()
    print("   Policy Information Processed and Saved.   ")
    print()
    Repeat = input("Would you like to enter another policy?(YES/NO): ")



    ClaimNum += 1

    f = open("OSICDef.dat", "w")
    f.write(str(ClaimNum))
    f.write("\n{}".format(str(BasicPrem)))
    f.write("\n{}".format(str(addPremRate)))
    f.write("\n{}".format(str(XtraLibCost)))
    f.write("\n{}".format(str(GlassCost)))
    f.write("\n{}".format(str(LoanCarCost)))
    f.write("\n{}".format(str(HSTRate)))
    f.write("\n{}".format(str(ProcessFee)))

f.close()
