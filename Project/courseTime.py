class CourseTime:
    def __init__(self, arg):  # are: String
        # The __init__ method takes a single argument, expected to be a string.
        # It should either be "online" or a whitespace delimited triple of "<start time> <end time> <days>"
        # where start and end time should be hours and minutes in 24 hour (military) format,
        # while days is one or more of MTWRFS. Sunday is not allowed, R stands for Thursday.
        # If the argument is not valid an exception is thrown.
        pass

    def __str__(self):
        # returns "<start time> <end time> <days>", or "online" for online courses.
        return ""

    # return the start times as datetime.time objects
    def start(self):
        return -1  # datetime.time

    # return the end times as datetime.time objects
    def end(self):
        return -1  # datetime.time

    # The isOnline method returns True if it is online.
    def isOnline(self):
        return None

    # The isOverlap method takes a second CourseTime as its argument.
    # It returns True of the day and time of the two courses overlap
    def isOverlap(self):
        return None

