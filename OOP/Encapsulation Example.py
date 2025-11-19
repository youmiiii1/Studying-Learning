class WashM:
    def __init__(self,speed, duration, temperature):
        self.__speed = speed
        self.__duration = duration
        self.__temperature = temperature

    def slow_mode(self):
        self.__speed = 400
        self.__duration = 28
        self.__temperature = 20
        return f"Speed: {self.__speed} | Duration: {self.__duration} | Temperature: {self.__temperature}"

    def medium_mode(self):
        self.__speed = 650
        self.__duration = 45
        self.__temperature = 40
        return f"Speed: {self.__speed} | Duration: {self.__duration} | Temperature: {self.__temperature}"

    def fast_mode(self):
        self.__speed = 700
        self.__duration = 55
        self.__temperature = 100
        return f"Speed: {self.__speed} | Duration: {self.__duration} | Temperature: {self.__temperature}"

m_1 = WashM(0,0,0)

def main_menu():
    while True:
        user_choice = int(input("Please choose Mode: "))

        if user_choice == 1:
            print(m_1.slow_mode())

        elif user_choice == 2:
            print(m_1.medium_mode())

        elif user_choice == 3:
            print(m_1.fast_mode())

        elif user_choice == 0:
            break

        else:
            break
main_menu()






