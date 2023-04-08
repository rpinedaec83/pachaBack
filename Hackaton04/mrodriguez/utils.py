import os
import os.path
import time


class Menu:
    def __init__(self, menuName, optionsList):
        self.menuName = menuName
        self.optionsList = optionsList

    def showMenu(self):
        a = True
        while a:
            self.clearMenu()

            print(
                Color.PURPLE
                + "--- "
                + "MENÚ "
                + self.menuName.upper()
                + " ---"
                + Color.END
            )
            print("")
            print("OPCIONES")
            print("")
            for key, value in self.optionsList.items():
                print(key + Color.GREEN + " → " + Color.END + value)
            print("")

            resp = input(Color.YELLOW + "Por favor ingresa una opción: " + Color.END)
            print("")

            if resp == "0":
                print(Color.YELLOW + "Saliendo... Hasta pronto.")
                time.sleep(2)
                break

            b = 0
            for key, value in self.optionsList.items():
                if value == resp:
                    b += 1
            if b > 0:
                a = False
            else:
                print(Color.RED + "❌ Ingresa una opción válida" + Color.END)
                time.sleep(2)

        return resp

    def clearMenu(self):
        def clear():
            return os.system("clear")

        clear()


class FileManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def readFile(self):
        try:
            file = open(self.fileName, "r")
            return file.read()
        except Exception as e:
            return e

    def writeFile(self, line):
        try:
            currentDirectory = os.getcwd()
            path = currentDirectory + "\\" + self.fileName  # print(path)
            if os.path.isfile(path):
                try:
                    file = open(self.fileName, "a")
                    file.write(line + "\n")
                except Exception as e:
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.fileName, "w")
                file.close()

                file = open(self.fileName, "a")
                file.write(line + "\n")
        except Exception as e:
            print(e)

    def removeFile(self):
        currentDirectory = os.getcwd()
        path = currentDirectory + "\\" + self.fileName

        if os.path.isfile(path):
            try:
                os.remove(path)
                # print("Removiendo archivo")
            except Exception as e:
                print(e)


class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
