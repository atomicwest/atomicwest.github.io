#from http://kevman3d.blogspot.co.nz/2015/04/python-snippets-maya-for-budding-td.html

#use internalVar for queries in the workstation configurations/workstations

import maya.cmds as cmds

# return root documents-maya folder
print cmds.internalVar(userAppDir=True)

# return scripts folder
print cmds.internalVar(userScriptDir=True)

# return preferences folder
print cmds.internalVar(userPrefDir=True)

# return prefs-icons folder
print cmds.internalVar(userBitmapsDir=True)

"""
run scripts at startup by placing them all in userSetup.py
put userSetup in the wokstations scripts folder
adding "import maya.cmds" (or any other modules) as cmds in userSetup.py 
adds these commands at startup
"""

# access and setup workspaces
import maya.cmds as cmds

#get root folder of maya projects
print cmds.internalVar(userWorkspaceDir=True)

#get a list of the workspaces/projects
listWS = cmds.workspace(listWorkspaces = True)
for wsp in listWS:
  print wsp

# change Maya to use a workspace if it exists
#use a try/except catch
try:
  cmds.workspace('WorkspaceName', openWorkspace=True)
except:
  raise Exception("Project WorkspaceName doesn't exist!")

#retrieve root location of current project setup in Maya
workspaceFolder = cmds.workspace( q=True, rd=True)

#write log files for a project 
logPath = cmds.workspace ( q=True, rd=True ) + 'data'

#set up frame rates and resolutions for projects
#insert this into the userSetup.py file for automatic loading
cmds.currentUnit( linear='m' ) #sets the units to meters
cmds.currentUnit( time='film') #sets the frame rate to 24fps

#set render resolution to 720p
cmds.setAttr( 'defaultResolution.width', 1280 )
cmds.setAttr( 'defaultResolution.width', 720 )

#enable autosave every 300 seconds/5minutes
cmds.autoSave( int=300, dst=0, prm=False, en=True, lim=True, max=10 )
