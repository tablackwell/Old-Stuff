# Thomas Blackwell - ID tablackw
# tablackwell@email.wm.edu
# Professor hong
# CS 241 Section 2
# Lab 4 - gradeprog.py

## To Do List ##
## Make format pretty
## Test for weird cases
## Resolve issue of blank lines
## ???
## profit.


class StudentRecord:
    ''' A storage class for the student information.'''
    
    def __init__(self, studentID, studentGrade ):
        '''initializes a student storage object.'''
        self._studentID = studentID
        self._studentGrade = int(studentGrade)
        
    def __str__(self):
        '''Proper string output for student objects. Easier for debugging.'''
        return (self._studentID + '  ' + str(self._studentGrade))

def recordReader():
    '''This function reads through and returns the unsorted record sequence.'''
    
    studentList = []
    recordFile = open('rawgrade.txt', 'r')
    for line in recordFile:
        line = line.split()
        studentObject = StudentRecord(line[0],line[1])
        studentList.append(studentObject)
        print(studentObject)
    return studentList

def alphaSorter(studentList):
    ''' Sorts the student info and grades by alphabetical order of ID/names.
    This is a selection sorter
    '''
    
    studentListAlpha = studentList
    
    n = len(studentListAlpha)
    for i in range( n - 1):
        smallNdx = i
        for j in range( i + 1, n):
            if studentListAlpha[j]._studentID < studentListAlpha[smallNdx]._studentID:
                smallNdx = j
        if smallNdx != i:
            tmp = studentListAlpha[i]
            studentListAlpha[i] = studentListAlpha[smallNdx]
            studentListAlpha[smallNdx] = tmp
            
    return studentListAlpha

def gradeSorter(studentList):
    '''Sorts the student info according to the grades of the students. This is
    a selection sorter
    '''
    
    studentListGrades = studentList
    
    n = len(studentListGrades)
    for i in range( n - 1):
        smallNdx = i
        for j in range( i + 1, n):
            if studentListGrades[j]._studentGrade > studentListGrades[smallNdx]._studentGrade:
                smallNdx = j
        if smallNdx != i:
            tmp = studentListGrades[i]
            studentListGrades[i] = studentListGrades[smallNdx]
            studentListGrades[smallNdx] = tmp
            
    return studentListGrades


def recordWriter(sortedByGrades, sortedByID):
    '''Writes the sorted student info to a text file named procgrade.txt.'''
    
    outputFile = open('procgrade.txt', 'w')
    outputFile.write('Student Records in Alphabetical Order\n\n')
    for item in sortedByID:
        outputFile.write(item._studentID)
        outputFile.write('  ')
        outputFile.write(str(item._studentGrade) + '\n')
    outputFile.write('\nStudent records by letter grades:\n\n')
    
    for item in sortedByGrades:
        outputFile.write(item._studentID)
        outputFile.write('  ')
        outputFile.write(str(item._studentGrade) + '\n')
        
def main():
    '''calls the functions'''
    
    studentList = recordReader()
    sortedByGrades = gradeSorter(studentList)
    sortedByID = alphaSorter(studentList)
    recordWriter(sortedByGrades, sortedByID)
    
main()