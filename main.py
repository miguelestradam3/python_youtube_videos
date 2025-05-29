from youtube_module.youtube import YoutubeClass

if __name__ == "__main__":
    buff = YoutubeClass()
    buff.download_video(url="https://www.youtube.com/watch?v=SLcOFCpcJ-w", path="Pokemon")