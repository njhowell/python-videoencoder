# python-videoencoder
A Python Celery application for queuing and processing video encoding jobs

## Overview

`queueFiles.py` will scan a directory defined in `dirConfig.py` and move/queue all video files ready for processing. The destination directories are also defined in `dirConfig.py`.

`videoTasks.py` defines the encode task. This takes a source file (including full path) and a destination directory to output the encoded file to. It uses ffmpeg, and creates a mp4 h264 file according to the settings in the file. 


## Making it go

Check out this repo to a system with python3. You'll need a RabbitMQ instance somewhere, and whichever machine runs the workers will need access to ffmpeg. 

Configure the RabbitMQ settings in `celeryconfig.py`.

One machine needs to run `queueFiles.py` to process and queue videos in a given directory. 

Start a celery worker either on the same machine, or on 1 or more other machines. You'll need celery installed using `pip install celery`.

If more than one machine is used, then there must be shared storage between them, e.g by using NFS, and the video folders mounted to identical paths.

Start a worker like so:
```
cd /path/to/git/checkout
celery worker -A videoTasks -l info -Ofair
```

The `-l` and `-O` arguments are optional, change them if you like.

The worker process should pick up any messages in the queue and begin processing.
