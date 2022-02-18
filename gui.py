

from faulthandler import disable
from pathlib import Path
from tkinter import *
from turtle import bgcolor 
from PIL import ImageTk,Image 
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import DISABLED, Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Objeto de Aprendizagem")
window.geometry("720x480")
window.configure(bg = "#798896")

def tab1():
    global canvas, entry_image_1, entry_bg_1, entry_1, button_image_1, button_1, image_image_1, image_1, image_image_2, image_2, image_image_3, image_3
    def tab2():
        global l, frame, img, canvas2, image_image_4, image_4, canvas3, button_4, button_5, button_6, button_image_5, button_image_4, button_image_6
        if entry_1.get() != "":
            #apagar itens para recriar a tela
            
            
            entry_1.destroy(), button_1.destroy(), canvas.destroy()
            




            
            def sair():
                window.destroy()
            #criação dos elementos da segunda tela
            canvas3 = Canvas(
                window,
                bg = "#7A8997",
                height = 480,
                width = 720,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas3.place(x = 0, y = 0)
            image_image_4 = PhotoImage(
                file=relative_to_assets("image_4.png"))
            image_4 = canvas3.create_image(
                360.0,
                151.0,
                image=image_image_4
            )

            button_image_4 = PhotoImage(
                file=relative_to_assets("button_4.png"))
            button_4 = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=sair,
                relief="flat"
            )
            button_4.place(
                x=493.0,
                y=370.0,
                width=193.0,
                height=35.0
            )

            button_image_5 = PhotoImage(
                file=relative_to_assets("button_5.png"))
            button_5 = Button(
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_5 clicked"),
                relief="flat"
            )
            button_5.place(
                x=274.0,
                y=370.0,
                width=193.0,
                height=35.0
            )

            button_image_6 = PhotoImage(
                file=relative_to_assets("button_6.png"))
            button_6 = Button(
                image=button_image_6,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_6 clicked"),
                relief="flat"
            )
            button_6.place(
                x=38.0,
                y=370.0,
                width=193.0,
                height=35.0
            )

            canvas3.create_text(231.0,305.0,anchor="nw",text="IDADE MÉDIA",fill="#FFFFFF",font=("RibeyeMarrow Regular", 36 * -1))
        else:
            
                
            #Alerta para caso o usuário esqueça de colocar o nome     
            canvas2 = Canvas(window, width = 165, height = 93, bg="red", bd=0, relief = "ridge")  
            canvas2.pack()  
            img = ImageTk.PhotoImage(Image.open("alert.png"))  
            canvas2.create_image(0, 0, anchor=NW, image=img) 
        
    #criação da primeira tela       
    canvas = Canvas(
        window,
        bg = "#798896",
        height = 480,
        width = 720,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    canvas.place(x = 0, y = 0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        549.5,
        150.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D5D9E1",
        highlightthickness=0
    )
    entry_1.place(
        x=504.5,
        y=133.0,
        width=90.0,
        height=33.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=tab2,
        relief="flat"
    )
    button_1.place(
        x=453.0,
        y=233.0,
        width=193.0,
        height=35.0
    )

    canvas.create_text(
        507.0,
        88.0,
        anchor="nw",
        text="Aluno\n",
        fill="#000000",
        font=("Roboto", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        436.0,
        402.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        676.0,
        42.0,
        image=image_image_2
    )

    canvas.create_text(
        540.0,
        282.0,
        anchor="nw",
        text=".",
        fill="#7A8997",
        font=("Roboto", 18 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        185.0,
        247.0,
        image=image_image_3
    )
tab1()

window.resizable(False, False)

window.mainloop()
