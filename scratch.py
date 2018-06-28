from datetime import datetime
import json
import os
from uuid import uuid4

class Main:
    def __init__(self):
        self.assignments = {}

        self.welcome()
        self.main_menu()

    def main_menu(self):
        """
        Shows the main menu screen and presents the user with options
        :return:
        """

        answer = input("Enter [1] to list assignments\n" +
                       "Enter [2] to enter a new assignment\n" +
                       "Enter [3] to mark an assignment as completed\n" +
                       "Enter [4] to save and exit\n" +
                       "Enter [5] to delete an assignment: ")
        print()
        if answer == "1":
            # Print welcome screen
            self.welcome()
            if len(self.assignments) > 0:
                self.list_assignments()
            else:
                print("Looks like there's nothing here yet...\n")
        if answer == "2":
            # Print welcome screen
            self.welcome()
            name = ""
            while name == "":
                name = input("Please enter an assignment name: ")
                if name == "":
                    print("Error: name can't be empty")
                for i in self.assignments:
                    if i.info()["name"] == name:
                        print("Error: assignment with name already exists")
                        name = ""
            due = input("Enter a due date: ")
            subject = input("Enter the subject: ")
            print()
            self.make_assignment(name, due, subject)

            # Print welcome screen
            os.system("cls")
            print("||| WorKeeper |||\n")
            #if x == True:
            #    print("Assignment created!\n")
        if answer == "3":
            index = 1
            self.welcome()
            for i in self.assignments:
                print("%i. %s" % (index, i.info()["name"]))
                index += 1
            response = input("Which assignment do you wish to mark as" +
                             " completed? (Please match case): ")
            for i in self.assignments:
                if response == i.info()["name"]:
                    i.complete()
                    # Print welcome screen
                    self.welcome()
                    print("Assignment %s marked as completed!\n" %
                          (i.info()["name"]))
                else:
                    self.welcome()

        if answer == "4":
            pass

        if answer == "5":
            index = 1
            self.welcome()
            if self.assignments is []:
                self.welcome()
                print("Can't delete when list is empty\n")
                pass
            for i in self.assignments:
                print("%i. %s" % (index, i.info()["name"]))
                index += 1
            response = input("Which assignment do you wish to mark delete?" +
                             "(Please match case): ")
            for i in self.assignments:
                if response == i.info()["name"]:
                    self.assignments.remove(i)
                    self.welcome()
                    print("Assignment %s removed\n" % (i.info()["name"]))

    @staticmethod
    def welcome():
        os.system("cls")
        print("||| WorKeeper |||\n")
        print()

    def list_assignments(self):
        print("Unfinished Assignments:\n")
        for key, value in self.assignments.itmes():
            print(key, value[''])
        print("\nCompleted Assignments:\n")
        for i in self.assignments:
            if "true" in i.info()["done"]:
                print(i)
        print()

    def make_assignment(self, name, due, subject):
        # generate a random uid to associate with each assignment
        self.assignments[uuid4()] = {'name': str(name),
                                     'due': str(due),
                                     'subject': str(subject),
                                     'done': False}
        print(self.assignments) # debug
        self.list_assignments() # debug

def main():
    Main()

if __name__ == "__main__":
    main()