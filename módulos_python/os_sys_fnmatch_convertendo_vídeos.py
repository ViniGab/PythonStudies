# https://ffmpeg.zeranoe.com/builds/

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt - map v:0 -map a 1:0 -ss "SAIDA"
"""

import os
import fnmatch
import sys

if sys.plataform == "Windows":
    comando_ffmpeg = 'ffmpeg'