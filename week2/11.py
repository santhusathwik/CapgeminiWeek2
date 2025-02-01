class Logger:
    def log(self,*m):
        for message in m:
            if message=="error":
                print("Error Message")
            elif message=="warning":
                print("Warning Message")
            elif message=="info":
                print("Info Message")
l=Logger()
l.log("error")
print("------------------")
l.log("error","warning","info")
print("------------------")
l.log("info")