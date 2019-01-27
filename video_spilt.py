#encoding = utf-8
import subprocess
import os
'''
输入视频路径
起始时间
终止时间         
'''
#------------------需要修改的部分-------------
video_path = r"D:\seagate2\SNIS-556_FHD.mkv"#视频所在的目录
start_time = "00:00:00"
stop_time =  "03:57:25"
#---------------以上是可以修改的部分-----------

#分割出视频所在的目录完整名称，如 "c:/video"
root_dir = os.path.split(video_path)[0]

#创建split文件夹，存放截取出来的视频,如 "c:/video/split"
split_dir = os.path.join(root_dir,"split")
if not os.path.isdir(split_dir):
    os.makedirs(split_dir)

#获取视频文件短名字，包含前缀路径，不包含后缀名,如 "c:/video/star-998"
shortname = os.path.splitext(video_path)[0]

#获取视频文件后缀名，如 ".mp4"
houzhuiming = os.path.splitext(video_path)[-1]

#获取视频文件真正的名字，不包含前缀路径，不包含后缀名，如 "STAR-998"
filename = os.path.split(shortname)[-1]

#构建分割得到的视频完整名称
output_name = split_dir +"/"+ "" + houzhuiming

#判断是否有重名文件
while os.path.exists(os.path.join(split_dir,filename + houzhuiming)):
    filename = filename + "-1"

#构建最终输出的文件完整名
output_name = os.path.join(split_dir,filename + houzhuiming)


def spilt_video(video_path, start_time, stop_time,output_name):       
    subprocess.call(["ffmpeg", "-i", video_path, "-vcodec", "copy", "-acodec", "copy", "-ss", start_time, "-to", stop_time, output_name, "-y"])


if __name__ == "__main__":
    spilt_video(video_path, start_time, stop_time, output_name)