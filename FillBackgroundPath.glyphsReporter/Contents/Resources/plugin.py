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

from __future__ import division, print_function, unicode_literals
import objc
from AppKit import NSColor
from GlyphsApp import GSControlLayer
from GlyphsApp.plugins import *

class FillBackgroundPath(ReporterPlugin):

	@objc.python_method
	def settings(self):

		# The name as it will appear in Glyphs’s View menu
		self.menuName = 'Fill Background Path'

	@objc.python_method
	def background(self, layer):
		if isinstance(layer, GSControlLayer):
			return
		# Fills background path of current glyph with non-photo blue
		NSColor.colorWithRed_green_blue_alpha_(.643, .867, .929, .3).set()
		if layer.background.bezierPath:
			layer.background.bezierPath.fill()
		# Fills background path of current component glyph with vermillion
		NSColor.colorWithRed_green_blue_alpha_(.89, .259, .204, .3).set()
		for backgroundComponent in layer.background.components:
			backgroundComponent.bezierPath.fill()
