#
#import modules
#
from pymxs import runtime as mxs
import os

#
#define a master folder and suffix name
#

folder = r"Y:\_assetPacksRe\_unknown\3d model GROHE\Grohtherm"

convertedEndingName = "_BUILD"

# Find any .max files in the folder specified, if max exist, open, export # entire scene to fbx.
for root, dirs, files in os.walk(folder):
    for item in files:
        if item.endswith((".max", ".MAX")):
            filePath = os.path.join(root, item)
            filePath = filePath.replace('\\', '\\\\')
            print(filePath)

            filePathExported = filePath.replace('.max', '').replace('.MAX', '')
            mxs.loadMaxFile(filePath, quiet=True, prompt=False, useFileUnits=False)

            filePathExported = filePathExported + '_MAX' + convertedEndingName + '.fbx'
            print(filePathExported)

            mxs.exportFile(filePathExported, mxs.Name('noPrompt'), selectedOnly=False)

# run the script in the maxscript console
os.system('maxscript "Y:\_assetPacksRe\_unknown\3d model GROHE\Grohtherm\alipars.ms"')