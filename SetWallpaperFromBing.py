#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import time
import Image
import os
import win32gui,win32con,win32api

def FetchPicFormBing(ImagePath):
    # 获取Bing首页图片的真实地址
    r = requests.get('http://cn.bing.com/')
    r = requests.get(r.text.split("g_img={url:'")[1].split("'")[0])

    # 输入图片的类型(gep、bmp、gif)
    #print r.headers['content-type']

    # 保存图片到本地(直接以jpg为后缀，这个对图片格式没有影响)
    f = open("C:\\temp.jpg", "wb")
    f.write(r.content)
    f.close()

    # 将图片变为bmp格式
    img = Image.open("C:\\temp.jpg")
    img.save(ImagePath)
    os.remove("C:\\temp.jpg")


def SetWallpaperFromBMP(ImagePath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,ImagePath, 1+2)

if __name__ == "__main__":
    ImagePath = "C:\\"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+".bmp"
    FetchPicFormBing(ImagePath)
    SetWallpaperFromBMP(ImagePath)
