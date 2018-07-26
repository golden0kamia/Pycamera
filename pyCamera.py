from tkinter import *
from datetime import datetime
from time import sleep

try:
    from picamera import PiCamera
    import RPi.GPIO as GPIO
    camera = PiCamera(resolution = (1640, 1232), framerate = 30)
    camera.exposure_mode = 'night'

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print('check button are not pressed and connected')
    while GPIO.input(5) and GPIO.input(3):
        pass
    print('Start program')
except:
    print('error while setting up the raspberry')

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
        camera.iso = 0
    else:
        isoScale.config(state=NORMAL)
        camera.iso = isoScale.get()

def Destroy():
	print("Quit")
	camera.close()
	window.destroy
	GPIO.cleanup()
	quit()

window = Tk()
#window.attributes('-fullscreen', True)

sharpnessActivate = BooleanVar()
contrastActivate = BooleanVar()
brightnessActivate = BooleanVar()
saturationActivate = BooleanVar()
isoActivate = BooleanVar()


view = Frame(window, bg=backGround)
view.pack(fill=BOTH, expand=1)

sharpnessFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
sharpnessFrame.grid(row=1, column=1, columnspan=2)

sharpnessLabel = Label(sharpnessFrame, text="Sharpness", bg=backGround, fg=foreGround, padx=2)
sharpnessLabel.grid(row=1, column=1)

sharpnessScale = Scale(sharpnessFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=SharpnessCMD)
sharpnessScale.grid(row=1, column=2)
sharpnessScale.set(0)
sharpnessScale.config(state=DISABLED)

sharpnessCheck = Checkbutton(sharpnessFrame, bg=backGround, fg=foreGround, text="Auto", command=SharpnessCMD, variable=sharpnessActivate)
sharpnessCheck.grid(row=1, column=3)
sharpnessCheck.select()


contrastFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
contrastFrame.grid(row=2, column=1, columnspan=2)

contrastLabel = Label(contrastFrame, text="Contrast", bg=backGround, fg=foreGround, padx=6)
contrastLabel.grid(row=1, column=1)

contrastScale = Scale(contrastFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=ContrastCMD)
contrastScale.grid(row=1, column=2)
contrastScale.set(0)
contrastScale.config(state=DISABLED)

contrastCheck = Checkbutton(contrastFrame, bg=backGround, fg=foreGround, text="Auto", command=ContrastCMD, variable=contrastActivate)
contrastCheck.grid(row=1, column=3)
contrastCheck.select()


brightnessFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
brightnessFrame.grid(row=3, column=1, columnspan=2)

brightnessLabel = Label(brightnessFrame, text="Brightness", bg=backGround, fg=foreGround)
brightnessLabel.grid(row=1, column=1)

brightnessScale = Scale(brightnessFrame, length=300, from_=0, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=BrightnessCMD)
brightnessScale.grid(row=1, column=2)
brightnessScale.set(50)
brightnessScale.config(state=DISABLED)

brightnessCheck = Checkbutton(brightnessFrame, bg=backGround, fg=foreGround, text="Auto", command=BrightnessCMD, variable=brightnessActivate)
brightnessCheck.grid(row=1, column=3)
brightnessCheck.select()


saturationFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
saturationFrame.grid(row=4, column=1, columnspan=2)

saturationLabel = Label(saturationFrame, text="Saturation", bg=backGround, fg=foreGround, padx=1)
saturationLabel.grid(row=1, column=1)

saturationScale = Scale(saturationFrame, length=300, from_=-100, to=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=SaturationCMD)
saturationScale.grid(row=1, column=2)
saturationScale.set(0)
saturationScale.config(state=DISABLED)

saturationCheck = Checkbutton(saturationFrame, bg=backGround, fg=foreGround, text="Auto", command=SaturationCMD, variable=saturationActivate)
saturationCheck.grid(row=1, column=3)
saturationCheck.select()


isoFrame = Frame(view, bg=backGround, relief=SUNKEN, bd=2)
isoFrame.grid(row=5, column=1, columnspan=2)

isoLabel = Label(isoFrame, text="ISO", bg=backGround, fg=foreGround, padx=19)
isoLabel.grid(row=1, column=1)

isoScale = Scale(isoFrame, length=300, from_=100, to=800, resolution=100, bg=backGround, fg=foreGround, orient=HORIZONTAL, command=ISOCMD)
isoScale.grid(row=1, column=2)
isoScale.config(state=DISABLED)

isoCheck = Checkbutton(isoFrame, bg=backGround, fg=foreGround, text="Auto", command=ISOCMD, variable=isoActivate)
isoCheck.grid(row=1, column=3)
isoCheck.select()


openCamera = Button(view, text="Camera", bg=backGround, fg=foreGround, command=lambda:camera.start_preview(), bd=7)
openCamera.grid(row=6, column=1)

quitCamera = Button(view, text="Quit", bg=backGround, fg=foreGround, command=Destroy, bd=7)
quitCamera.grid(row=6, column=2)

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
                camera.start_recording("%s.mjpeg" %datetime.now().strftime('%Y-%m-%d_%H:%M:%S'), 'mjpeg')
                vFlag = True
            else:
                camera.capture("%s.png" %datetime.now().strftime('%Y.%m.%d_%H:%M:%S'), 'png')

    if GPIO.input(3):
        camera.quit_preview

