#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quickshot: 一键截屏进剪贴板 (Windows)
  F9  = 全屏截图  -> 剪贴板 + 存档
  F10 = 当前活动窗口截图 -> 剪贴板 + 存档
存档目录: C:\\Users\\Administrator\\screenshots\\ (时间戳命名, latest.png 恒为最新一张)
截屏成功有一声短提示音。退出: 在托盘无图标, 用任务管理器结束 pythonw 或运行 quickshot_stop.bat
"""
import datetime
import io
import os
import winsound

import keyboard
import win32clipboard
import win32con
import win32gui
from PIL import ImageGrab

SAVE_DIR = os.path.expanduser(r"C:\Users\Administrator\screenshots")
os.makedirs(SAVE_DIR, exist_ok=True)


def to_clipboard(img):
    """PNG 进剪贴板: CF_DIB 格式 (BMP 去头)"""
    buf = io.BytesIO()
    img.convert("RGB").save(buf, "BMP")
    data = buf.getvalue()[14:]
    buf.close()
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    finally:
        win32clipboard.CloseClipboard()


def archive(img):
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(SAVE_DIR, f"{ts}.png")
    img.save(path, "PNG")
    img.save(os.path.join(SAVE_DIR, "latest.png"), "PNG")
    return path


def shot_fullscreen():
    img = ImageGrab.grab(all_screens=True)
    to_clipboard(img)
    archive(img)
    winsound.MessageBeep(winsound.MB_ICONASTERISK)


def shot_active_window():
    hwnd = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox=rect, all_screens=True)
    to_clipboard(img)
    archive(img)
    winsound.MessageBeep(winsound.MB_ICONASTERISK)


def main():
    keyboard.add_hotkey("f9", shot_fullscreen)
    keyboard.add_hotkey("f10", shot_active_window)
    keyboard.wait()   # 常驻后台


if __name__ == "__main__":
    main()
