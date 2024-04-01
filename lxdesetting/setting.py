import tkinter as tk
import os

# List of applications along with their descriptions
applications = [
    {'name': 'Arandr', 'description': 'Monitor Settings Editor', 'command': 'arandr'},
    {'name': 'Lxsession Default Apps', 'description': 'Default Applications Settings', 'command': 'lxsession-default-apps'},
    {'name': 'Lxinput', 'description': 'Keyboard and Mouse Settings', 'command': 'lxinput'},
    {'name': 'Xfce4 Power Manager', 'description': 'Power Management', 'command': 'xfce4-power-manager'},
    {'name': 'Obconf', 'description': 'Openbox Appearance Configurator', 'command': 'obconf'},
    {'name': 'Lxappearance', 'description': 'LXDE Appearance Configurator', 'command': 'lxappearance'},
    {'name': 'Pavucontrol', 'description': 'Sound Settings', 'command': 'pavucontrol'},
    {'name': 'Lxsession Edit', 'description': 'LXDE Session Configuration Editor', 'command': 'lxsession-edit'},
    {'name': 'Lxrand', 'description': 'LXDE Resolution Configurator', 'command': 'lxrand'},
    {'name': 'Grub Customizer', 'description': 'GRUB Editor', 'command': 'grub-customizer'},
    {'name': 'HP Toolbox', 'description': 'HP Printer Diagnostic Tool', 'command': 'hp-toolbox'},
    {'name': 'Gparted', 'description': 'Graphical Partition Manager', 'command': 'gparted'},
    {'name': 'Nitrogen', 'description': 'Wallpaper Settings Manager', 'command': 'nitrogen'},
    {'name': 'Conky Manager', 'description': 'Conky Widgets Manager', 'command': 'conky-manager'},
    {'name': 'LXDM Setting', 'description': 'LXDM Login Manager Settings', 'command': 'sudo lxdm-config'},
    {'name': 'GPU Test', 'description': 'Graphics Card Performance Test', 'command': 'glmark2'},
    {'name': 'System Monitor', 'description': 'System Resource Monitor', 'command': 'gnome-system-monitor'},
    {'name': 'LXDE Menu', 'description': 'LXDE Menu Editor', 'command': 'menulibre'},
    {'name': 'HardInfo', 'description': 'System Analyzer', 'command': 'hardinfo'},
]

# Function to run the selected application
def run_application(index):
    os.system(applications[index]['command'])

# Function to close the program
def close_program():
    window.destroy()

# Function to display tooltip next to the mouse cursor
def show_tooltip(event, description):
    tooltip_label.config(text=description)
    tooltip_label.place(x=event.x_root + 10, y=event.y_root + 10)

# Function to hide the tooltip
def hide_tooltip(event):
    tooltip_label.config(text='')
    tooltip_label.place_forget()

# Create the window
window = tk.Tk()
window.title('LXDM Setting')
window.configure(bg='white')

# Function to center elements after window resize
def center_window(event=None):
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Call center_window function at the beginning
center_window()

# Add resize event
window.bind('<Configure>', center_window)

# Create labels with application names and buttons for each application
for index, app_info in enumerate(applications):
    app_label = tk.Label(window, text=app_info['name'], bg='white')
    app_label.pack(padx=10, pady=5, anchor='e')

    app_button = tk.Button(window, text='Run', 
                           command=lambda index=index: run_application(index),
                           relief='raised', bg='lightblue')
    app_button.pack(padx=10, pady=5, anchor='w')
    app_button.bind("<Enter>", lambda event, desc=app_info['description']: show_tooltip(event, desc))
    app_button.bind("<Leave>", hide_tooltip)

# Create a button to close the program
close_button = tk.Button(window, text='Close', command=close_program, bg='lightblue')
close_button.pack(pady=10)

# Button to start and stop Xcompmgr program
xcompmgr_button = tk.Button(window, text='Start Xcompmgr', command=lambda: os.system('xcompmgr -c -f -F -D 5 &'), bg='lightblue')
xcompmgr_button.pack(padx=5, pady=5)

kill_xcompmgr_button = tk.Button(window, text='Stop Xcompmgr', command=lambda: os.system('killall xcompmgr'), bg='lightblue')
kill_xcompmgr_button.pack(padx=5, pady=5)

# Label for tooltip
tooltip_label = tk.Label(window, text='', bg='white')
tooltip_label.bind("<Leave>", hide_tooltip)
tooltip_label.place(x=0, y=0)

# Run the main loop of the program
window.mainloop()
