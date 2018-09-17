"""
python final image viewer
displays images and makes them disappear
author Nick
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
#imports

class ButtonImage(EasyFrame):
	def __init__(self):
		#set up window 
		EasyFrame.__init__(self, title = "Picture Viewer 1.0")
		self.setResizable(False)
		#title
		self.addLabel(text = "Image Viewer 1.0", row = 0, column = 1, columnspan = 3)
		#adds the buttons with commands that show and hide the images
		self.addButton(text = "click", row = 2, column = 0, command = self.show1)
		self.addButton(text = "click", row = 2, column = 1, command = self.show2)
		self.addButton(text = "click", row = 2, column = 2, command = self.show3)

	""" 
	3 show commands sets up the label for displaying their associated images
	change button to now command the hide command

	"""
	def show1(self):
		imageLabel1 = self.addLabel(text="", row = 1, column = 0, sticky = "NSEW")

		self.image1 = PhotoImage(file="image1.gif")
		imageLabel1["image"] = self.image1

		self.addButton(text = "click", row = 2, column = 0, command = self.hide1)
		
	def show2(self):
		imageLabel2 = self.addLabel(text="", row = 1, column = 1, sticky = "NSEW")
		
		self.image2 = PhotoImage(file="image2.gif")
		imageLabel2["image"] = self.image2

		self.addButton(text = "click", row = 2, column = 1, command = self.hide2)

	def show3(self):
		imageLabel3 = self.addLabel(text="", row = 1, column = 2, sticky = "NSEW")		

		self.image3 = PhotoImage(file="image3.gif")
		imageLabel3["image"] = self.image3

		self.addButton(text = "click", row = 2, column = 2, command = self.hide3)

"""
3 hide commands change the image file to blank, hiding the image
return the buttons to the original show commands to redisplay the images
"""

	def hide1(self):
		self.image1 = PhotoImage(file="")
		self.addButton(text = "click", row = 2, column = 0, command = self.show1)
	def hide2(self):
		self.image2 = PhotoImage(file="")
		self.addButton(text = "click", row = 2, column = 1, command = self.show2)
	def hide3(self):
		self.image3 = PhotoImage(file="")
		self.addButton(text = "click", row = 2, column = 2, command = self.show3)

#run the main 
def main():
	ButtonImage().mainloop()

main()