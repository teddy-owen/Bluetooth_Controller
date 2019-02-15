"""
Bluetooth Controls

Controls class is constructed to set
functions to execute on various input
over bluetooth

Ex:
    # define on, off, slider and other functions
    c = controls.Controls(on=on,off=off,slider=slider,other=other)
    # set a class variable to be accessed via self within the function
    c.proc = None
    # begin listening for bluetooth input
    c.begin()

Event types are set here, and can be changed.
floats representing 0-1 are considered a slider event.
"""

import BT_input_stream as input

def _default_action(self):
    return None

class Controls():
    
    START = "START"
    SELECT = "SELECT"
    SQUARE = "SQUARE"
    TRIANGLE = "TRIANGLE"
    CROSS = "CROSS"
    CIRCLE = "CIRCLE"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    ON = "ON"
    OFF = "OFF"

    def __init__(self,
        slider=_default_action,
        on=_default_action,
        off=_default_action,
        start=_default_action,
        select=_default_action,
        square=_default_action,
        triangle=_default_action,
        cross=_default_action,
        circle=_default_action,
        up=_default_action,
        down=_default_action,
        left=_default_action,
        right=_default_action,
        other=_default_action,
        **kwargs):
        
        self.slider = slider
        self.on = on
        self.off = off
        self.start = start
        self.select = select
        self.square = square
        self.triangle = triangle
        self.cross = cross
        self.circle = circle
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.other = other
    
    def begin(self):
        for event in input.stream_input():
            if isinstance(event, float):
                self.slider(self,event)
            elif event == self.ON:
                self.on(self)
            elif event == self.OFF:
                self.off(self)
            elif event == self.START:
                self.start(self)
            elif event == self.SELECT:
                self.select(self)
            elif event == self.SQUARE :
                self.square(self)
            elif event == self.TRIANGLE:
                self.triangle(self)
            elif event == self.CROSS:
                self.cross(self)
            elif event == self.CIRCLE:
                self.circle(self)
            elif event == self.UP:
                self.up(self)
            elif event == self.DOWN:
                self.down(self)
            elif event == self.LEFT:
                self.left(self)
            elif event == self.RIGHT:
                self.right(self)
            else:
                self.other(self,event)


