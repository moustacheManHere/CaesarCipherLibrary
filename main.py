import sys

sys.dont_write_bytecode = True

import Ram

if __name__ == "__main__":

    prog = Ram.GetsFullMarks()
    if prog.checkVitals() is not None:
        prog.output.print_start()
        prog.run()
        prog.output.print_end()
