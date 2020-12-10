import os, subprocess

def print_files_indir():
    # Simple function to print the videos in the current dir
    files = sorted(os.listdir())
    count = 0
    videos = []

    for file in files:
        if file.endswith('.mp4') or file.endswith('.webm'):
            print("{} - {}".format(count,file))
            videos.append(file)
            count += 1
    return count, videos

def resize_and_transcode():
    vid = []
    while not vid:
        count, videos = print_files_indir()
        idx = int(input("Choose video number {} \n".format(len(collage_vids) + 1)))
        if idx not in range(count):
            print("BAD INPUT!")
            continue
        vid.append(videos[idx])

    sizes = ["1280x720", "720x480", "360x240", "160x120"]
    idx = int(input("\nWhich resize do you want to apply?\n 1: 720p\n 2: 480p\n 3: 360x240\n 4: 160x120 \n")) - 1

    out_webm = sizes[idx] + "_" + filename.split('.')[0] + ".webm"
    out_mp4 = sizes[idx] + "_" + filename.split('.')[0] + ".mp4"

    os.system("ffmpeg -i {} -c:v libvpx -c:a libvorbis -vf scale={},setsar=1:1 {}".format(vid[0], sizes[idx], "vp8_" + out_webm ))
    os.system("ffmpeg -i {} -c:v libvpx-vp9 -c:a libvorbis -vf scale={},setsar=1:1 {}".format(vid[0], sizes[idx], "vp9_" + out_webm))
    os.system("ffmpeg -i {} -c:v libx265 -vf scale={},setsar=1:1 {}".format(vid[0], sizes[idx], "h265_" + out_mp4))
    os.system("ffmpeg -i {} -c:v libaom-av1 -vf scale={},setsar=1:1 {}".format(vid[0], sizes[idx], "av1_" + out_mp4))




def collage_2x2():
    collage_vids = []
    while len(collage_vids) < 4:
        count, videos = print_files_indir()
        idx = int(input("Choose video number {} \n".format(len(collage_vids) + 1)))
        if idx not in range(count):
            print("BAD INPUT!")
            continue
        collage_vids.append(videos[idx])

    os.system('ffmpeg -i {} -i {} -i {} -i {} -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" 2x2_collage.mp4'.format(collage_vids[0],collage_vids[1],collage_vids[2],collage_vids[3]))

def stream(input, port):
        os.system("ffmpeg -re -i {} -v 0 -vcodec mpeg4 -acodec copy -b:v 64k -f mpegts udp://127.0.0.1:{}".format(input, port))
