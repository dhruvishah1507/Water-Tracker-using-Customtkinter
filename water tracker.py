
import customtkinter as ctk
import playsound3 as ps
window = ctk.CTk()
window.geometry("400x400")
window.title("Water Tracker")

def alarm():
    ps.playsound("danger-alarm-sound-effect-meme.mp3")


def play():
    timer = int(time.get())
    ms = (timer*60)*60
    window.after(ms, alarm)
    

label = ctk.CTkLabel(window, text = "Water Tracker",font= ("Vardana",25))
label.pack(pady=20)
task = ctk.CTkEntry(window, placeholder_text="Task", font = ("Vardana",15))
task.pack(pady=15)
time = ctk.CTkEntry(window, placeholder_text="Timer", font = ("Vardana",15))
time.pack(pady=15)
button = ctk.CTkButton(window, text= "Start", font = ("Vardana",15), command=lambda:play())
button.pack(pady=15)

window.mainloop()

