#@+leo-ver=4-thin
#@+node:ville.20090815203828.5235:@thin spydershell.py
#@<< docstring >>
#@+node:ville.20090815203828.5236:<< docstring >>
''' Launch spyder environment with access to Leo instance

http://source.pythonxy.com/spyder/doc/

Usage:

Execute alt-x spyder-launch to start spyder

Execute alt-x spyder-update to pass current c,p,g to spyder
interactive session. spyder-update also shows the window
if it was closed before.

'''
#@-node:ville.20090815203828.5236:<< docstring >>
#@nl

__version__ = '0.0'
#@<< version history >>
#@+node:ville.20090815203828.5237:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 VMV First version
# 
# 0.2 VMV name changed to "spyder' (was "pydee")
#@-at
#@-node:ville.20090815203828.5237:<< version history >>
#@nl

#@<< imports >>
#@+node:ville.20090815203828.5238:<< imports >>
import sys

import leo.core.leoGlobals as g
import leo.core.leoPlugins as leoPlugins

# Whatever other imports your plugins uses.
#@nonl
#@-node:ville.20090815203828.5238:<< imports >>
#@nl

#@+others
#@+node:ville.20090815203828.5239:init
def init ():
    ok = g.app.gui.guiName() == 'qt'    
    return ok

#@-node:ville.20090815203828.5239:init
#@+node:ville.20090815203828.5240:Leo commands
@g.command('spyder-launch')
def spyder_launch(event):
    """ Launch spyder """
    # Options
    from spyderlib import spyder
    commands, intitle, message, options = spyder.get_options()

    # Main window
    g.spyder = main = spyder.MainWindow(commands, intitle, message, options)
    main.setup()
    g.spyderns = main.console.shell.interpreter.namespace
    spyder_update(event)
    main.show()

@g.command('spyder-light')
def spyder_light(event):
    """ Launch spyder in "light" mode """
    oldarg = sys.argv
    sys.argv = ['spyder', '--light']
    spyder_launch(event)
    sys.argv = oldarg


@g.command('spyder-update')
def spyder_update(event):
    """ Reset commander and position to current in pydee session 

    Also shows pydee window if it was closed earlier

    """    

    c = event['c']
    ns = g.spyderns
    ns['c'] = c
    ns['g'] = g
    ns['p'] = c.p
    g.spyder.show()
#@-node:ville.20090815203828.5240:Leo commands
#@-others
#@nonl
#@-node:ville.20090815203828.5235:@thin spydershell.py
#@-leo
