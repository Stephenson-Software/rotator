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
        numItems = len(inputList)

        # every numItems rotations restore the list, so whole cycles are skipped
        if (numItems > 0 and numRotations >= numItems):
            numRotations = numRotations % numItems

        for i in range(numRotations):
            self.rotate(inputList)