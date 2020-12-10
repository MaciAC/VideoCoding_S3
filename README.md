# VideoCoding_S3
##Seminar 3 of Video Coding subject in UPF

**Task 1:** Resize as first seminar and transcode to VP8, VP9, h265 & AV1.

**Task 2:** Create a 2x2 collage with the 4 videos differently encoded.

**Task 3:** Stream to a local IP and play in VLC.

**Task 4:** Activate the stream with a python file.

### Requirements
	ffmpeg, Python3

### Executing
Run "python3 -i Stream.py" in the same folder that the video you want to resize/transcode. The execution will wait for you to enter commands.

Task 1. While Stream.py is interactively executing run:

```python
resize_and_transcode()
```

Task 2. While Stream.py is interactively executing run:

```python
collage_2x2()
```

Task 3 & 4. While Stream.py is interactively executing run:

```python
stream("filename", "port")
```

Where filename is the video you want to stream and port the one you want to use.

Then, in a new terminal run:

```
vlc udp://@:port
```

Where port is the one you used in the previous command.

WARNING: If you are in a mac vlc probably will not be correctly executed. Run this before the previous command:

```
alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'
```
