#from http://kevman3d.blogspot.com/2015/05/introduction-to-simple-maya-ui-coding.html

import maya.cmds as cmds

#UIs work as hierarchies

#function for query a field ID and execute procedure
#e.g. query text field and print to the script editor
def printTextField(fieldID):
  print cmds.textField( fieldID, query=True, text=True)
  

#declare window id string
windowID = 'Example UI'

#ensure UI isn't active already
if cmds.window(windowID, exists=True):
  cmds.deleteUI(windowID)

#create UI window
cmds.window(winID)

#add layout
cmds.columnLayout()

#create a variable to store reference to the textfield control
#this does not store the value entered into the field
txtcontrol = cmds.textField()

#button linking to command
cmds.button(label='Print to Script Editor', command='printTextField'(txtcontrol)')

#display UI window
cmds.showWindow()
