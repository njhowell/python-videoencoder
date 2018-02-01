from celery import Celery
import celeryconfig
import os.path
from subprocess import call

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def encode(srcFile, dstFolder):
    outFileName = dstFolder+os.path.splitext(os.path.basename(srcFile))[0]+".mp4"
    argsStr =  " -i \"%s\" -c:v libx264 -vf \"yadif\" -crf 25 -crf_max 35 -bufsize 2M -strict experimental -acodec aac -ar 48000 -ab 160k -y \"%s\" " % (srcFile, outFileName)
    result = call("ffmpeg" + argsStr, shell=True)
    return result
