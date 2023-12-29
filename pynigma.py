class EnigmaMachine():
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, letter):
        encryptValue = letter
        isNextRotorRotate = True

        for rotor in self.rotors:
            if (isNextRotorRotate == True):
                rotor.rotate()
            isNextRotorRotate = rotor.isNextRotorRotate()
            encryptValue = rotor.encrypt(encryptValue)

        encryptValue = self.reflector.encrypt(encryptValue)

        reversedOrderRotors = self.rotors.reverse()

        for rotor in reversedOrderRotors:
            if (isNextRotorRotate == True):
                rotor.rotate()
            isNextRotorRotate = rotor.isNextRotorRotate()
            encryptValue = rotor.encrypt(encryptValue)

        return encryptValue
    
    def addRotors(self, rotors):
        self.rotors = rotors

    def addReflector(self, reflector):
        self.reflector = reflector

class Reflector():
    def __init__(self, name, wiring):
        self.name = name
        self.wiring = wiring
    
    def encrypt(self, letter):
        position = ord(letter) - 97
        encryptedLetter = self.wiring[position]
        return encryptedLetter


class Rotor():

    def __init__(self, name, wiring, rotatePosition = 0, currentPosition = 0):
        self.name = name

        assert len(wiring) == 26, "Wiring mapping has invalid length."
        assert wiring.isalpha(), "Wiring mapping in not alpha."
        self.wiring = wiring
        self.rotatePosition = rotatePosition
        self.currentPosition = currentPosition

    def rotate(self):
        nextPosition = self.currentPosition + 1
        if(nextPosition == len(self.wiring) ):
            self.currentPosition = 0
        else:
            self.currentPosition = nextPosition

    #Called after rotate()
    def isNextRotorRotate(self):
        if(self.rotatePosition == (self.currentPosition - 1) ):
            return True
        elif(self.rotatePosition == 25 and self.currentPosition == 0):
            return True
        else:
            return False


    def encrypt(self, letter):
        position = ord(letter) - 97 + self.currentPosition
        encryptedLetter = self.wiring[position]
        return encryptedLetter