import os

myPath = r"D:\SteamLibrary\steamapps\common\Democracy 3\Polska2015\data\missions\Polska2015\polska2015.txt"
myRoot = r"D:\SteamLibrary\steamapps\common\Democracy 3\Polska2015"

# Find all extra characters, possible Polish signs
allFiles = [os.path.join(root, file)
            for root, dirs, files in os.walk(myRoot) for file in files if file[-4:] in [".txt", ".csv"]]

allChars = bytes()
for filepath in allFiles:
    with open(filepath, "rb") as myFile:
        allChars += myFile.read()
        allChars = bytes(set(allChars))

print("Show all values of bytes above 126")
allChars = sorted(filter(lambda x: x > 126, allChars))
for char in allChars:
    print(char)

# put all those chars into text, together with their byte value, to show how they appear within a game
if False:
    insertion = bytes()
    for nr in allChars:
        insertion += bytes(f" {nr} ", encoding="utf-8")
        insertion += bytes([nr])
        
    with open(myPath, "rb") as myFile:
        text = myFile.read()

    newText = text[:377] + insertion + text[979:]
    with open(myPath, "wb") as myFile:
        myFile.write(newText)
    
    # If you run the game, description of Polska2015 mission will show polish signs and their byte values.
    # By the way, it showed some letters with diactrics outside of Polish language. Those are to be fixed
'''
153 error due to wrong encoding in party names "Nowocześni" and "Lewicowych Demokratów "partynames.txt
159 Ó
163 Shows as pound ingame. Should be Polish Ł in Liczer.txt
175 unicode u with dot above (\xc5\xaf) instead of Polish ł in partynames.txt
187 part of UTF-8 BOM signature xef\xbb\xbf. Wrong encoding in partynames.txt
191 part of UTF-8 BOM signature xef\xbb\xbf. Wrong encoding in partynames.txt
196 Ą
197 unicode u with dot above (\xc5\xaf) instead of Polish ł in partynames.txt
202 Ś
203 Ź
206 Ż
211 wrong encoding of Polish Ó in sliders.csv
214 Ć
217 Ł
219 Ń
220 Ę
228 ą
234 ś
235 ź
238 ż
239 part of UTF-8 BOM signature xef\xbb\xbf. partynames.txt was saved with wrong encoding
241 wrong Polish ń in simulation.csv
246 ć
249 ł
251 ń
252 ę
255 ó
'''

# Investigate those strange chars, outside of Polish diactrics
strangeChars = bytes([153, 163, 175, 187, 191, 197, 211, 239, 241])

for filepath in allFiles:
    with open(filepath, "rb") as myFile:
        filenamePrinted = False
        lines = myFile.readlines()
        for line in lines:
            for char in strangeChars:
                if char in line:
                    if not filenamePrinted:
                        filenamePrinted = True
                        print(f"\n{filepath}")
                    print(f"{char} {line}")
