import os

# defail class for hold variables
class vars:
    rootSerchPath = ""
    ZipFileName =""

    @staticmethod
    def Initialize():
        vars.rootSerchPath = vars.getRootSerchPath(os.sys.argv)
        vars.ZipFileName = vars.getZipFileName(os.sys.argv)

    # get value from command line arguments  default value="archive.zip"
    @staticmethod
    def getZipFileName(args):
        if len(args) == 2:
            return args[1]
        else:
            return "archive.zip"

    # get value from command line arguments item 2  default value=r'\\NAS3F6715\Multimedia\_Materials\CGAxis PBR Textures
    # Collection\CGAxis PBR Textures Volume 18 - Wood'
    # as static

    def getRootSerchPath(args):
        if len(args) == 3:
            return args[2]
        else:
            return r'\\NAS3F6715\Multimedia\_Materials\CGAxis PBR Textures Collection\CGAxis PBR Textures Volume 18 - Wood'
