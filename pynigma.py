#The enigma machine was a german encryption machine used during WW2.
#One of it's main weaknesses was that a letter could never be encrypted
#as itself.
class EnigmaMachine():
    def __init__(self, rotors, reflector, isShowSteps):
        #The order of rotors is important!
        #Order starts reversed because goes right to left first.
        rotors.reverse()
        self.rotors = rotors
        self.reflector = reflector
        self.isShowSteps = isShowSteps
        self.plugs = []

    #Each click of a key causes the right-most rotor to rotate one position.
    #The rotors to the left can only rotate if the preceding rotor is in
    #a certain position. These positions are called "ring position" and are a setting.
    def checkRotate(self):
        rotateNext = True
        for rotor in self.rotors:
            if(rotateNext == True):
                rotateNext = rotor.isNextRotorRotate()
                rotor.rotate()
            else:
                break
    
    #Adds a plug to the imaginary plugboard
    def addPlug(self, letter1, letter2):
        plugs = self.plugs
        isDuplicate = False
        for x in plugs:
            if((x.hasLetter(letter1) == True) or (x.hasLetter(letter2) == True)):
               isDuplicate = True
               break
        assert isDuplicate == False, "Duplicate plug detected!"
        if(isDuplicate == False):
            plug = Plug([letter1, letter2])
            plugs.append(plug)
    
    #Checks if theres a plug connection. If there's not, returns
    #unchanged value.
    def checkPlugs(self, letter):
        for plug in self.plugs:
            if(plug.hasLetter(letter)):
                return plug.getOtherLetter(letter)
        return letter
    
    #Removes the plug which contains a letter
    def removePlug(self, letter):
        plugs = self.plugs
        for x in plugs:
            if(x.hasLetter(letter) == True):
                plugs.remove(x)

    #Displays plug connections
    def plugsDisplay(self):
        output = ""
        for plug in self.plugs:
            output = output + str(plug.getConnection()) + " "
        return output

    #Encrypts a phrase
    def encrypt(self, phrase):
        encryptedMessage = ""
        words = phrase.split()
        for word in words:
            encryptedWord = ""
            for x in range(len(word)):
                encryptedWord = encryptedWord + self.encryptLetter(word[x])
            encryptedMessage = encryptedMessage + encryptedWord + " "
        return encryptedMessage


    #Enigma uses a "substitution cipher", where essentially a letter gets
    #swapped out for another. Each time a key is pressed, it is encryped once
    #through each rotor, then once through the reflector, then again once more
    #through each rotor on the way back. Given 3 rotors, that's 7 encryptions!
    #(Not including plugs)
    def encryptLetter(self, letter):
        self.checkRotate()

        encryptValue = letter

        encryptValue = self.checkPlugs(encryptValue)

        if(self.isShowSteps == True):
            print("State: " + str(self.getRotorPositions()))
            print("Input: " + letter)
        
        encryptValue = self.rotorForwardEncrypt(encryptValue)
        
        encryptValue = self.reflectorEncrypt(encryptValue)

        encryptValue = self.rotorReverseEncrypt(encryptValue)

        if(self.isShowSteps == True):
            print("Result: " + encryptValue)

        encryptValue = self.checkPlugs(encryptValue)

        return encryptValue
    
    def rotorForwardEncrypt(self, letter):
        encryptValue = letter
        for rotor in self.rotors:
            encryptValue = rotor.encrypt(encryptValue)
            if(self.isShowSteps == True):
                print(rotor.name + " encryption: " + encryptValue)
        return encryptValue
    
    def rotorReverseEncrypt(self, letter):
        rotorsCopy = self.rotors.copy()
        rotorsCopy.reverse()

        encryptValue = letter
        for rotor in rotorsCopy:
            encryptValue = rotor.encryptReverse(encryptValue)
            if(self.isShowSteps == True):
                print(rotor.name + " encryption: " + encryptValue)
        return encryptValue

    def reflectorEncrypt(self, letter):
        encryptValue = letter
        encryptValue = self.reflector.encrypt(encryptValue)
        if(self.isShowSteps == True):
                print(self.reflector.name + " encryption: " + encryptValue)
        return encryptValue

    #This is one of the settings. Current positions acts as an "offset" for
    #each wheel. For instance, if it was rotated one position, hitting the 
    #"A" key would give the output for the "B" key instead from the rotor.
    def setRotorCurrentPositions(self, currentPositions):
        assert len(currentPositions) == len(self.rotors), "Number of positions not equal to number of rotors."
        for x in range(len(self.rotors)):
            self.rotors[x].setCurrentPosition(currentPositions[x])

    #This is another setting called the "Ring Setting". Ring setting determines when
    #the following rotor can rotate. There was one of these for each rotor.
    def setRotorRotatePositions(self, rotatePositions):
        assert len(rotatePositions) == len(self.rotors), "Number of positions not equal to number of rotors."
        for x in range(len(self.rotors)):
            self.rotors[x].setRotatePosition(rotatePositions[x])

    def getRotorPositions(self):
        rotorPositions = []
        for rotor in self.rotors:
            rotorPositions.append(rotor.getCurrentPostion())
        rotorPositions.reverse()
        return rotorPositions

    def addRotors(self, rotors):
        self.rotors = rotors

    def addReflector(self, reflector):
        self.reflector = reflector

    def setIsShowSteps(self, bool):
        self.isShowSteps(bool)

#Reflectors swap one letter for another based on the wiring.
class Reflector():
    def __init__(self, name, wiring):
        self.name = name
        self.wiring = wiring
    
    def encrypt(self, letter):
        position = ord(letter) - 65
        encryptedLetter = self.wiring[position]
        return encryptedLetter

#Each rotor has 26 positions, one for each letter. Each letter is wired to
#a different letter.
class Rotor():
    def __init__(self, name, wiring, rotatePosition = 0, currentPosition = 0):
        self.name = name
        assert len(wiring) == 26, "Wiring mapping has invalid length."
        assert wiring.isalpha(), "Wiring mapping in not alpha."
        self.wiring = wiring

        self.setRotatePosition(rotatePosition)
        self.setCurrentPosition(currentPosition)

    def rotate(self):
        nextPosition = self.currentPosition + 1
        if(nextPosition > 25 ):
            self.currentPosition = 0
        else:
            self.currentPosition = nextPosition

    #The next rotor can only rotate if the preceding rotor is in the
    #correct position.
    def isNextRotorRotate(self):
        if (self.currentPosition == self.rotatePosition):
            return True
        else:
            return False

    #Right to left. Converts the position to the letter linked to
    #the wiring.
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

    #Left to Right. Converts the wiring to the wiring linked to the
    #letter.
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
        if (type(newCurrentPosition) == str):
            self.currentPosition = ord(newCurrentPosition) - 65
        else:
            self.currentPosition = newCurrentPosition

    def setRotatePosition(self, newRotatePosition):
        if (type(newRotatePosition) == str):
            self.rotatePosition = ord(newRotatePosition) - 65
        else:
            self.rotatePosition = newRotatePosition

    def getCurrentPostion(self):
        return self.currentPosition

#Plugs are connected to the plugboard. They swap one letter for another
#based on the plug settings. 
class Plug():
    def __init__(self, connection):
        assert len(connection) == 2
        self.connection = connection
    def getOtherLetter(self, letter):
        if self.hasLetter(letter):
            for x in self.connection:
                if(x != letter):
                    return x
        else:
            return None
    def hasLetter(self, letter):
        if letter in self.connection:
            return True
        else:
            return False
    def getConnection(self):
        return self.connection