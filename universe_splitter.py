import random
import time

def get_inputs():
    inputs = []
    input_a = input("In one universe, I will now: ")
    input_b = input("In the other universe, I will now: ")
    inputs.append(input_a)
    inputs.append(input_b)
    return inputs

def get_idx():
    return random.randint(0,1)

def animation():
    time_delay = 0.8
    line_length = 20
    print("\n" + "-"*line_length + "\n")
    print("Input:         ", end = "")
    time.sleep(time_delay)
    print("Valid")
    print("Internet:      ", end = "")
    time.sleep(time_delay)
    print("Connected")
    print("Geneva:        ", end = "")
    time.sleep(time_delay)
    print("Online")
    print("Device:        ", end = "")
    time.sleep(time_delay)
    print("Ready")
    print("Photon:        ", end = "")
    time.sleep(time_delay)
    print("Emitted")
    print("\n" + "-"*line_length + "\n") 

def universe(idx):
    if (idx == 0):
        a_or_b = "A"
    else:
        a_or_b = "B"
    universe = "You are in universe " + a_or_b
    len_decision = len(universe)

    print("YOUR UNIVERSE HAS JUST SPLIT!" + "\n")
    time.sleep(0.75)
    print("*"*(len_decision+10))
    print("*" + " "*(len_decision+8) + "*")
    print(f"*    {universe}    *")
    print("*" + " "*(len_decision+8) + "*")
    print("*"*(len_decision+10) + "\n")

def result(inputs, idx):
    if (idx == 0):
        not_idx = 1
    else:
        not_idx = 0
    time.sleep(0.75)
    print("You are in the universe in which you should " + inputs[idx] + ".")
    print("(And right now, in the other universe, the other you is being told to " + inputs[not_idx] + ".)\n")


def main():
    inputs = get_inputs()
    animation()
    idx = get_idx()
    universe(idx)
    result(inputs, idx)


if (__name__ == "__main__"):
    main()
