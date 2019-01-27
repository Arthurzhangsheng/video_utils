#encoding = utf-8
import subprocess
import os
'''
文件目录结构如下所示
├── test
   └── video.mp4          
'''
#------------------需要修改的部分-------------
root_dir = r"D:\seagate2\JP\DVAJ-242\split"#视频所在的目录
rate = 25 #裁剪帧率,不建议修改,因为合成时默认采用25帧的合成频率
frame_format = "jpg" #jpg体积小且设置jpg质量参数后（默认2），看不出有损压缩； png无损但体积大
extract_sound = True #是否提取音频
#---------------以上是可以修改的部分-----------

pic_out_dir = root_dir + "/" +"frames"
if not os.path.isdir(pic_out_dir):
    os.makedirs(pic_out_dir)

format_list = [".mp4", ".avi", ".mkv", ".flv"]#其他视频格式应该也可以,需要的话加进列表中即可
file_list = []

def getfile(root_dir):
    if os.path.isdir(root_dir):
        for fpathe, dirs, files in os.walk(root_dir):
            for _file in files:
                if os.path.splitext(_file)[-1].lower() in format_list:
                    shortname = os.path.splitext(_file)[0]
                    video_path = os.path.join(fpathe, _file)

                    print("正在处理{}".format(_file))               
                    subprocess.call(["ffmpeg", '-i', video_path, "-r", str(rate), "-f", "image2","-y", "-qscale:v","2",pic_out_dir+'/'+shortname+'-%05d.'+frame_format])
                    print("处理{}完成".format(_file))
                    
                    if extract_sound:
                        print("正在提取视频{}的音频".format(_file))
                        subprocess.call(["ffmpeg", '-i', video_path, "-vn", "-acodec", "copy","-y", root_dir+'/'+shortname+".aac"])
                        print("视频{}提取音频完成".format(_file))
                    file_list.append(_file)
        
        print("共处理了{}个视频".format(str(len(file_list))))
    else:
        print("路径不对,请确认路径的是不是写错了")


if __name__ == "__main__":
    getfile(root_dir)
