from tkinter import *
from tkinter import messagebox, ttk
import subprocess


def göster():
    try:
        ifconfig_cikti = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        ifconfig_cikti = ifconfig_cikti.stdout
        listb = Listbox(pencere1, width=80, height=40)
        listb.place(x=50,y=50)
        
        # ifconfig çıktısını satır satır böler ve her bir satırı listbox'a ekler
        for line in ifconfig_cikti.splitlines():
            listb.insert(END, line)  

    except Exception as e:
        print(e)
        messagebox.showerror("Başarısız", "Tekrar deneyin.")


pencere1 = Tk()
pencere1.geometry("800x800+300+0")
pencere1.title("KLAVYE DEĞİŞTİRME")

label1 = Label(pencere1, text="İNTERFACE BİLGİLERİNİ ALMAK İÇİN TIKLAYINIZ")
label1.pack()

buton = Button(pencere1, text="BİLGİLERİ GÖSTER", command=göster)
buton.pack()

pencere1.mainloop()
