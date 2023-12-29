import pynigma

if __name__ == "__main__":
    testRotor = pynigma.Rotor("Basic", "bcdefghijklmnopqrstuvwxyza")
    
    print(testRotor.encrypt("a"))
    testRotor.rotate()
    print(testRotor.encrypt("a"))