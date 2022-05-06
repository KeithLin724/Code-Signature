'''
Code signature
written: KYLiN
This is a code build date and time display
Date: 05/07/22
'''

from tkinter import *
from datetime import datetime as dt


class DateTimeFrame:
    def __init__(self, frame) -> None:
        self.Frame = Frame(frame)

        self.labelStr = Label(self.Frame,
                              text='Date:',
                              font=('Arial', 12)).pack(side=LEFT)
        self.showDateLabel = Label(self.Frame)
        self.showDateLabel.pack(side=LEFT)

        self.Frame.pack()

    # init the time reload
    def initTime(self) -> None:
        timeStr = dt.now()
        timeStr = timeStr.strftime('%x')
        self.showDateLabel.config(text=timeStr)
        self.showDateLabel.after(1000, self.initTime)

    def get_time() -> str:
        return dt.now().strftime('%x')
