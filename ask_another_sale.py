def ask_another_sale():
    answer_ok = False
    
    while answer_ok == False:
        answer = input("Do you want to register another sale? (y/n): ").strip().lower()

        if answer == "y" or answer == "yes":
            answer_ok = True
            return True
        elif answer == "n" or answer == "no":
            answer_ok = True
            return False
        else:
            print("Write only yes or no")