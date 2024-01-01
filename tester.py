import pynigma

if __name__ == "__main__":
    rotorI = pynigma.Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0, 0)
    rotorII = pynigma.Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0, 0)
    rotorIII = pynigma.Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0, 0)
    rotorIV = pynigma.Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", 0, 0)
    rotorV = pynigma.Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", 0, 0)

    reflectorB = pynigma.Reflector("UKW-B","YRUHQSLDPXNGOKMIEBFZCWVJAT")

    enigmaMachine = pynigma.EnigmaMachine([rotorIII, rotorI, rotorII], reflectorB, False)

    enigmaMachine.addPlug("A", "C")
    enigmaMachine.addPlug("B", "D")
    enigmaMachine.addPlug("E", "F")
    enigmaMachine.addPlug("Z", "G")

    enigmaMachine.setRotorCurrentPositions(["A","Z","C"])
    enigmaMachine.setRotorRotatePositions(["F","B","D"])

    print(enigmaMachine.encrypt("PETER PIPER PICKED A PECK OF PICKLED PEPPERS A PECK OF PICKLED PEPPERS PETER PIPER PICKED IF PETER PIPER PICKED A PECK OF PICKLED PEPPERS WHERES THE PECK OF PICKLED PEPPERS PETER PIPER PICKED"))

    enigmaMachine.setRotorCurrentPositions(["A","Z","C"])
    enigmaMachine.setRotorRotatePositions(["F","B","D"])

    print(enigmaMachine.encrypt("OYKCI RDNTA VXEIUV M NBPM UP UZZQQMB FHKXSFJ P TLVI ZG OMJZKWG KDUNIMB IVGMX NSGWB VGOUWW YK EVKRI BYDID IMXZJY J MDFD RO METCIJS TVYTKNP VBCXIE HKR UDFJ SA TNXPPTC FXOFIXC VRNUL IDXMA HEPVAF"))
