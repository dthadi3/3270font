#!/usr/bin/env python3
# -*- coding:utf-8 -*-

boxes = """
┌─┬┐╔═╦╗╓─╥╖╒═╤╕
├─┼┤╠═╬╣╟─╫╢╞═╪╡
│ ││║ ║║║ ║║│ ││
└─┴┘╚═╩╝╙─╨╜╘═╧╛
"""

misc_glyphs = """
Other miscellaneous glyphs: ™●⌘⏎⬇⬆✔✼✎✘‘’◢◣◤◥▮◆
"""

apl_set = """
The APL set: ⌶⌷⌸⌹⌺⌻⌼⌽⌾⌿⍀⍁⍂⍃⍄⍅⍆⍇⍈⍉⍊⍋⍌⍍⍎⍏⍐⍑⍒⍓⍔⍕⍖⍗⍘⍙⍚⍛⍜⍝⍞⍟⍠⍡⍢⍣⍤⍥⍦⍧⍨⍩⍪⍫⍬⍭⍮⍯⍰⍱⍲⍳⍴⍵⍶⍷
⍸⍹⍺
"""

if __name__ == '__main__':
    print(boxes)
    print(misc_glyphs)
    print(apl_set)
    print("\x1b[1mBOLD\x1b[0m \x1b[3mITALIC\x1b[0m NORMAL")
