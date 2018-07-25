from tkinter import *
from picamera import PiCamera
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep

camera = PiCamera()
camera.resolution = (1640, 1232)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while GPIO.input(5):
    pass

sharpnessString = ""
contrastString = ""
brightnessString = ""
saturationString = ""
isoString = ""
backGround = "black"
foreGround = "red"
vFlag = False

    
def SharpnessCMD(value = 0):
    global sharpnessString
    if sharpnessActivate.get():
        sharpnessScale.config(state=DISABLED)
        camera.sharpness = 0
    else:
        sharpnessScale.config(state=NORMAL)
        camera.sharpness = sharpnessScale.get()

def ContrastCMD(value = 0):
    global contrastString
    if contrastActivate.get():
        contrastScale.config(state=DISABLED)
        camera.contrast = 0
    else:
        contrastScale.config(state=NORMAL)
        camera.contrast = contrastScale.get()

def BrightnessCMD(value = 0):
    global brightnessString
    if brightnessActivate.get():
        brightnessScale.config(state=DISABLED)
        camera.brightness = 50
    else:
        brightnessScale.config(state=NORMAL)
        camera.brightness = brightnessScale.get()

def SaturationCMD(value = 0):
    global saturationString
    if saturationActivate.get():
        saturationScale.config(state=DISABLED)
        camera.saturation = 0
    else:
        saturationScale.config(state=NORMAL)
        camera.saturation = saturationScale.get()
        
def ISOCMD(value = 0):
    global isoString
    if isoActivate.get():
        isoScale.config(state=DISABLED)
        camera.iso = 200
    else:
        isoScale.config(state=NORMAL)
        camera.iso = isoScale.get()

def Destroy():
	print("Quit")
	window.destroy
	GPIO.cleanup()
	quit()

window = Tk()

sharpnessActivate = BooleanVar()
contrastActivate = BooleanVar()
brightnessActivate = BooleanVar()
saturationActivate = BooleanVar()
isoActivate = BooleanVar()


view = Frame(window, bg=backGround)
view.pack(fill=BOTH, expand=1)

sharpnessFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
sharpnessFrame.pack(fill=X, expand=1)

sharpnessLabel = Label(sharpnessFrame, text="Sharpness", bg=backGround, fg=foreGround, padx=2)
sharpnessLabel.pack(side=LEFT)

sharpnessCheck = Checkbutton(sharpnessFrame, bg=backGround, fg=foreGround, text="Auto", command=SharpnessCMD, variable=sharpnessActivate)
sharpnessCheck.pack(side=RIGHT)
sharpnessCheck.select()

sharpnessScale = Scale(sharpnessFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=SharpnessCMD)
sharpnessScale.pack(side=RIGHT, fill=X, expand=1)
sharpnessScale.set(0)
sharpnessScale.config(state=DISABLED)


contrastFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
contrastFrame.pack(fill=X, expand=1)

contrastLabel = Label(contrastFrame, text="Contrast", bg=backGround, fg=foreGround, padx=6)
contrastLabel.pack(side=LEFT)

contrastCheck = Checkbutton(contrastFrame, bg=backGround, fg=foreGround, text="Auto", command=ContrastCMD, variable=contrastActivate)
contrastCheck.pack(side=RIGHT)
contrastCheck.select()

contrastScale = Scale(contrastFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=ContrastCMD)
contrastScale.pack(side=RIGHT, fill=X, expand=1)
contrastScale.set(0)
contrastScale.config(state=DISABLED)


brightnessFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
brightnessFrame.pack(fill=X, expand=1)

brightnessLabel = Label(brightnessFrame, text="Brightness", bg=backGround, fg=foreGround)
brightnessLabel.pack(side=LEFT)

brightnessCheck = Checkbutton(brightnessFrame, bg=backGround, fg=foreGround, text="Auto", command=BrightnessCMD, variable=brightnessActivate)
brightnessCheck.pack(side=RIGHT)
brightnessCheck.select()

brightnessScale = Scale(brightnessFrame, length=300, from_=0, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=BrightnessCMD)
brightnessScale.pack(side=RIGHT, fill=X, expand=1)
brightnessScale.set(50)
brightnessScale.config(state=DISABLED)


saturationFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
saturationFrame.pack(fill=X, expand=1)

saturationLabel = Label(saturationFrame, text="Saturation", bg=backGround, fg=foreGround, padx=1)
saturationLabel.pack(side=LEFT)

saturationCheck = Checkbutton(saturationFrame, bg=backGround, fg=foreGround, text="Auto", command=SaturationCMD, variable=saturationActivate)
saturationCheck.pack(side=RIGHT)
saturationCheck.select()

saturationScale = Scale(saturationFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=SaturationCMD)
saturationScale.pack(side=RIGHT, fill=X, expand=1)
saturationScale.set(0)
saturationScale.config(state=DISABLED)


isoFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
isoFrame.pack(fill=X, expand=1)

isoLabel = Label(isoFrame, text="ISO", bg=backGround, fg=foreGround, padx=19)
isoLabel.pack(side=LEFT)

isoCheck = Checkbutton(isoFrame, bg=backGround, fg=foreGround, text="Auto", command=ISOCMD, variable=isoActivate)
isoCheck.pack(side=RIGHT)
isoCheck.select()

isoScale = Scale(isoFrame, length=300, from_=100, to=800, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=ISOCMD)
isoScale.pack(side=RIGHT, fill=X, expand=1)
isoScale.config(state=DISABLED)


openCamera = Button(view, text="Camera", bg=backGround, fg=foreGround, command=camera.start_preview(), bd=7)
openCamera.pack(fill=X, expand=1, side=LEFT)

quitCamera = Button(view, text="Quit", bg=backGround, fg=foreGround, command=Destroy, bd=7)
quitCamera.pack(fill=X, expand=1, side=RIGHT)

window.mainloop()

while True:
    if GPIO.input(5):
        if vFlag:
            cmera.stop_recording()
            vFlag = False
        else:
            sd = 0
            while GPIO.input(5):
                sleep(100)
                sd = sd+1
                if sd >= 15:
                    break
            if sd >= 15:
                camera.start_recording("%s.jpg" %datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
                vFlag = True
            else:
                camera.capture("%s.jpg" %datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))

    if not GPIO.input(3):
        camera.quit_preview

