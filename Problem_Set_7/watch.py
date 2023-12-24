import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # output should always have https://youtu.be/ even if the input doesn't
    # if input doesn't contain a youtube link, output should be "None"
    if re.search(r"^<iframe(.)*><\/iframe>$", s) and (video_id_pattern := re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed\/([0-9A-Za-z_-]+)", s)):
        video_id = video_id_pattern.group(1)
        return "https://youtu.be/" + video_id
    elif re.search(r"^src=\"$", s) and (video_id_pattern := re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed\/([0-9A-Za-z_-]+)", s)):
        video_id = video_id_pattern.group(1)
        return "https://youtu.be/" + video_id
    else:
        return "None"

if __name__ == "__main__":
    main()
