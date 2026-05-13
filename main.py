from app.Controller import Controller
from app.Relogio import Relogio

def main():
    Relogio().resetar()
    Controller.main()

if __name__ == '__main__':
    main()