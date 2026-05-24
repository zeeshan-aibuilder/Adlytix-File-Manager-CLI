# --------------------------------------------------------------------
#                     Mini File Management System
# --------------------------------------------------------------------
# ********************************************************************
# ====================================================================
#                   Create,Edit & delete Any file
# ====================================================================

import os
import time


def Activity_logs(action_massege):

    with open("System_logs.txt", "a") as log_file:
        current_time = time.ctime()

        log_file.write(f"\n[{current_time}] : {action_massege}")


while True:
    print("Choose What You Wanna To Do!")
    time.sleep(1)
    print("========================================================")
    print("Enter 1 To Create File")
    print("Enter 2 To Update File")
    print("Enter 3 To Delete File")
    print("Enter 4 To Search File")
    print("Enter 5 to see all files")
    print("Enter S to See Action Logs")
    print("Enter exit To ShutDown System")
    print("========================================================")

    choice = input("Enter Your Choice = ")
    # ====================================================================
    #                          File Creation
    # ====================================================================
    if choice == "1":
        nam = input("File Name = ")

        with open(nam, "w") as o_file:
            Activity_logs(f"User Created file: {nam}")
            while True:
                data = input("Enter Data = ")
                if data.lower() == "exit":
                    break
                o_file.write(data + "\n")

        ans = input("See Data? Reply (yes or No) = ")

        if ans.lower() == "yes":

            with open(nam, "r") as r_file:
                see = r_file.read()
                print(see)

    # ====================================================================
    #                            Edit Data
    # ====================================================================
    elif choice == "2":
        print("===========================================================")
        nam = input("Enter File Name = ")
        if os.path.exists(nam):
            c_data = input("Replace Sentence = ")
            n_data = input("Enter New Data = ")

            with open(nam, "r") as o_file:
                a = o_file.read()

            new_data = a.replace(c_data, n_data)

            with open(nam, "w") as u_file:
                u_file.write(new_data)

            see = input("See Updated Data? (yes/No) = ")
            if see.lower() == "yes":

                with open(nam, "r") as r_file:
                    saw = r_file.read()

                print(saw)

        else:
            print("Welcome Back!")

    # --------------------------------------------------------------------
    #                       Delete File
    # --------------------------------------------------------------------
    elif choice == "3":
        print("===========================================================")
        name = input("Enter File Name = ")
        if os.path.exists(name):
            os.remove(name)
            Activity_logs(f"User Deleted file: {name}")
            print(f"File {name} is Deleted Succesfully!")

        else:
            print(f"File {name} not found!")

    # ====================================================================
    #                           Search File
    # ====================================================================

    elif choice == "4":
        print("===========================================================")
        name = input("Enter file name = ")
        if os.path.exists(name):
            print(os.path.abspath(name))

        else:
            print(f"File {name} not found!")

    # ====================================================================
    #                           Exit Syatem
    # ====================================================================

    elif choice == "5":
        all_files = os.listdir(".")
        print("*******************************************************")
        print("-------------------------------------------------------")
        print("                      ALL Files                        ")
        print("-------------------------------------------------------")
        print("*******************************************************")

        for file in all_files:
            print(f"-> {file}")
            time.sleep(0.5)

        choi = input("Enter File Name to open = ")
        if os.path.exists(choi):
            with open(choi, "r") as r_file:
                data = r_file.read()
                print(data)

    # ====================================================================
    #                           System Logs
    # ====================================================================
    elif choice.lower() == "s":
        if os.path.exists("System_logs.txt"):
            with open("System_logs.txt", "r") as log_file:
                print(log_file.read())

        else:
            print("No Logs Generated yet!")

        print("-------------------------------------------------------")

    # ====================================================================
    #                           Exit Syatem
    # ====================================================================
    elif choice == "6" or choice.lower() == "exit":
        print("===========================================================")
        print("Thank you For Using Adlytix system")
        time.sleep(1)
        print("System is Shutting down!")
        time.sleep(0.5)
        print("Allah Hafiz 😘")
        break

    else:
        print("===========================================================")
        print("       Invalid choice! Please select from 1 to 5.")
        print("===========================================================")
