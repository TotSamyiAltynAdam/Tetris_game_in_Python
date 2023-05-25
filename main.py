from menu import Menu
from app import App
from settings import*

if __name__ == '__main__':
    while(True):
        file_path = MAXIMUM_SCORE_PATH
        with open(file_path, "r") as file:
            stored_number = int(file.readline().strip())
        m = Menu()
        app = App()
        m.run(stored_number)
        app.run()
