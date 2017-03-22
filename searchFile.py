import os
import threading
import win32api
from os.path import join

lookfor = "uploadFile.txt"

class myThread(threading.Thread):
    Gloflag = False
    def __init__(self, threadId, drive):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.drive = drive

    def run(self):
        self.drive = self.drive
        print self.drive
        for root, dirs, files in os.walk(self.drive):
            if myThread.Gloflag == True:
                break

            print self.threadId,"  searching", root
            if lookfor in files:
                myThread.Gloflag = True
                print "found: %s" % join(root, lookfor)
                break


if __name__ == "__main__":
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]


    for i in drives:
        thread1 = myThread("Thread-" + i, str(i))
        thread1.start()

