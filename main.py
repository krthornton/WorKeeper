"""
To Do:
1. Convert "true" and "false" to actual booleans. Convert save to json
3. Add ability to delete assignment
4. Add ability to edit assignment
"""

from assignment import *
import os


def main():

    # Print welcome screen
    welcome()

    # Load the save file and load previously saved assignments
    save_file = open("assignments.txt", "r")
    assignment_dic = []
    load_assignments(assignment_dic, save_file)
    save_file.close() # Close file after reading

    # Main menu
    while True:
        answer = input("Enter [1] to list assignments\n" +
                        "Enter [2] to enter a new assignment\n" +
                        "Enter [3] to mark an assignment as completed\n" +
                        "Enter [4] to save and exit: ")
        print()
        if answer == "1":
            # Print welcome screen
            welcome()
            if len(assignment_dic) > 0:
                list_assignments(assignment_dic)
            else:
                print("Looks like there's nothing here yet...\n")
        if answer == "2":
            # Print welcome screen
            welcome()
            name = input("Enter an assignment name: ")
            due = input("Enter a due date: ")
            subject = input("Enter the subject: ")
            print()
            x = make_assignment(assignment_dic, name, due, subject, "False")

            # Print welcome screen
            os.system("cls")
            print("||| WorKeeper |||\n")
            if x == True:
                print("Assignment created!\n")
        if answer == "3":
            index = 1
            welcome()
            for i in assignment_dic:
                print("%i. %s" % (index, i.info()["name"]))
                index += 1
            response = input("Which assignment do you wish to mark as" +
                            " completed? (Please match case): ")
            for i in assignment_dic:
                if response == i.info()["name"]:
                    i.complete()
                    # Print welcome screen
                    welcome()
                    print("Assignment %s marked as completed!\n" %
                            (i.info()["name"]))
                else:
                    welcome()

        if answer == "4":
            break

    # Open file for writing and save assignments
    write_file = open("assignments.txt", "w")
    welcome()
    print("Saving...")
    save_assignments(assignment_dic, write_file)
    write_file.close()
    print("Done")
    exit()



def load_assignments(assignment_dic, save_file):
    for line in save_file:
        line = line.split("$")
        if len(line) == 4:
            assignment_dic.append(Assignment(line[0], line[1],
                                             line[2], line[3]))



def save_assignments(assignments_dic, save_file):
    for i in assignments_dic:
        i = i.info()
        x = ("%s$%s$%s$%s" % (i["name"], i["due"], i["subject"], i["done"]))
        save_file.write("%s\n" % x)
    return



def welcome():
    os.system("cls")
    print("||| WorKeeper |||\n")
    print()



def list_assignments(assignment_dic):
    print("Unfinished Assignments:\n")
    for i in assignment_dic:
        if "False" in i.info()["done"]:
            print(i)
    print("\nCompleted Assignments:\n")
    for i in assignment_dic:
        if "True" in i.info()["done"]:
            print(i)
    print()


def make_assignment(assignment_dic, name=None, due=None, subject=None,
                    done=None):
    # Returns True if assignment is successfully created
    if ("$" in name) or ("$" in due) or ("$" in subject):
        problem("invalid character '$'")
        return False
    else:
        assignment_dic.append(Assignment(name, due, subject, done))
        return True



def problem(message):
    # message must be a string
    os.system("cls")
    print("||| WorKeeper |||\n")
    input("Error: %s" % message)



main()
