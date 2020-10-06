class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VSCode:
    def execute(self):
        print("Spelling check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()


ide=Pycharm()

ide=VSCode()

lap1=Laptop()
lap1.code(ide)