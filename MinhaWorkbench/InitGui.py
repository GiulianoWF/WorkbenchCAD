import meuMenu
import FreeCAD
import FreeCADGui


class MinhaWorkbech (Workbench):
	MenuText = 'Minha Workbech'

	def Initialize(self):
		commandslist = [
			'meuComando_moverToolbar' #definido em moverToolbar.py
			]
		self.appendToolbar('Minha Toolbar', commandslist)

	def Activated(self):
		return

	def ContextMenu(self, recipient):
		self.appendContextMenu( "Minha opcao de menu", 	[ 'meuComando_moverToolbar'] )

FreeCADGui.addWorkbench( MinhaWorkbech )