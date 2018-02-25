
class Assignment():
    def __init__(self, name=None, due=None, subject=None, done="False"):
        self.__done = done
        self.__due = due
        self.__subject = subject
        self.__name = name

    # Returns current assignments details as string
    def __str__(self):
        if "true" in self.__done:
            done = "Completed!"
        else:
            done = "Unfinished"
        if self.__due == "":
            due = "Indefinite"
        else:
            due = self.__due
        output = []
        output.append("   " + '{:>12}'.format("Assignment: ") + "%s" % self.__name)
        output.append("   " + '{:>12}'.format("Due: ") + "%s" % due)
        output.append("   " + '{:>12}'.format("Subject: ") + "%s" % self.__subject)
        output.append("   " + '{:>12}'.format("Completed: ") + "%s" % done)
        output_str = ("%s\n%s\n%s\n%s\n" % (output[0], output[1], output[2],
                                            output[3]))
        return output_str

    # Returns assignment info in dictionary form
    def info(self):
        output = {"name": self.__name, "due": self.__due,
                    "subject": self.__subject, "done": self.__done}
        return output

    # Marks an assignment as completed
    def complete(self):
        self.__done = "true"
