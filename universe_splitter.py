import random
import time

def getInput():
    inputs = []
    input_a = input("First option : ")
    input_b = input("Second option: ")
    inputs.append(input_a)
    inputs.append(input_b)
    return inputs

def chooseResult(inputs):
    random_index = random.randint(0,1)
    choice = inputs[random_index]
    return choice

def universeSplitterAnimation():
    print()
    print("Input:         ", end = "")
    time.sleep(1)
    print("Valid")
    print("Internet:      ", end = "")
    time.sleep(1)
    print("Connected")
    print("Geneva:        ", end = "")
    time.sleep(1)
    print("Online")
    print("Device:        ", end = "")
    time.sleep(1)
    print("Ready")
    print("Photon:        ", end = "")
    time.sleep(1)
    print("Emitted")
    print()
    print("-"*20)
    print()
    time.sleep(1)    

def printDecision(decision):
    len_decision = len(decision)
    print("Decision: ")
    print("!"*(len_decision+10))
    print("!" + " "*(len_decision+8) + "!")
    print(f"!    {decision}    !")
    print("!" + " "*(len_decision+8) + "!")
    print("!"*(len_decision+10))
    print()    

def doIt():
    time.sleep(4)
    print("... now go do it!")

def main():
    inputs = getInput()
    
    universeSplitterAnimation()
    
    decision = chooseResult(inputs)
    
    printDecision(decision)
    
    doIt()


if (__name__ == "__main__"):
    main()
