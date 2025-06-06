from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#criando janela
janela = Tk()
janela.title("")
janela.geometry("550x510")


ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx= 272)

style = ttk.Style(janela)
style.theme_use("clam")

#Criando Frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

#Trocar pokemon
def trocar_pokemon(i):
    global img_pok

    frame_pokemon.configure(bg=pokemon[i]['cor'])

    pok_nome.config(text=i, bg=pokemon[i]['cor'])
    pok_tipo.config(text=pokemon[i]['tipo'], bg=pokemon[i]['cor'])
    pok_id.config(text=pokemon[i]['id'], bg=pokemon[i]['cor'])
    pok_hp.config(text=f"HP: {pokemon[i]['status']['HP']}")
    pok_atack.config(text=f"Ataque: {pokemon[i]['status']['Ataque']}")
    pok_defesa.config(text=f"Defesa: {pokemon[i]['status']['Defesa']}")
    pok_velocidade.config(text=f"Velocidade: {pokemon[i]['status']['Velocidade']}")
    pok_total.config(text=f"Total: {pokemon[i]['status']['Total']}")
    pok_habilidade.config(text="Habilidades")

    habilidades = pokemon[i]['habilidades']
    pok_raio.config(text=habilidades[0] if len(habilidades) > 0 else "")
    pok_soco.config(text=habilidades[1] if len(habilidades) > 1 else "")

    # Atualiza imagem
    img_pok = Image.open(pokemon[i]['imagem'])
    img_pok = img_pok.resize((238, 238))
    img_pok = ImageTk.PhotoImage(img_pok)
    pok_img.config(image=img_pok, bg=pokemon[i]['cor'])
    pok_img.image = img_pok  # evita garbage collection

    pok_tipo.lift()

# Nome do pokemon
pok_nome = Label(frame_pokemon, text="Pikachu", relief='flat', anchor='center', font=('Fixedsys 20 bold'), fg=co1, bg=pokemon['Pikachu']['cor'])
pok_nome.place(x=12, y=15)

#categoria do pokemon
pok_tipo =  Label(frame_pokemon, text="", relief='flat', anchor='center', font=('Ivy 10 bold'), fg=co1)
pok_tipo.place(x=12, y=50)

#ID do pokemon
pok_id =  Label(frame_pokemon, text="", relief='flat', anchor='center', font=('Ivy 10 bold'), fg=co1)
pok_id.place(x=12, y=75)

#Status do pokemon
pok_status =  Label(janela, text="Status", relief='flat', anchor='center', font=('Verdana 20'), fg=co0)
pok_status.place(x=15, y=310)

#HP do pokemon
pok_hp =  Label(janela, text="HP: 100", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_hp.place(x=15, y=360)

#Ataque do pokemon
pok_atack =  Label(janela, text="Ataque: 600", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_atack.place(x=15, y=385)

#Defesa do pokemon
pok_defesa =  Label(janela, text="Defesa: 500", relief='flat', anchor='center', font=('Verdana 10'),  fg=co4)
pok_defesa.place(x=15, y=410)

#Velocidade do pokemon
pok_velocidade =  Label(janela, text="Velocidade: 300", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_velocidade.place(x=15, y=435)

#Total do pokemon
pok_total =  Label(janela, text="Total: 1800", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_total.place(x=15, y=460)

#Habilidade do pokemon
pok_habilidade =  Label(janela, text="Habilidades", relief='flat', anchor='center', font=('Verdana 20'), fg=co0)
pok_habilidade.place(x=180, y=310)

#HP do pokemon
pok_raio =  Label(janela, text="Raio Do Trovão", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_raio.place(x=180, y=360)

#Soco do pokemon
pok_soco =  Label(janela, text="Soco do Trovão", relief='flat', anchor='center', font=('Verdana 10'), fg=co4)
pok_soco.place(x=180, y=385)

#Criando Botões para pokemons

#Botão pikachu
img_cab_pikachu = Image.open("images/cabeca-pikachu.png")
img_cab_pikachu = img_cab_pikachu.resize((40, 40))
img_cab_pikachu = ImageTk.PhotoImage(img_cab_pikachu)
pik_img_b = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=img_cab_pikachu, text='Pikatchu', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
pik_img_b.place(x=375, y=10)


#Botão Bulbasaur
img_cab_bulbasaur = Image.open("images/cabeca-bulbasaur.png")
img_cab_bulbasaur = img_cab_bulbasaur.resize((40, 40))
img_cab_bulbasaur = ImageTk.PhotoImage(img_cab_bulbasaur)
bub_img_b = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=img_cab_bulbasaur, text='Bulbasaur', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
bub_img_b.place(x=375, y=70)

#Botão Charmander
img_cab_charmander = Image.open("images/cabeca-charmander.png")
img_cab_charmander = img_cab_charmander.resize((40, 40))
img_cab_charmander = ImageTk.PhotoImage(img_cab_charmander)
char_img_b = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=img_cab_charmander, text='Charmander', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
char_img_b.place(x=375, y=130)

#Botão Gyarados
img_cab_gyarados = Image.open("images/cabeca-gyarados.png")
img_cab_gyarados = img_cab_gyarados.resize((40, 40))
img_cab_gyarados = ImageTk.PhotoImage(img_cab_gyarados)
gya_img_b = Button(janela, command=lambda:trocar_pokemon('Gyarados'), image=img_cab_gyarados, text='Gyarados', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
gya_img_b.place(x=375, y=190)

#Botão Gengar
img_cab_gengar = Image.open("images/cabeca-gengar.png")
img_cab_gengar = img_cab_gengar.resize((40, 40))
img_cab_gengar = ImageTk.PhotoImage(img_cab_gengar)
gen_img_b = Button(janela, command=lambda:trocar_pokemon('Gengar'), image=img_cab_gengar, text='Gengar', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
gen_img_b.place(x=375, y=250)

#Botão Dragonite
img_cab_dragonite = Image.open("images/cabeca-dragonite.png")
img_cab_dragonite = img_cab_dragonite.resize((40, 40))
img_cab_dragonite = ImageTk.PhotoImage(img_cab_dragonite)
dra_img_b = Button(janela, command=lambda:trocar_pokemon('Dragonite'),image=img_cab_dragonite, text='Dragonite', width=150, relief='raised', overrelief='ridge', compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'))
dra_img_b.place(x=375, y=310)

# Inicializa com a imagem do Pikachu
img_pok = Image.open(pokemon['Pikachu']['imagem'])
img_pok = img_pok.resize((238, 238))
img_pok = ImageTk.PhotoImage(img_pok)
pok_img = Label(frame_pokemon, image=img_pok, relief='flat', bg=pokemon['Pikachu']['cor'])
pok_img.place(x=60, y=50)

trocar_pokemon('Pikachu')  # Inicializa com o Pikachu


janela.mainloop()