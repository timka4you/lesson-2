import tkinter as tk
from subprocess import run


def redscreen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Use full-screen mode
    root.wm_attributes('-topmost', True)  # Use Sticky mode
    # The following code can be based on other results they want to achieve changes
    frame = tk.Frame(root, bg='darkblue')
    frame.pack(fill='both', expand=True)
    return root


def close_explorer():
    "" "Close the Explorer process" ""
    run('taskkill /F /IM explorer.exe')


if __name__ == '__main__':
    root = redscreen()
    close_explorer()
    root.mainloop()
