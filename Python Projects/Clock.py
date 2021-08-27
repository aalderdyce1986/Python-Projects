# Clock Program
from time import *

  def update():
    timeString = strftime('%I:%M:%S %p')
    timeLabel.config(text=timeString)

    dayString = strftime('%A')
    dayLabel.config(text=dayString)

    dateString = strftime('%B %d, %Y')
    dateLabel.config(text=dateString)

    win.after(1000,update)


win = Tk()

timeLabel = Label(win,font=("Arial",50),fg="#00FF00",bg="black")
timeLabel.pack()

dayLabel = Label(win,font=("Ink Free",30))
dayLabel.pack()

dateLabel = Label(win,font=("Ink Free",25))
dateLabel.pack()

update()



win.mainloop()