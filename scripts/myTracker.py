#------Custom Tracker------#
import nuke
import math

def customTracker():
    trackNode= nuke.knobDefault('Tracker.label', '[value name]')


    code = '''
allTranforms = nuke.allNodes("Transform", recurseGroups=True)
allCornerPin = nuke.allNodes("CornerPin2D", recurseGroups=True)
refFrame = int(nuke.thisNode()['reference_frame'].value())
trackerName = nuke.thisNode().name()

##--Here is the original script in a default tracker node--##
tracker = nuke.thisNode()
cornerPinOption = tracker.knob("cornerPinOptions").getValue()
if cornerPinOption == 0:
    tracker.knob("createPinUseCurrentFrame").execute()
elif cornerPinOption == 1:
    tracker.knob("createPinUseReferenceFrame").execute()
elif cornerPinOption == 2:
    tracker.knob("createPinUseCurrentFrameBaked").execute()
elif cornerPinOption == 3:
    tracker.knob("createPinUseReferenceFrameBaked").execute()
elif cornerPinOption == 4:
    tracker.knob("createTransformStabilize").execute()
elif cornerPinOption == 5:
    tracker.knob("createTransformMatchMove").execute()
elif cornerPinOption == 6:
    tracker.knob("createTransformStabilizeBaked").execute()
elif cornerPinOption == 7:
    tracker.knob("createTransformMatchMoveBaked").execute()
##---------------------------------------------------------##


try:
    [node for node in nuke.allNodes("Transform", recurseGroups=True) if node not in allTranforms][0].knob("label").setValue("<html><center>From: " + trackerName + "\\nFrame: " + "%s</center></html>"%refFrame)
    [node for node in nuke.allNodes("Transform", recurseGroups=True) if node not in allTranforms][0].knob("shutteroffset").setValue("centred")
    
except:
    [node for node in nuke.allNodes("CornerPin2D", recurseGroups=True) if node not in allCornerPin][0].knob("label").setValue("<html><center>From: " + trackerName + "\\nFrame: " + "%s</center></html>"%refFrame)
    [node for node in nuke.allNodes("CornerPin2D", recurseGroups=True) if node not in allCornerPin][0].knob("shutteroffset").setValue("centred")
    '''

    nuke.thisNode().knob('createCornerPin').setValue(code)


nuke.addOnUserCreate(customTracker, nodeClass="Tracker4")
