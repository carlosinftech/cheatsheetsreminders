class FileReader:
    def __init__(self):
        self.__content = ''

    def readFile(self,path,readorwrite):
        f = open(path,readorwrite)
        self.__content = f.read()
        f.close()

    def printContent(self):
        print(self.__content)

    def contextManager(self,path,readorwrite):
        with open(path,readorwrite) as f:
            self.__content = f.read()
            self.printContent()
            print('is closed: ', f.closed)
        print('is closed: ', f.closed)

    def readLineByLine(self,path,readorwrite):
        with open(path,readorwrite) as f:
            for line in f:
                print(line, end='')

    def readRangeOfLines(self,path, readorwrite,beggining,end):
        with open(path, readorwrite) as f:
            for x in range (0,end):
                line = f.readline()
                if x in range(beggining,end):
                    print(x, line, end='')

fr = FileReader()
# fr.readFile('C:\carlos\csvExample.csv','r')
# fr.printContent()
# fr.contextManager('C:\carlos\csvExample.csv','r')
# fr.readLineByLine('C:\carlos\csvExample.csv','r')
# fr.readRangeOfLines('C:\carlos\csvExample.csv','r',4,6)