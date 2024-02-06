#python -m pip install playsound==1.2.2
from playsound import playsound
import os

path=os.path.dirname(__file__)
playsound(rf"{path}\Music Files\James Bond (Original).mp3")

