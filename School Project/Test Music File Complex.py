#python -m pip install pygame comptypes pycaw
from pygame import mixer
import time
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
 
# Control volume
#vol = float(input("Enter Volume:"))
length = int(input("Enter the lenght of audio you want to play:"))
#netvol = vol - 100
volume.SetMasterVolumeLevel(-15.0, None)

path=os.path.dirname(__file__)
mixer.init()
mixer.music.load(rf"{path}\Music Files\MissionImpossibleTheme.mp3")
mixer.music.play()
time.sleep(length)
mixer.music.stop()