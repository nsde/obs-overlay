
"""
Gets Song which is currently playing on Spotify.
Nothing more, nothing less.

No API.
No external programs needed.
No dependencies.

Only works on Windows! (Modify the get_windows() function to make it work on other platforms).
Furthermore, some features such as (Song.featuring) need more testing.
"""

import ctypes

# Any other programs you have opened.
# This is only needed if it doesn't work properly.
BLACKLIST = ['OBS', 'Visual Studio', 'LibreWolf', 'Firefox', 'Chrome', 'Discord']

def get_windows():
    """Returns a list of all currently opened Windows."""
    # Stolen from https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/
    # I don't even pretend to know what this does

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    
    titles = []
    def foreach_window(hwnd, lParam):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            
            if buff.value:
                titles.append(buff.value)
        return True

    ctypes.windll.user32.EnumWindows(EnumWindowsProc(foreach_window), 0)
    
    return titles

class Song:
    def __init__(self, window_title: str):
        self.window = window_title
        
        title = window_title.split(' - ')
        
        self.full_title = title[1]
        self.title = self.full_title.split(' (')[0]

        self.artist = title[0]
        
        self.is_remix = 'remix' in self.title.lower()
        self.is_live = '(live)' in self.title.lower()

    @property
    def featuring(self) -> str:
        # TODO: Better detection
        if '(' in self.title:
            try:
                return ' '.join(self.title.split('(')[-1].split()[1:]).split(')')[0]
            except IndexError:
                return None
        
    def __str__(self) -> str:
        return self.window

def get_current_song():
    for window in get_windows():
        if window.count(' - '):
            allow = True
            # TODO: Add more checks
            for blacklisted in BLACKLIST:
                if blacklisted in window:
                    allow = False

            if allow:
                return Song(window)

if __name__ == '__main__':
    print(get_current_song().featuring)
