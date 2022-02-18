


from pathlib import Path
from tkinter import *
from turtle import bgcolor 
from PIL import ImageTk,Image 
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Objeto de Aprendizagem")
window.geometry("720x480")
window.configure(bg = "#798896")

def tab1():
    global canvas, entry_image_1, entry_bg_1, entry_1, button_image_1, button_1, image_image_1, image_1, image_image_2, image_2, image_image_3, image_3, tab2
    def tab2():
        global   img, canvas2, tab2_creation, nome
        nome = entry_1.get()
        if nome != "":
            #apagar itens para recriar a tela
            print(nome)
            
            entry_1.destroy(), button_1.destroy(), canvas.destroy()
            



            def tab2_creation():
                global image_image_4, image_4, canvas3, button_4, button_5, button_6, button_image_5, button_image_4, button_image_6
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
                    command=tab3,
                    relief="flat"
                )
                button_6.place(
                    x=38.0,
                    y=370.0,
                    width=193.0,
                    height=35.0
                )
                canvas3.create_text(231.0,305.0,anchor="nw",text="IDADE MÉDIA",fill="#FFFFFF",font=("RibeyeMarrow Regular", 36 * -1))
            
            def tab3():
                
                global image_image_5, image_5, canvas4, button_7, button_8, button_image_8, button_image_7, sair
                button_4.destroy(), button_5.destroy(), button_6.destroy(), canvas3.destroy()
                def voltar():
                    canvas4.destroy(), button_7.destroy(), button_8.destroy()
                    tab2_creation()
                def tab4():
                    canvas4.destroy(), button_7.destroy(), button_8.destroy()
                    def voltar2():
                        canvas5.destroy(), button_10.destroy(), button_9.destroy()
                        tab3()
                    def tab5():
                        canvas5.destroy(), button_10.destroy(), button_9.destroy()
                        def tab6():
                            canvas6.destroy(), button_11.destroy(), button_12.destroy()
                            def tab7():
                                canvas7.destroy(), button_13.destroy(), button_14.destroy()
                                global canvas8, button_15,  button_image_15, image_9, image_image_9
                                canvas8 = Canvas(
                                    window,
                                    bg = "#FFFFFF",
                                    height = 480,
                                    width = 720,
                                    bd = 0,
                                    highlightthickness = 0,
                                    relief = "ridge"
                                )

                                canvas8.place(x = 0, y = 0)
                                image_image_9 = PhotoImage(
                                    file=relative_to_assets("image_9.png"))
                                image_9 = canvas8.create_image(
                                    361.0,
                                    240.0,
                                    image=image_image_9
                                )

                                button_image_15 = PhotoImage(
                                    file=relative_to_assets("button_7.png"))
                                button_15 = Button(
                                    image=button_image_15,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=tab2_creation,
                                    relief="flat"
                                )
                                button_15.place(
                                    x=540.0,
                                    y=408.0,
                                    width=116.0,
                                    height=34.637298583984375
                                )
                            global canvas7, image_image_8, image_8, button_14, button_13, button_image_13, button_image_14
                            canvas7 = Canvas(
                                window,
                                bg = "#FFFFFF",
                                height = 480,
                                width = 720,
                                bd = 0,
                                highlightthickness = 0,
                                relief = "ridge"
                            )

                            canvas7.place(x = 0, y = 0)
                            image_image_8 = PhotoImage(
                                file=relative_to_assets("image_8.png"))
                            image_8 = canvas7.create_image(
                                360.0,
                                239.0,
                                image=image_image_8
                            )

                            button_image_13 = PhotoImage(
                                file=relative_to_assets("button_7.png"))
                            button_13 = Button(
                                image=button_image_13,
                                borderwidth=0,
                                highlightthickness=0,
                                command=tab5,
                                relief="flat"
                            )
                            button_13.place(
                                x=47.0,
                                y=25.0,
                                width=116.0,
                                height=34.637306213378906
                            )

                            button_image_14 = PhotoImage(
                                file=relative_to_assets("button_9.png"))
                            button_14 = Button(
                                image=button_image_14,
                                borderwidth=0,
                                highlightthickness=0,
                                command=tab7,
                                relief="flat"
                            )
                            button_14.place(
                                x=183.0,
                                y=25.0,
                                width=116.0,
                                height=34.637306213378906
                            )
                        global canvas6, image_7, button_11, button_12, image_image_7, button_image_11, button_image_12
                        canvas6 = Canvas(
                            window,
                            bg = "#FFFFFF",
                            height = 480,
                            width = 720,
                            bd = 0,
                            highlightthickness = 0,
                            relief = "ridge"
                        )
                        
                        canvas6.place(x = 0, y = 0)
                        image_image_7 = PhotoImage(
                            file=relative_to_assets("image_7.png"))
                        image_7 = canvas6.create_image(
                            360.0,
                            240.0,
                            image=image_image_7
                        )

                        button_image_11 = PhotoImage(
                            file=relative_to_assets("button_7.png"))
                        button_11 = Button(
                            image=button_image_11,
                            borderwidth=0,
                            highlightthickness=0,
                            command=tab4,
                            relief="flat"
                        )
                        button_11.place(
                            x=47.0,
                            y=25.0,
                            width=116.0,
                            height=34.637306213378906
                        )

                        button_image_12 = PhotoImage(
                            file=relative_to_assets("button_8.png"))
                        button_12 = Button(
                            image=button_image_12,
                            borderwidth=0,
                            highlightthickness=0,
                            command=tab6,
                            relief="flat"
                        )
                        button_12.place(
                            x=183.0,
                            y=25.0,
                            width=116.0,
                            height=34.637306213378906
                        )
                    global image_6, image_image_6, button_10, button_9, button_image_10, button_image_9, canvas5
                    canvas5 = Canvas(
                        window,
                        bg = "#FFFFFF",
                        height = 480,
                        width = 720,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge"
                    )

                    canvas5.place(x = 0, y = 0)
                    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
                    image_6 = canvas5.create_image(
                        362.0,
                        240.0,
                        image=image_image_6
                    )

                    button_image_9 = PhotoImage(
                        file=relative_to_assets("button_8.png"))
                    button_9 = Button(
                        image=button_image_9,
                        borderwidth=0,
                        highlightthickness=0,
                        command=tab5,
                        relief="flat"
                    )
                    button_9.place(
                        x=183.0,
                        y=25.0,
                        width=116.0,
                        height=34.637306213378906
                    )

                    button_image_10 = PhotoImage(
                        file=relative_to_assets("button_7.png"))
                    button_10 = Button(
                        image=button_image_10,
                        borderwidth=0,
                        highlightthickness=0,
                        command=voltar2,
                        relief="flat"
                    )
                    button_10.place(
                        x=47.0,
                        y=25.0,
                        width=116.0,
                        height=34.637306213378906
                    )
                canvas4 = Canvas(
                    window,
                    bg = "#FFFFFF",
                    height = 480,
                    width = 720,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge"
                )

                canvas4.place(x = 0, y = 0)
                image_image_5 = PhotoImage(
                    file=relative_to_assets("image_5.png"))
                image_5 = canvas4.create_image(
                    359.0,
                    241.0,
                    image=image_image_5
                )

                button_image_7 = PhotoImage(
                    file=relative_to_assets("button_7.png"))
                button_7 = Button(
                    image=button_image_7,
                    borderwidth=0,
                    highlightthickness=0,
                    command=voltar,
                    relief="flat"
                )
                button_7.place(
                    x=47.0,
                    y=425.0,
                    width=116.0,
                    height=34.637298583984375
                )

                button_image_8 = PhotoImage(
                    file=relative_to_assets("button_8.png"))
                button_8 = Button(
                    image=button_image_8,
                    borderwidth=0,
                    highlightthickness=0,
                    command=tab4,
                    relief="flat"
                )
                button_8.place(
                    x=189.0,
                    y=425.0,
                    width=116.0,
                    height=34.637298583984375
                )
            def sair():
                window.destroy()
            #criação dos elementos da segunda tela
            tab2_creation()
            
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
