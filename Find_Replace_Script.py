import re

def findMatches( filePath, regex, flags=0):
    with codecs.open( filePath, "r+",'utf-8' ) as file:
        # Read contents from file as a single string
        fileContents = file.read()
        # Compile regex pattern
        textPattern = re.compile( regex , flags )
        matches = re.findall(textPattern, fileContents)
        # Count number of matches
        num_matches = (len(matches))


        if num_matches > 0:
            print(str(num_matches) + " matches found at:\n")
            for match in matches:
                print(match)
                match
#                print("\t" + str(s) + ":" + str(e))
        else:
            print(str(num_matches) + " matches found.")

wksp = r"D:\Liam\Python_Workspace\Scratch\test4.txt"

findMatches(wksp, "dog")