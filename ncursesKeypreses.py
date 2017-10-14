import curses as curses

ncols, nlines = 20, 20
uly, ulx = 20, 20

stdscr = curses.initscr()
#stdscr = curses.newwin(nlines, ncols, uly, ulx)
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up")
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "Down")

curses.endwin()
