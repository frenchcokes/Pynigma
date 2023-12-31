class EnigmaMachine():
    def __init__(self, rotors, reflector, isShowSteps):
        self.rotors = rotors
        self.reflector = reflector
        self.isShowSteps = isShowSteps
    
    def checkRotate(self):
        rotateNext = True

        for rotor in self.rotors:
            if(rotateNext == True):
                rotateNext = rotor.isNextRotorRotate()
                rotor.rotate()
            else:
                break
    
    def getRotorValues(self):
        rotorValues = []
        for rotor in self.rotors:
            rotorValues.append(rotor.getCurrentPostion())
        rotorValues.reverse()
        return rotorValues

    def encrypt(self, letter):
        self.checkRotate()

        encryptValue = letter

        if(self.isShowSteps == True):
            print("State: " + str(self.getRotorValues()))
            print("Input: " + letter)
        for rotor in self.rotors:
            encryptValue = rotor.encrypt(encryptValue)
            if(self.isShowSteps == True):
                print(rotor.name + " encryption: " + encryptValue)
        
        encryptValue = self.reflector.encrypt(encryptValue)
        if(self.isShowSteps == True):
                print(self.reflector.name + " encryption: " + encryptValue)

        rotorsCopy = self.rotors.copy()
        rotorsCopy.reverse()
        reversedOrderRotors = rotorsCopy

        for rotor in reversedOrderRotors:
            encryptValue = rotor.encryptReverse(encryptValue)
            if(self.isShowSteps == True):
                print(rotor.name + " encryption: " + encryptValue)

        return encryptValue
    
    def setRotorCurrentPositions(self, currentPositions):
        assert len(currentPositions) == len(self.rotors), "Number of positions not equal to number of rotors."
        for x in range(len(self.rotors)):
            self.rotors[x].setCurrentPosition(currentPositions[x])

    def setRotorRotatePositions(self, rotatePositions):
        assert len(rotatePositions) == len(self.rotors), "Number of positions not equal to number of rotors."
        for x in range(len(self.rotors)):
            self.rotors[x].setRotatePosition(rotatePositions[x])

    def addRotors(self, rotors):
        self.rotors = rotors

    def addReflector(self, reflector):
        self.reflector = reflector

    def setIsShowSteps(self, bool):
        self.isShowSteps(bool)

class Reflector():
    def __init__(self, name, wiring):
        self.name = name
        self.wiring = wiring
    
    def encrypt(self, letter):
        position = ord(letter) - 65
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
        if(nextPosition > 25 ):
            self.currentPosition = 0
        else:
            self.currentPosition = nextPosition

    def isNextRotorRotate(self):
        if (self.currentPosition == self.rotatePosition):
            return True
        else:
            return False

    #Right to left
    def encrypt(self, letter):
        inputPosition = self.currentPosition #0-25
        letterPosition = ord(letter) - 65 #0-25
        convertedPosition = letterPosition + inputPosition

        if(convertedPosition > 25):
            convertedPosition = convertedPosition - 26
        elif(convertedPosition < 0):
            convertedPosition = convertedPosition + 26

        encryptedLetter = self.wiring[convertedPosition]
        return encryptedLetter

    #Left to Right
    def encryptReverse(self, letter):
        inputPosition = self.currentPosition

        convertedPosition = self.wiring.find(letter) - inputPosition

        if(convertedPosition > 25):
            convertedPosition = convertedPosition - 26
        elif(convertedPosition < 0):
            convertedPosition = convertedPosition + 26

        encryptedLetter = chr(convertedPosition + 65)
        return encryptedLetter
    
    def setCurrentPosition(self, newCurrentPosition):
        self.currentPosition = newCurrentPosition

    def setRotatePosition(self, newRotatePosition):
        self.rotatePosition = newRotatePosition

    def getCurrentPostion(self):
        return self.currentPosition