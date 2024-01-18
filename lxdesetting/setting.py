import tkinter as tk
import os

# lista aktywatorów i ich nazw
applications = [
    {'name': 'Arandr', 'command': 'arandr'},
    {'name': 'Lxsession Default Apps', 'command': 'lxsession-default-apps'},
    {'name': 'Lxinput', 'command': 'lxinput'},
    {'name': 'Xfce4 Power Manager', 'command': 'xfce4-power-manager'},
    {'name': 'Obconf', 'command': 'obconf'},
    {'name': 'Lxappearance', 'command': 'lxappearance'},
    {'name': 'Pavucontrol', 'command': 'pavucontrol'},
    {'name': 'Lxsession Edit', 'command': 'lxsession-edit'},
    {'name': 'Lxrand', 'command': 'lxrand'},
    {'name': 'Grub Customizer', 'command': 'grub-customizer'},
    {'name': 'HP Toolbox', 'command': 'hp-toolbox'},
    {'name': 'Gparted', 'command': 'gparted'},
    {'name': 'Nitrogen', 'command': 'nitrogen'},
    {'name': 'Conky Manager', 'command': 'conky-manager'},
    {'name': 'LXDM Setting', 'command': 'sudo lxdm-config'},
    {'name': 'GPU Test', 'command': 'glmark2'},
    {'name': 'System Monitor', 'command': 'gnome-system-monitor'},
    {'name': 'LXDE Menu', 'command': 'menulibre'},
    {'name': 'HardInfo', 'command': 'hardinfo'},



]

# funkcja uruchamiająca wybrany program
def run_application(index):
    os.system(applications[index]['command'])

# funkcja zamykająca program
def close_program():
    window.destroy()

# stworzenie okna
window = tk.Tk()
window.title('LXDM Setting')
window.configure(bg='white')

# stworzenie etykiet z nazwami programów i przycisków dla każdego aktywatora
num_rows = (len(applications) + 1) // 2
for i in range(num_rows):
    for j in range(2):
        index = i * 2 + j
        if index < len(applications):
            app_label = tk.Label(window, text=applications[index]['name'])
            app_label.grid(row=i, column=j*2, padx=10, pady=10, sticky='e')
            
            app_button = tk.Button(window, text='Uruchom', 
                                   command=lambda index=index: run_application(index))
            app_button.grid(row=i, column=j*2+1, padx=10, pady=10)

# stworzenie przycisku zamykającego program
close_button = tk.Button(window, text='Zamknij', command=close_program)
close_button.grid(row=num_rows+1, column=0, columnspan=2, pady=10)

# przycisk do włączania i wyłączania programu Xcompmgr
xcompmgr_button = tk.Button(window, text='Włącz Xcompmgr', command=lambda: os.system('xcompmgr -c -f -F -D 5 &'))
xcompmgr_button.grid(row=num_rows, column=0, padx=5, pady=5)

kill_xcompmgr_button = tk.Button(window, text='Wyłącz Xcompmgr', command=lambda: os.system('killall xcompmgr'))
kill_xcompmgr_button.grid(row=num_rows, column=1, padx=5, pady=5)

# uruchomienie głównej pętli programu
window.mainloop()

