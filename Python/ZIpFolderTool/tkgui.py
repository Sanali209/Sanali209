#gui part of application

#use tkinter to create a window

#Import modules
from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

from programvar import vars as pv
from SLM.FuncModule import *

#create ui for application


class Application(Tk):

    def __init__(self):
        super().__init__()

        self.createWindow()
        self.createWidgets()
        self.start()

    # defain window setings and layout
    def createWindow(self):

        self.title("Zip Files tool")
        self.geometry("800x600")
        self.resizable(True, True)


        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=80 )
        self.grid_rowconfigure(2, weight=1)



    #defain fields for gui elements
    rootSearchPathV: StringVar
    #defain field for log
    logV: StringVar
    LOGVALUE = "123"


    # 2 fielsd and 1 button with text "Zip"
    # button "Zip" will call function zipFiles
    # 2 fields will be filled with values rootSerchPath and ZipFileName
    def createWidgets(self):

        self.label1 = Label(self, text="Root Search Path")
        self.label1.grid(row=0, column=0, sticky=W)

        #create text field viz as drag end drop target for explorer window
        self.rootSearchPathV = StringVar()
        self.rootSearchPathV.set(pv.rootSerchPath)
        print(self.rootSearchPathV.get())
        rootSearchPathField = Entry(self, textvariable=self.rootSearchPathV)
        rootSearchPathField.grid(row=0, column=1, sticky=NSEW)

        # create label with text "Log"
        label4 = Label(self, text="Log", background='#f0f0f0')
        label4.grid(row=1, column=0, sticky=W)

        # create text list for zipping logs files
        self.logV = StringVar()
        self.logV.set(self.LOGVALUE)
        self.log_field = Listbox(self, width=50, height=10)
        self.log_field.textvariable = self.logV
        self.log_field.grid(row=1, column=1, sticky=NSEW)
        #show scrollbar for log listbox
        yscrollbar = Scrollbar(self, orient=VERTICAL, command=self.log_field.yview)
        yscrollbar.grid(row=1, column=2, sticky=NSEW)
        self.log_field.configure(yscrollcommand=yscrollbar.set)

        #create button with teht help and show help window
        self.help_button = Button(self, text="Help", command=self.showHelpWindow)
        self.help_button.grid(row=2, column=0, sticky=W)



        # create button with text "Zip"
        zipButton = Button(self, text="Zip", command=self.zipFiles)
        zipButton.grid(row=2, column=1, sticky=NSEW)

        # create button with text "Browse"
        browseButton = Button(self, text="Browse", command=self.askdirectory)
        browseButton.grid(row=0, column=2, sticky=NSEW)

    # defain function to handle help button event
    def showHelpWindow(self):
        # create help window
        self.help_window = Toplevel(self)
        self.help_window.title("Help")
        self.help_window.geometry("800x600")
        self.help_window.resizable(True, True)
        self.help_window.grid_columnconfigure(0)
        self.help_window.grid_columnconfigure(1, weight=1)

        # add help text "This application will zip all files in the root search path.
        # affect onli on subdirectories located in the root search path."
        self.help_window.text = Text(self.help_window, width=80, height=20)

        self.help_window.text.insert(END, "This application will zip all files in the root search path.\n")
        self.help_window.text.insert(END, "affect onli on subdirectories located in the root search path.\n")
        self.help_window.text.grid(row=0, column=0, sticky=W)

    # defain function to handle askdirectory event
    def askdirectory(self):
        #get file path from askdirectory event
        file_path = filedialog.askdirectory()
        self.rootSearchPathV.set(file_path)

    # defain function zipFiles
    def zipFiles(self):
        #get values from fields
        pv.rootSerchPath = self.rootSearchPathV.get()

        Directories = getDirectories(pv.rootSerchPath)
        # print directories to zippingLogs listbox
        for curDir in Directories:
            printToConsoleAndFile("Zipping directory: " + curDir)
            #print to log listbox
            self.log_field.insert(END, "Zipping directory: " + curDir)

        # show os.sys.argv for debug
        print(os.sys.argv)

        for curZipDir in Directories:
            print("Zipping files in directory: " + curZipDir + " to file: " + pv.ZipFileName)
            ZipingFiles: list[str] = getZipingdFiles(curZipDir)

            arhiveFilepath: str = os.path.join(curZipDir, pv.ZipFileName)

            if ZipingFiles and not os.path.exists(arhiveFilepath):

                # display arhiveFilepath details name and list of files in poup gui window and save to csv file
                print("arhiveFilepath: " + arhiveFilepath)
                print("ZipingFiles: " + str(ZipingFiles))

                with ZipFile(arhiveFilepath, 'w') as zip:

                    for curFilePath in ZipingFiles:
                        zip.write(os.path.join(curZipDir, curFilePath), curFilePath)

                    for curFilePath in ZipingFiles:
                        os.remove(os.path.join(curZipDir, curFilePath))

    # start application
    def start(self):
        self.mainloop()

    # defain function to handle drop event
    def on_drop(self, event):
        #get file path from drop event
        file_path = event.data.decode('utf-8')
        self.rootSearchPathV.set(file_path)
