#THIS PROJECT IS ROBOSPEAKER
import os

if __name__ == '__main__':
    print("welcome to the robospeaker 2.1, Created by Muneeb Haider")
    while True:
        x=input("what you want to speak me :  ")
        if(x == "q"):
            print("----ROBOSPEAKER IS OVER----")
            break
        command = f"say {x}"
        os.system(command)

