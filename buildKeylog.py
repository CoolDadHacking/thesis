#### buildKeylog.py
#### records audio and labels to files in working directory
## Rambo You
## University of Minnesota
## Capstone MSST 2017
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
import string, time, csv, sys, sh

#variables
startTime = time.time()
keyPressFile = sys.argv[1] + '.csv' #choose filename once started
audioFile = sys.argv[1] + '.wav' 
print('Enter ‘:’ key to stop recording')
with open(keyPressFile, 'w') as csvfile:
   fieldnames = ['keyPressed','timestamp']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   while 1:
        pressed  = stdscr.getch()
        #functional if else seems faster than calling class
        if pressed  == ord('a'):
            writer.writerow({'keyPressed':'a','timestamp':time.time()-startTime})
        elif pressed  == ord('b'):
            writer.writerow({'keyPressed':'b','timestamp':time.time()-startTime})
        elif pressed  == ord('c'):
            writer.writerow({'keyPressed':'c','timestamp':time.time()-startTime})
        elif pressed  == ord('d'):
            writer.writerow({'keyPressed':'d','timestamp':time.time()-startTime})
        elif pressed  == ord('e'):
            writer.writerow({'keyPressed':'e','timestamp':time.time()-startTime})
        elif pressed  == ord('f'):
            writer.writerow({'keyPressed':'f','timestamp':time.time()-startTime})
        elif pressed  == ord('g'):
            writer.writerow({'keyPressed':'g','timestamp':time.time()-startTime})
        elif pressed  == ord('h'):
            writer.writerow({'keyPressed':'h','timestamp':time.time()-startTime})
        elif pressed  == ord('i'):
            writer.writerow({'keyPressed':'i','timestamp':time.time()-startTime})
        elif pressed  == ord('j'):
            writer.writerow({'keyPressed':'j','timestamp':time.time()-startTime})
        elif pressed  == ord('k'):
            writer.writerow({'keyPressed':'k','timestamp':time.time()-startTime})
        elif pressed  == ord('l'):
            writer.writerow({'keyPressed':'l','timestamp':time.time()-startTime})
        elif pressed  == ord('m'):
            writer.writerow({'keyPressed':'m','timestamp':time.time()-startTime})
        elif pressed  == ord('n'):
            writer.writerow({'keyPressed':'n','timestamp':time.time()-startTime})
        elif pressed  == ord('o'):
            writer.writerow({'keyPressed':'o','timestamp':time.time()-startTime})
        elif pressed  == ord('p'):
            writer.writerow({'keyPressed':'p','timestamp':time.time()-startTime})
        elif pressed  == ord('q'):
            writer.writerow({'keyPressed':'q','timestamp':time.time()-startTime})
        elif pressed  == ord('r'):
            writer.writerow({'keyPressed':'r','timestamp':time.time()-startTime})
        elif pressed  == ord('s'):
            writer.writerow({'keyPressed':'s','timestamp':time.time()-startTime})
        elif pressed  == ord('t'):
            writer.writerow({'keyPressed':'t','timestamp':time.time()-startTime})
        elif pressed  == ord('u'):
            writer.writerow({'keyPressed':'u','timestamp':time.time()-startTime})
        elif pressed  == ord('v'):
            writer.writerow({'keyPressed':'v','timestamp':time.time()-startTime})
        elif pressed  == ord('w'):
            writer.writerow({'keyPressed':'w','timestamp':time.time()-startTime})
        elif pressed  == ord('x'):
            writer.writerow({'keyPressed':'x','timestamp':time.time()-startTime})
        elif pressed  == ord('y'):
            writer.writerow({'keyPressed':'y','timestamp':time.time()-startTime})
        elif pressed  == ord('z'):
            writer.writerow({'keyPressed':'z','timestamp':time.time()-startTime})
        elif pressed  == ord('A'):
            writer.writerow({'keyPressed':'A','timestamp':time.time()-startTime})
        elif pressed  == ord('B'):
            writer.writerow({'keyPressed':'B','timestamp':time.time()-startTime})
        elif pressed  == ord('C'):
            writer.writerow({'keyPressed':'C','timestamp':time.time()-startTime})
        elif pressed  == ord('D'):
            writer.writerow({'keyPressed':'D','timestamp':time.time()-startTime})
        elif pressed  == ord('E'):
            writer.writerow({'keyPressed':'E','timestamp':time.time()-startTime})
        elif pressed  == ord('F'):
            writer.writerow({'keyPressed':'F','timestamp':time.time()-startTime})
        elif pressed  == ord('G'):
            writer.writerow({'keyPressed':'G','timestamp':time.time()-startTime})
        elif pressed  == ord('H'):
            writer.writerow({'keyPressed':'H','timestamp':time.time()-startTime})
        elif pressed  == ord('I'):
            writer.writerow({'keyPressed':'I','timestamp':time.time()-startTime})
        elif pressed  == ord('J'):
            writer.writerow({'keyPressed':'J','timestamp':time.time()-startTime})
        elif pressed  == ord('K'):
            writer.writerow({'keyPressed':'K','timestamp':time.time()-startTime})
        elif pressed  == ord('L'):
            writer.writerow({'keyPressed':'L','timestamp':time.time()-startTime})
        elif pressed  == ord('M'):
            writer.writerow({'keyPressed':'M','timestamp':time.time()-startTime})
        elif pressed  == ord('N'):
            writer.writerow({'keyPressed':'N','timestamp':time.time()-startTime})
        elif pressed  == ord('O'):
            writer.writerow({'keyPressed':'O','timestamp':time.time()-startTime})
        elif pressed  == ord('P'):
            writer.writerow({'keyPressed':'P','timestamp':time.time()-startTime})
        elif pressed  == ord('Q'):
            writer.writerow({'keyPressed':'Q','timestamp':time.time()-startTime})
        elif pressed  == ord('R'):
            writer.writerow({'keyPressed':'R','timestamp':time.time()-startTime})
        elif pressed  == ord('S'):
            writer.writerow({'keyPressed':'S','timestamp':time.time()-startTime})
        elif pressed  == ord('T'):
            writer.writerow({'keyPressed':'T','timestamp':time.time()-startTime})
        elif pressed  == ord('U'):
            writer.writerow({'keyPressed':'U','timestamp':time.time()-startTime})
        elif pressed  == ord('V'):
            writer.writerow({'keyPressed':'V','timestamp':time.time()-startTime})
        elif pressed  == ord('W'):
            writer.writerow({'keyPressed':'W','timestamp':time.time()-startTime})
        elif pressed  == ord('X'):
            writer.writerow({'keyPressed':'X','timestamp':time.time()-startTime})
        elif pressed  == ord('Y'):
            writer.writerow({'keyPressed':'Y','timestamp':time.time()-startTime})
        elif pressed  == ord('Z'):
            writer.writerow({'keyPressed':'Z','timestamp':time.time()-startTime})
        elif pressed  == ord('1'):
            writer.writerow({'keyPressed':'1','timestamp':time.time()-startTime})
        elif pressed  == ord('2'):
            writer.writerow({'keyPressed':'2','timestamp':time.time()-startTime})
        elif pressed  == ord('3'):
            writer.writerow({'keyPressed':'3','timestamp':time.time()-startTime})
        elif pressed  == ord('4'):
            writer.writerow({'keyPressed':'4','timestamp':time.time()-startTime})
        elif pressed  == ord('5'):
            writer.writerow({'keyPressed':'5','timestamp':time.time()-startTime})
        elif pressed  == ord('6'):
            writer.writerow({'keyPressed':'6','timestamp':time.time()-startTime})
        elif pressed  == ord('7'):
            writer.writerow({'keyPressed':'7','timestamp':time.time()-startTime})
        elif pressed  == ord('8'):
            writer.writerow({'keyPressed':'8','timestamp':time.time()-startTime})
        elif pressed  == ord('9'):
            writer.writerow({'keyPressed':'9','timestamp':time.time()-startTime})
        elif pressed  == ord('0'):
            writer.writerow({'keyPressed':'0','timestamp':time.time()-startTime})
        elif pressed == ord('.') or 46:
            writer.writerow({'keyPressed':'.','timestamp':time.time()-startTime})
        elif pressed  == ord(' '):
            writer.writerow({'keyPressed':'space','timestamp':time.time()-startTime})
        elif pressed  == 127: #backspace key
            writer.writerow({'keyPressed':'backspace','timestamp':time.time()-startTime})
        elif pressed == 10: #enter key
            writer.writerow({'keyPressed':'return','timestamp':time.time()-startTime})
        elif pressed  == ord(':'):
            sh.killall('sox')
            break #exit loop
