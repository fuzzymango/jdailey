import nuke
import math
import time,re,subprocess
from backdropCreator import *

nuke.knobDefault('Merge.label', '[value mix]')
nuke.knobDefault('Merge.note_font', 'Bitstream Vera Sans Bold')
nuke.knobDefault('Merge.note_font_color', '16711935')


nuke.knobDefault('BackdropNode.note_font','Bitstream Vera Sans Bold')
nuke.knobDefault('BackdropNode.tile_color', '555819519')

nuke.knobDefault('Defocus.label', '[value defocus]')

nuke.knobDefault('Roto.cliptype', 'no clip')
nuke.knobDefault('Roto.replace', 'true')
nuke.knobDefault('Roto.note_font_color', '21010530')

nuke.knobDefault('RotoPaint.cliptype', 'no clip')
nuke.knobDefault('RotoPaint.note_font_color', '21010530')

#------custom node------#

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Jacob")
n = nuke.menu("Nodes").addMenu("Other/Aliased nodes")

m.addCommand("Killoutline", "nuke.createNode(\"KillOutline.nk\")")
m.addCommand("Flicker", "nuke.createNode(\"Flicker\")")

m.addCommand("STRamp", "nuke.createNode(\"STRamp.nk\")")
m.addCommand("CameraShake_FS", "nuke.createNode(\"CameraShake.nk\")")
m.addCommand("hueMix", "nuke.createNode(\"hueMix_v02.nk\")")
m.addCommand("multiLevel_lightwrap", "nuke.createNode(\"multiLevel_lightwrap.nk\")")
m.addCommand("Grain", "nuke.createNode(\"grain_v03.nk\")")
n.addCommand('Create Custom backdrop',"mdCreateBackdrop()",'Alt+b')

from myTracker import *

nuke.addOnCreate(customTracker, nodeClass="Tracker4")

