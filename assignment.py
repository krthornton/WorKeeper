
class Assignment():
    def __init__(self, name=None, due=None, subject=None, done="False"):
        self.__done = done
        self.__due = due
        self.__subject = subject
        self.__name = name

    # Returns current assignments details as string
    def __str__(self):
        if "True" in self.__done:
            done = "Completed!"
        else:
            done = "Unfinished"
        if self.__due == "":
            due = "Indefinite"
        else:
            due = self.__due
        output = ("Assignment: %s\nDue: %s\nSubject: %s\nCompleted: %s\n"
                    % (self.__name, due, self.__subject, done))
        return output

    def info(self):
        output = {"name": self.__name, "due": self.__due,
                    "subject": self.__subject, "done": self.__done}
        return output

    # Marks an assignment as completed
    def complete(self):
        self.__done = "True"

    # Saves current assignment details to assignments.txt
    #def save(self, save_file):
    #    save_file.write("%s$%s$%s$%s\n" % (self.__name, self.__due,
    #                    self.__subject, self.__done))
