#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import time
from PIL import Image
from StringIO import StringIO
import os

import win32gui
import win32con
import win32api


def FetchPicFromBing(ImagePath):
    # 获取Bing首页图片的真实地址
    r = requests.get('http://cn.bing.com/')
    r = requests.get(r.text.split("g_img={url:'")[1].split("'")[0])

    # 将图片保存为bmp格式
    img = Image.open(StringIO(r.content))
    img.save(ImagePath)


def SetWallpaperFromBMP(ImagePath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, ImagePath, 1+2)

if __name__ == "__main__":
    ImagePath = "C:\\" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".bmp"
    FetchPicFromBing(ImagePath)
    SetWallpaperFromBMP(ImagePath)
