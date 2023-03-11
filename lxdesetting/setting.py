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
    {'name': 'Gparted', 'command': 'gparted'}
]

# funkcja uruchamiająca wybrany program
def run_application(index):
    os.system(applications[index]['command'])

# funkcja zamykająca program
def close_program():
    window.destroy()

# stworzenie okna
window = tk.Tk()
window.title('Aktywatory')

# stworzenie przycisków dla każdego aktywatora
num_rows = (len(applications) + 1) // 2
for i in range(num_rows):
    for j in range(2):
        index = i * 2 + j
        if index < len(applications):
            app_button = tk.Button(window, text=applications[index]['name'], 
                                   command=lambda index=index: run_application(index))
            app_button.grid(row=i, column=j, padx=5, pady=5)

# stworzenie przycisku zamykającego program
close_button = tk.Button(window, text='Zamknij', command=close_program)
close_button.grid(row=num_rows, column=0, columnspan=2, pady=10)

# uruchomienie głównej pętli programu
window.mainloop()
