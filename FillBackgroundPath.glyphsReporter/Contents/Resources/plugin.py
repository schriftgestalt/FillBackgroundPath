# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class FillBackgroundPath(ReporterPlugin):
	def settings(self):

		# The name as it will appear in Glyphs’s View menu
		self.menuName = 'Fill Background Path'

	def background(self, layer):

		# Fills background path of current glyph with non-photo blue
		NSColor.colorWithRed_green_blue_alpha_(.643, .867, .929, .3).set()
		if layer.background.bezierPath:
			layer.background.bezierPath.fill()
		# Fills background path of current component glyph with vermillion
		NSColor.colorWithRed_green_blue_alpha_(.89, .259, .204, .3).set()
		for backgroundComponent in layer.background.components:
			backgroundComponent.bezierPath.fill()
