#!/usr/bin/python
import sys
import glob
import os
import copy
import string

def searchFolder(theFolder, virusDefs):
	print(theFolder)
	items = glob.glob(theFolder + "*");
	for x in items:
		if os.path.isdir(x):
			print("It's a directory")
			print(x)
			searchFolder(x +"/", virusDefs)
		else:
			print("It's a file!")
			print(x)
			byteString = ""
			testing = open(x, "rb")
			fileBytes = bytearray(testing.read())
			for definition in virusDefs:
				if definition in fileBytes:
					print("This File is Infected With a Virus")
					newDefinition = copy.copy(definition)
					deflength = len(newDefinition) -1
					coutner = deflength
					while coutner > (deflength -4):
						newDefinition[coutner] = 'x'
						coutner = coutner - 1
					defLocation = fileBytes.find(definition)

					i = 0
					while i < len(definition):
						fileBytes[defLocation + i] = newDefinition[i] 
						i = i + 1
					print("Sanitizing File, replacing last 4 bits of signature with XXXX")
					fileHandle = open(x, "w")
					fileHandle.write(fileBytes);
					fileHandle.close()
					fileName = os.path.basename(x)
					print("Quarantining file, moving to /home/cbeau132/workspace/Security/Lab4/a/BadFiles/")
					os.rename(x, "/home/cbeau132/workspace/Security/Lab4/a/BadFiles/" + fileName)
			testing.close()
			
			
def loadDefinitions(fileName):
	return open(fileName).readlines()
	

listOfArgs = sys.argv
virusDefs = []
definitions = loadDefinitions(listOfArgs[2]);
for defss in definitions:
	print
	virusDefs.append(bytearray(defss,"utf-8"));
#virusDefs.append(bytearray("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", "utf-8"))
searchFolder(listOfArgs[1], virusDefs)

