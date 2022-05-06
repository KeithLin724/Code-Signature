'''
Code signature
written: KYLiN
This is a code of Entry , using tkinter Entry and label
Date: 05/07/22
'''

from tkinter import *


class kyEntry:
    def __init__(self, frame, entryName: str) -> None:

        self.__Frame = Frame(frame)
        # label for display
        self.__label = Label(self.__Frame,
                             text=entryName,
                             width=20,
                             font=('Arial', 12)).pack(side=LEFT)
        # entry
        self.__entry = Entry(self.__Frame)
        self.__entry.pack(side=LEFT)

        self.__Frame.pack()

    # get input string for entry
    def get_enter_input(self) -> str:
        return self.__entry.get()

    # clear screen
    def clear_entry(self) -> None:
        self.__entry.delete(0, END)
