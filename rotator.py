# @author Daniel McCoy Stephenson
# @since 8/24/2023
class Rotator:
    def rotate(self, inputList):
        numItems = len(inputList)

        firstItem = inputList[0]
        for i in range(numItems):
            nextIndex = i+1
            if (nextIndex == numItems):
                continue
            inputList[i] = inputList[nextIndex]

        inputList[numItems - 1] = firstItem
    
    def rotateRepeat(self, inputList, numRotations):
        for i in range(numRotations):
            self.rotate(inputList)