"""
Example of Bluetooth Controller

`sudo python3 example.py` and connect your device

Run this w/ bluetooth (usually root) privileges
"""

import BT_controls as controls

def on(self):
    print("on")
    return

def off(self):
    print("off")
    return

def up(self):
    self.count +=1
    print(self.count)
    return

def down(self):
    self.count -=1
    print(self.count)
    return

def slider(self,event):
    print(event)
    return

def other(self,event):
    print(event)
    return

if __name__ == "__main__":
    c = controls.Controls(on=on,off=off,up=up,down=down,slider=slider,other=other)
    c.count = 0
    c.begin()
