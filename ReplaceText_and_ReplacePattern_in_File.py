# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:15:14 2020

@author: ln83883
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:50:41 2020

@author: ln83883
"""

import re
import codecs
#from tempfile import mkstemp
#from shutil import move
#from os import remove

def replaceText( filePath, old_text, new_text, flags=0 ):
    """This function reads contents from a file as a single string, and then
    performs a find/replace for the input text throughout the file.
    The input is interpretted at raw/litteral text. To ignore upper/lowercase,
        use: flags=re.IGNORECASE
    """
    # open file
    with codecs.open( filePath, "r+",'utf-8' ) as file:

        # Read contents from file as a single string
        fileContents = file.read()
        # Compile regex pattern from litteral text
        textPattern = re.compile( re.escape( old_text ), flags )
        # Count number of matches
        num_matches = str(len(re.findall(textPattern, fileContents)))
        # Count number of matches
        num_matches = str(len(re.findall(textPattern, fileContents)))
        # Find regex pattern matches and replace with new text
        fileContents = textPattern.sub( new_text, fileContents )
        # reset the read/write pointer to beginning of file
        file.seek( 0 )
        # Clear the original contents of the file
        file.truncate()
        # Write the new content with replacements to the file
        file.write( fileContents )
        # Report number of matches found/replaced
        if num_matches == 1:
            print(str(num_matches) + " replacement made.")
        else:
            print(str(num_matches) + " replacements made.")

def replacePattern( filePath, regex, replacement, flags=re.MULTILINE):
    """This function reads contents from a file as a single string, and then
    uses a regular expression to match instances of the input pattern and
    replaces them throughout a file. To add additional regex flags, use the
    following syntax:  flags=re.MULTILINE | <additional flag>
    example:
        replacePattern(file path, wksp, r"^.*TEST", r"hedgehog", replacement,
                       flags=re.MULTILINE | re.IGNORECASE)
    """
    # open file
    with codecs.open( filePath, "r+",'utf-8' ) as file:

        # Read contents from file as a single string
        fileContents = file.read()
        # Compile regex pattern
        textPattern = re.compile( regex, flags )
        # Count number of matches
        num_matches = str(len(re.findall(textPattern, fileContents)))
        # Find regex pattern matches and replace with new text
        fileContents = textPattern.sub( replacement, fileContents )
        # reset the read/write pointer to beginning of file
        file.seek( 0 )
        # Clear the original contents of the file
        file.truncate()
        # Write the new content with replacements to the file
        file.write( fileContents )
        # Report number of matches found/replaced
        if num_matches == 1:
            print(str(num_matches) + " replacement made.")
        else:
            print(str(num_matches) + " replacements made.")

#def findMatches( filePath, regex, flags=re.MULTILINE):
#        # Read contents from file as a single string
#        fileContents = file.read()
#        # Compile regex pattern
#        textPattern = re.compile( regex, flags )
#        matches = re.findall(textPattern, fileContents)
#        # Count number of matches
#        num_matches = (len(matches))
#        if num_matches == 1:
#            print(num_matches + " match found at:\n")
#        elif num_matches > 0:
#            print(num_matches + " matches found at:\n")
#        else:
#            print(str(num_matches) + "matches found.")

wksp = r"D:\Liam\Python_Workspace\Scratch\test4.txt"

replacePattern(wksp, r"^.*TEST", r"hedgehog", flags=re.MULTILINE | re.IGNORECASE)
#replaceText(wksp, "lazy","relaxed")
# replaceText(wksp, "duck", "Fox")

with open(wksp,"r") as file:
    read = file.read()
    print("\n")
    print(read)


#import codecs
#
#from tempfile import mkstemp
#from shutil import move
#from os import remove
#
#
#def replace(source_file_path, pattern, substring):
#    fh, target_file_path = mkstemp()
#
#    with codecs.open(target_file_path, 'w', 'utf-8') as target_file:
#        with codecs.open(source_file_path, 'r', 'utf-8') as source_file:
#            for line in source_file:
#                target_file.write(line.replace(pattern, substring))
#    remove(source_file_path)
#    move(target_file_path, source_file_path)
#


#
#myfile = '''I think I like ducks.  Ducks seem pretty good.  They swim. They fly. Waddling is ok.
#Ducks are pretty shit on land, although they look cute and all.
#Is this enough text?  I think I like the idea.  And Ducks.  Ducks are fab.
#Duck duck ducky duckduckface!
#Quack!'''
#
#text = myfile
#
#patternLST = [r'[D|d]uck', r'[D|d]ucky']
#patterns = [ re.compile(p) for p in patternLST ]
#
#
#for match in re.findall(pattern,text):
#
#
#
#for pattern in patterns:
#    print('Looking for: ' + pattern + '\nin:\n\n ' + text + '-->')
#
#    if regex.search(text):
#        s = match.start()
#        e = match.end()
#        print('found a match!' + regex + " located at: " + s + ":" + e)
#    else:
#        print("no match")


