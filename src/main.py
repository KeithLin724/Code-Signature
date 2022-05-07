'''
Code signature
written: KYLiN
This is a main code of "Code signature"
Date: 05/07/22
'''

from tkinter import *
# IMPORT:
from KY_Entry import kyEntry
from DateTimeFrame import DateTimeFrame
from signatureBuilder import signature_Builder, LANGUAGES_COMMENT


def build_signature() -> None:  # make signature
    outSignatureText.delete(1.0, END)
    bodyInputStr = bodyText.get('1.0', END)
    signatureStr = signature_Builder(name=clientName.get_enter_input(),
                                     title=clientTitle.get_enter_input(),
                                     date=DateTimeFrame.get_time(),
                                     body=bodyInputStr,
                                     lang=langChoose.get())
    outSignatureText.insert(1.0, signatureStr)
    print(signatureStr)  # debug


def clear_all() -> None:  # clear function
    print('clear all')
    clientName.clear_entry()
    clientTitle.clear_entry()
    bodyText.delete(1.0, END)
    outSignatureText.delete(1.0, END)


def clear_Text() -> None:  # cleat text
    print('clear text')
    bodyText.delete(1.0, END)


# def out():  # debug
#    print(langChoose.get())


def main() -> None:
    global window
    window = Tk()
    window.title('Code Signature (Design by KYLiN)')
    #icon = PhotoImage(file='src\\photo\\icon.png')
    #window.iconphoto(True, icon)

    # user frame
    userFrame = Frame(window)

    global clientName
    clientName = kyEntry(entryName='Name: ', frame=userFrame)

    global clientTitle
    clientTitle = kyEntry(entryName='Title: ', frame=userFrame)

    # body
    bodyLabel = Label(userFrame,
                      text='Body: ',
                      font=('Arial', 12)).pack()
    global bodyText
    bodyText = Text(userFrame, height=30, width=30)
    bodyText.pack()

    clearText = Button(userFrame,
                       text='clear Body',
                       width=8,
                       command=clear_Text).pack(side=BOTTOM)

    userFrame.pack(side=LEFT)

    # button
    buttonFrame = Frame(window)
    runCodeSignature = Button(buttonFrame,  # NOTE: run signature
                              text='Build',
                              width=8,
                              command=build_signature).pack()

    clearAll = Button(buttonFrame,  # NOTE: clear Text
                      text='clear',
                      width=8,
                      command=clear_all).pack()

    buttonFrame.pack(side=BOTTOM)

    # NOTE:output frame
    outputFrame = Frame(window)
    # StringVar
    global langChoose
    lang = [i for i in LANGUAGES_COMMENT.keys()]
    langChoose = StringVar(outputFrame)
    langChoose.set(lang[0])

    langChooseOptionMenu = OptionMenu(outputFrame, langChoose, *lang)
    langChooseOptionMenu.pack()

    global outSignatureText
    outSignatureText = Text(outputFrame)
    outSignatureText.pack()

    global dateTimeOut
    dateTimeOut = DateTimeFrame(outputFrame)
    dateTimeOut.initTime()
    outputFrame.pack(side=RIGHT)

    #Button(window, text='debug', command=out).pack()

    # end of window loop
    window.mainloop()


if __name__ == '__main__':
    main()
