import sys
import time

indentIncreasing = True
indent = 0

try: 
    # infinite loop of the program
    while True:
        # indent printing depending on how many indents are stored
        # spaces x amount of indents, no end space so starts print next to indents
        print(' ' * indent, end='')
        print('******')
        time.sleep(0.1)
        # timer for 0.1 seconds before printing next line

        # if indent is increasing (moving to the right) + 1 to indent variable.
        if indentIncreasing:
            indent += 1
            # if spaces on left reach 20 then change directions
            if indent == 20:
                indentIncreasing = False
        else:
            # decreasing indent spacing so stars move back to left
            indent -= 1
            # if indent spacing reaches 0 change direction again
            if indent == 0:
                indentIncreasing = True

# program to execute until someone hits the exit commmand ctrl + c
except KeyboardInterrupt:
    sys.exit('program exited')
