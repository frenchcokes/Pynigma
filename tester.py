import pynigma

if __name__ == "__main__":
    rotorI = pynigma.Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0, 0)
    rotorII = pynigma.Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0, 0)
    rotorIII = pynigma.Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0, 0)

    #rotorI = pynigma.Rotor("I", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, 0)
    #rotorII = pynigma.Rotor("II", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, 0)
    #rotorIII = pynigma.Rotor("III", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, 0)
    rotorIV = pynigma.Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", 0, 0)
    rotorV = pynigma.Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", 0, 0)

    reflectorB = pynigma.Reflector("UKW-B","YRUHQSLDPXNGOKMIEBFZCWVJAT")

    enigmaMachine = pynigma.EnigmaMachine([rotorI, rotorII, rotorIII], reflectorB, False)

    enigmaMachine.addPlug("A", "C")
    enigmaMachine.addPlug("T", "B")

    enigmaMachine.setRotorCurrentPositions([0,0,0])
    enigmaMachine.setRotorRotatePositions([0,0,0])

    print(enigmaMachine.encrypt("HEHEXD LOL"))

    enigmaMachine.setRotorCurrentPositions([0,0,0])
    enigmaMachine.setRotorRotatePositions([0,0,0])

    print(enigmaMachine.encrypt("MQZJFG ZMN"))

    #print(rotorIII.encryptReverse(reflectorB.encrypt(rotorIII.encrypt("A"))))
    #print(rotorIII.encryptReverse(reflectorB.encrypt(rotorIII.encrypt("V"))))
