from celery import Celery
import celeryconfig
import os.path
from subprocess import call

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def encode(srcFile, dstFolder):
    outFileName = dstFolder+os.path.splitext(os.path.basename(srcFile))[0]+".mp4"
    argsStr =  " -i \"%s\" -map 0 -c copy -c:v libx264 -crf 20 -y \"%s\" " % (srcFile, outFileName)
    result = call("ffmpeg" + argsStr, shell=True)
    return result