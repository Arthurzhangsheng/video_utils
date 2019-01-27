import subprocess
import os
'''
文件目录结构如下所示
├── test
   ├── frames
   ├── labmerge
   ├── video.mp4
   └── video.aac          
'''
#------------------需要修改的部分-------------
frames_dir = r"D:\seagate2\JP\DVAJ-242\split\frames"
merge_rate = 25 #合成速率,请与裁剪速度相匹配
#---------------以上是可以修改的部分-----------

vid_dir = os.path.split(frames_dir)[0] #去掉frames一级
merge_dir = os.path.join(vid_dir,"labmerge")#labmerge文件夹和frames并列

#获取视频名字(不包含路径和名字)
def get_short_name(vid_dir):
    format_list = [".mp4", ".avi", ".mkv", ".flv"]
    for file_ in os.listdir(vid_dir):
        if os.path.splitext(file_)[-1].lower() in format_list:
            shortname = os.path.splitext(file_)[0]
            break
    return shortname
#获取截图的后缀名
def get_frame_format(frames_dir):
    for file_ in os.listdir(frames_dir):
        if os.path.splitext(file_)[-1].lower() in [".jpg", ".png"]:
            frame_format = os.path.splitext(file_)[-1].lower() #.jpg 或.png
            break
    return frame_format

shortname = get_short_name(vid_dir) #获取短文件名
frame_format = get_frame_format(frames_dir)#获取截图格式.jpg或.png
frame_name = shortname+ "-%05d" + frame_format #构建merge图名称
frame_full_name = os.path.join(merge_dir,frame_name)#构建merge图完整路径名称

#散图合成
temp_out = os.path.join(merge_dir,"out.mp4")
subprocess.call(["ffmpeg", "-r", str(merge_rate), '-i',frame_full_name, "-y","-c:v", "libx264", "-vf", "fps=25,format=yuv420p",temp_out])

#声音合成
sound_dir = os.path.join(vid_dir,shortname+".aac")
#判断是否有重名文件
while os.path.exists(os.path.join(merge_dir,shortname+"out.mp4")):
    shortname = shortname + "_1"
final_vid_name = os.path.join(merge_dir,shortname+"out.mp4")
subprocess.call(["ffmpeg", "-i", temp_out, "-i", sound_dir, "-vcodec", "copy", "-acodec", "copy","-y", final_vid_name])

print("视频合成处理完毕")