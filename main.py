"""
To Do:
3. Add ability to delete assignment
4. Add ability to edit assignment
"""

from assignment import *
import os
import json



def main():
    # Print welcome screen
    welcome()

    # Load the save file and load previously saved assignments
    save_file = open("assignments.json", "r+")
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
            name = ""
            while name == "":
                name = input("Please enter an assignment name: ")
                if name == "":
                    print("Error: name can't be empty")
                for i in assignment_dic:
                    if i.info()["name"] == name:
                        print("Error: assignment with name already exists")
                        name = ""
            due = input("Enter a due date: ")
            subject = input("Enter the subject: ")
            print()
            x = make_assignment(assignment_dic, name, due, subject, "false")

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
    write_file = open("assignments.json", "w")
    welcome()
    print("Saving...")
    save_assignments(assignment_dic, write_file)
    write_file.close()
    print("Done")
    exit()



# Used to return Assignment objects as dictionaries for json to save
def jsonDefault(o):
    return o.__dict__

# Returns list of dictionaries from given file object
def load_assignments(assignment_dic, save_file):
    try:
        data = json.load(save_file)
        for i in data:
            assignment_dic.append(Assignment(i["_Assignment__name"],
                                             i["_Assignment__due"],
                                             i["_Assignment__subject"],
                                             i["_Assignment__done"]))
    except:
        print("Generating new save file...\nIf this is not your first time",
              "opening WorKeeper,\nyour save file may be corrupted.\n")
    return

def save_assignments(assignments_dic, save_file):
    json.dump(assignments_dic, save_file, default = jsonDefault, indent = 4)
    return

def welcome():
    os.system("cls")
    print("||| WorKeeper |||\n")
    print()

def list_assignments(assignment_dic):
    print("Unfinished Assignments:\n")
    for i in assignment_dic:
        if "false" in i.info()["done"]:
            print(i)
    print("\nCompleted Assignments:\n")
    for i in assignment_dic:
        if "true" in i.info()["done"]:
            print(i)
    print()

def make_assignment(assignment_dic, name=None, due=None, subject=None,
                    done=None):
    assignment_dic.append(Assignment(name, due, subject, done))
    return True



main()
