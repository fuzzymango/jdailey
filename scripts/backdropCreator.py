import nuke
def nodeX(node):
	return node['xpos'].value()
	
def nodeY(node):
	return node['ypos'].value() 

	

def mdCreateBackdrop():
	nodes = nuke.selectedNodes()
	if nodes == None:
		return	
	
	#-----------	
	nodes.sort(key=nodeX)
	minX = nodes[0]['xpos'].value()
	#-----------
	nodes.sort(key=nodeY)
	minY = nodes[0]['ypos'].value()
	#-----------
	nodes.sort(key=nodeX, reverse=True)
	maxX = nodes[0]['xpos'].value()
	#-----------
	nodes.sort(key=nodeY, reverse=True)
	maxY = nodes[0]['ypos'].value()
	#-----------

	pad       = 250
	bgColor   = 640034559
	textColor = 1401472511
	textSize  = 45
			
	#xpos      = int((maxX+minX)/2)
	#ypos      = int((maxY+minY)/2)
	xpos = int(minX-(pad/2))
	ypos = int(minY-(pad/2))
	bdwidth   = maxX-minX
	bdheight  = maxY-minY

	
	bd = nuke.createNode("BackdropNode")
	bd.setXYpos(xpos,ypos)
	bd['bdwidth'].setValue(bdwidth+(pad*1.5))
	bd['bdheight'].setValue(bdheight+pad)
	bd['note_font_color'].setValue(textColor)
	bd['note_font_size'].setValue(textSize)
	bd['tile_color'].setValue(bgColor)

	
	return
	

		
		
