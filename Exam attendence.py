atte=int(input("Enter your attendence"))
if atte>75:
    print("You can appear in the exams")
else:
    medical=input("Enter Y for having medical record otherwise enter N:")
    if medical=="Y":
        print("You can appear in the exams")
    else:
        print("You cannot appear in the exams")
