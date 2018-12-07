import FreeCADGui
import FreeCAD

import numpy

class CommandoDeMover:
	def Activated(self):
		selecao = [s for s in FreeCADGui.Selection.getSelectionEx() if s.Document == FreeCAD.ActiveDocument ]
		if len(selecao) == 1:
			MovedorDeParte( FreeCADGui.activeDocument().activeView(),  selecao[0].Object )

	def GetResources(self):
		return{
		'Pixmap' : '/home/dechog/.FreeCAD/Mod/MinhaWorkbench/icones/Mover.svg'
		}

FreeCADGui.addCommand( 'meuComando_moverToolbar', CommandoDeMover() )


class MovedorDeParte :
	def __init__(self, view, obj):
		self.obj = obj
		self.posicaoInicial = self.obj.Placement.Base
		self.view = view

		self.callbackMovimento  = self.view.addEventCallback("SoLocation2Event",  self.movimentoMouse)
		self.callbackClick 		= self.view.addEventCallback("SoMouseButtonEvent",self.clickMouse)

 	def removerCallbacks(self):
		self.view.removeEventCallback("SoLocation2Event",  self.callbackMovimento)
		self.view.removeEventCallback("SoMouseButtonEvent",self.callbackClick)

	def movimentoMouse(self, info):
			novaPosicao = self.view.getPoint( *info['Position'] )
			self.obj.Placement.Base = novaPosicao


	def clickMouse(self, info):
		if info['Button'] == 'BUTTON1':
			self.removerCallbacks()