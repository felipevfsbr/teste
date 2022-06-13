from tkinter import *
from PIL import ImageTk, Image
import pygame
from tkinter import filedialog

# Inicializar mixer
pygame.mixer.init()

# Função Adicionar Musica
def add_musica():
    musica = filedialog.askopenfilename(initialdir='/audio', title='Escolha uma Musica!',
                                        filetypes=(('mp3 Files', '*.mp3'),))
    # Remover caminho local da musica
    musica = musica.replace('C:/Users/felip/PycharmProjects/pythonProject1/Audio/', '')
    musica = musica.replace('.mp3', '')

    # Adicionar Musica a lista
    song_box.insert(END, musica)

# Tocar Musica Selecionada

def play():
    musica = song_box.get(ACTIVE)
    musica = f'C:/Users/felip/PycharmProjects/pythonProject1/Audio/{musica}.mp3'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=0)

# Parar Musica

def parar():
    pygame.mixer.music.stop()

# Pausa Global
pausado = False

# Pausar Musica
def pausar(is_pausado):
    global pausado
    pausado = is_pausado
    if pausado:
        # despausar
        pygame.mixer.music.unpause()
        pausado = False
    else:
        # pausar
        pygame.mixer.music.pause()
        pausado = True

root = Tk()
root.title('Mp3 Player, Made by Felipe Néris')
root.iconbitmap()
root.geometry('500x300')

# Inicializando pygame mixer
pygame.mixer.init()

# Playlist
song_box = Listbox(root, bg='blue', fg='yellow', width=60, selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

# Botões de controle Imagens

pausa_img = ImageTk.PhotoImage(Image.open("images/pausa.png"))
play_img = ImageTk.PhotoImage(Image.open("images/play.png"))
voltar_img = ImageTk.PhotoImage(Image.open('images/retorna.png'))
avancar_img = ImageTk.PhotoImage(Image.open('images/avança.png'))
parar_img = ImageTk.PhotoImage(Image.open('images/stop.png'))

# Botões de controle Moldura

botoes_moldura = Frame(root)
botoes_moldura.pack()

# Botões de controle Funções

pausa = Button(botoes_moldura, image=pausa_img, borderwidth=0, command=lambda: pausar(pausado))
play = Button(botoes_moldura, image=play_img, borderwidth=0, command=play)
voltar = Button(botoes_moldura, image=voltar_img, borderwidth=0)
avancar = Button(botoes_moldura, image=avancar_img, borderwidth=0)
parar = Button(botoes_moldura, image=parar_img, borderwidth=0, command=parar)

pausa.grid(row=0, column=2, padx=10)
play.grid(row=0, column=3, padx=10)
voltar.grid(row=0, column=0, padx=10)
avancar.grid(row=0, column=1, padx=10)
parar.grid(row=0, column=4, padx=10)

# Criar Menu

meu_menu = Menu(root)
root.config(menu=meu_menu)

# Menu para Adicionar Música

menu_add_musica = Menu(meu_menu)
meu_menu.add_cascade(label='Adicionar Musicas', menu=menu_add_musica)
menu_add_musica.add_command(label='Adicionar uma Música á Playlist.', command=add_musica)

root.mainloop()
