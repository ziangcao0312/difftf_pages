import os
import ipdb
import re
import shutil
import numpy as np
import imageio
from moviepy.editor import VideoFileClip

path='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\car'
su=0
newpath='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\car_gif'
os.makedirs(os.path.join(newpath), exist_ok=True)
for classes in os.listdir(path):
    videoClip = VideoFileClip(os.path.join(path,classes))
    videoClip.write_gif(os.path.join(newpath,classes.split('.')[0]+'.gif'))

path='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\plane'
su=0
newpath='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\plane_gif'
os.makedirs(os.path.join(newpath), exist_ok=True)
for classes in os.listdir(path):
    videoClip = VideoFileClip(os.path.join(path,classes))
    videoClip.write_gif(os.path.join(newpath,classes.split('.')[0]+'.gif'))


path='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\chair'
su=0
newpath='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\chair_gif'
os.makedirs(os.path.join(newpath), exist_ok=True)
for classes in os.listdir(path):
    videoClip = VideoFileClip(os.path.join(path,classes))
    videoClip.write_gif(os.path.join(newpath,classes.split('.')[0]+'.gif'))    


path='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\omni'
su=0
newpath='F:\\Game\\NTU\\1_project\\diffrf\\difftf\\static\\videos\\omni_gif'
os.makedirs(os.path.join(newpath), exist_ok=True)
for classes in os.listdir(path):
    videoClip = VideoFileClip(os.path.join(path,classes))
    videoClip.write_gif(os.path.join(newpath,classes.split('.')[0]+'.gif'))         
    #ipdb.set_trace()
    #imageio.mimwrite(os.path.join(newpath, classes+'video.gif'), np.stack(rgbss), duration=300,loop=0)