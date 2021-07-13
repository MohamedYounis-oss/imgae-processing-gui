from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Image processing")
root.geometry("800x650")


# Program author name
headtitle = Label(root, text="Image processing proagramming assignment", padx=10, pady=10)
headtitle.place(x=1, y=1)

# -------------------------------------------------------------------------------------------------
# Load Image frame
loadImage = LabelFrame(root, text="Load image", width=170, height=90, padx=15, pady=23)
loadImage.place(x=10, y=35)

openButt = Button(loadImage, text="open", padx=50)
openButt.pack()

# -------------------------------------------------------------------------------------------------
# convert frame
convert = LabelFrame(root, text="Convert", width=170, height=90, padx=28, pady=12)
convert.place(x=185, y=35)

c = IntVar()
c.set(0)

Radiobutton(convert, text="Default colour", variable=c, value=1).pack()
Radiobutton(convert, text="gray", variable=c, value=2).pack()

# -------------------------------------------------------------------------------------------------
# Add noise frame
addNoise = LabelFrame(root, text="Add noise", width=170, height=90, padx=15)
addNoise.place(x=360, y=35)

an = IntVar()
an.set(0)

Radiobutton(addNoise, text="Salt & pepper noise", variable=an, value=1).pack()
Radiobutton(addNoise, text="Gaussian noise", variable=an, value=2).pack()
Radiobutton(addNoise, text="Poisson noise", variable=an, value=3).pack()

# -------------------------------------------------------------------------------------------------
# Original image frame
originalImage = LabelFrame(root, text="Original image", width=240, height=200)
originalImage.place(x=535, y=35)


#-----------------------------------------------------------------------------------------------
# Point transform Op's
pointTransform = LabelFrame(root, text="Point transform Op's", width=515, height=105)
pointTransform.place(x=10, y=130)

brightnessAdjustButt = Button(pointTransform, text="Brightness djustment", padx=30)
brightnessAdjustButt.place(x=20, y=10)

contrastAdjustButt = Button(pointTransform, text="Contrast adjustment ", padx=30)
contrastAdjustButt.place(x=250, y=10)

histogramButt = Button(pointTransform, text="         Histogram         ", padx=30)
histogramButt.place(x=250, y=50)

histogramEqualButt = Button(pointTransform, text="Histogram equalization", padx=25)
histogramEqualButt.place(x=20, y=50)

# ----------------------------------------------------------------------------------------------
# Local Transform Op's

localTransform = LabelFrame(root, text="Local transform Op's", width=515, height=200)
localTransform.place(x=10, y=235)

# edgedetfltr = LabelFrame(localTransform, text="Edge detection filters", width = 400, height = 288)
# edgedetfltr.place(x= 60 , y=340)


lowpassButt = Button(localTransform, text="Low pass filter    ", padx=50)
lowpassButt.place(x=10, y=20)

highpassButt = Button(localTransform, text="High pass filter   ", padx=50)
highpassButt.place(x=10, y=60)

medianFltrButt = Button(localTransform, text="Median filtering ", padx=50)
medianFltrButt.place(x=10, y=100)

avrgFltrButt = Button(localTransform, text="Avareging feltering", padx=44)
avrgFltrButt.place(x=10, y=140)

k = IntVar()
k.set(0)

Radiobutton(localTransform, text="Laplacian filter", variable=k, value=1).place(x=300, y=20)
Radiobutton(localTransform, text="Gaussian filter", variable=k, value=2).place(x=300, y=60)
Radiobutton(localTransform, text="Vert Prewitt", variable=k, value=3).place(x=300, y=100)
Radiobutton(localTransform, text="Horiz Prewitt", variable=k, value=4).place(x=300, y=140)

# ----------------------------------------------------------------------------------------------
# After noising adding

afternoiseImage = LabelFrame(root, text="After noising adding", width=240, height=200)
afternoiseImage.place(x=535, y=235)

# ----------------------------------------------------------------------------------------------
# Global Transform Op's

globalTransform = LabelFrame(root, text="Global transform Op's", width=250, height=150)
globalTransform.place(x=10, y=435)

lineDetectionUsingButt = Button(globalTransform, text="Line detection using Hough Transform    ")
lineDetectionUsingButt.place(x=10, y=20)

circlesDetectionButt = Button(globalTransform, text="Circles detection using Hough Transform")
circlesDetectionButt.place(x=10, y=70)

# Morphological
morphological = LabelFrame(root, text="Morphological Op's", width=250, height=150)
morphological.place(x=275, y=435)

dilationButt = Button(morphological, text="Dilation")
dilationButt.place(x=10, y=5)

erosionButt = Button(morphological, text="Erosion ")
erosionButt.place(x=10, y=35)

closeButt = Button(morphological, text=" Close   ")
closeButt.place(x=10, y=65)

opennButt = Button(morphological, text="  Open  ")
opennButt.place(x=10, y=95)

label1 = Label(morphological, text="Choose type of kernel")
label1.place(x=90, y=25)

var = StringVar()
var.set("arbitary")

drop = OptionMenu(morphological, var, "arbitary", "rectangle", "periodicline")
drop.place(x= 105, y=45)

saveButt = Button(root, text="Save result imgae")
saveButt.place(x=100, y=600)

exitButt = Button(root, text="Exit", padx=50)
exitButt.place(x=300, y=600)

#--------------------------------------------------------------------------------------
# Result image
resultImage = LabelFrame(root, text="Result image", width=240, height=200)
resultImage.place(x=535, y=435)



root.mainloop()
