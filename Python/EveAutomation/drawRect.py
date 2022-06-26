import win32api
import win32gui
import win32ui
from win32api import GetSystemMetrics


class RectDrawer:
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0, 0))
    monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

    red = win32api.RGB(255, 0, 0)  # Red color
    past_coordinates = monitor

    def Draw(DrawRect):
        posx = DrawRect[0]
        posy = DrawRect[1]
        Width = DrawRect[2]
        Height = DrawRect[2]
        for x in range(Width):
            win32gui.SetPixel(RectDrawer.dc, posx + x, posy, RectDrawer.red)
            win32gui.SetPixel(RectDrawer.dc, posx + x, posy + Height, RectDrawer.red)
            for y in range(Height):
                win32gui.SetPixel(RectDrawer.dc, posx, posy + y, RectDrawer.red)
                win32gui.SetPixel(RectDrawer.dc, posx + Width, posy + y, RectDrawer.red)



