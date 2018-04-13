dataSet = []

def importFiles(fileNames):
    for fileName in fileNames:
        with open(fileName, 'r+') as f:
            firstline = f.readline().rstrip()
            secondline = f.readline().rstrip()
            thirdline = f.readline()

            usernameItem = firstline
            hashtagsItem = secondline
            followersInThousandsItem = float(thirdline) / 1000

            dataSet.append([usernameItem, hashtagsItem, followersInThousandsItem])

            f.close()

importFiles("crypticloop.txt")