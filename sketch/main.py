import pygame
import sys
from tkinter import *
from tkinter import ttk

WIDTH = 800
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

COLUMNS = 100
ROWS = 100

PIXEL_HEIGHT = HEIGHT//ROWS
PIXEL_WIDTH = WIDTH//COLUMNS

screen = []

class pixel:

    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.drawn = False
        self.neighbours = []

    def color(self, window, color):
        pygame.draw.rect(window, color, (self.x * PIXEL_WIDTH, self.y * PIXEL_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT))

    def set_neighbours(self):
        for temp_x in range(self.x-1, self.x+2):
            for temp_y in range(self.y-1, self.y+2):
                if temp_x == self.x and temp_y == self.y:
                    continue
                if 0 <= temp_x < COLUMNS and 0 <= temp_y < ROWS:
                    self.neighbours.append(screen[temp_x][temp_y])

for i in range(COLUMNS):
    col = []
    for j in range(ROWS):
        col.append(pixel(i, j))
    screen.append(col)

for i in range(COLUMNS):
    for j in range(ROWS):
        screen[i][j].set_neighbours()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEMOTION:

            x, y = pygame.mouse.get_pos()
            i = x//PIXEL_WIDTH
            j = y//PIXEL_HEIGHT

            if event.buttons[0]:
                screen[i][j].drawn = True

            elif event.buttons[2]:
                screen[i][j].drawn = False
                for neighbour in screen[i][j].neighbours:
                    neighbour.drawn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                for i in range(COLUMNS):
                    for j in range(ROWS):
                        screen[i][j].drawn = False
            elif event.key == pygame.K_s:
                prompt = Tk()
                prompt.geometry("300x100")
                prompt.title("Save Image As...")
                
                def save():
                    string = entry.get()
                    pygame.image.save(window, string + ".png")
                    prompt.destroy()

                label = Label(prompt, text="Enter file name", font=("Helvetica 15 bold"))
                label.pack()

                entry = Entry(prompt, width=40)
                entry.focus_set()
                entry.pack()

                ttk.Button(prompt, text="Save", width=10, command=save).pack(pady=13)
                prompt.mainloop()                


        window.fill((255, 255, 255))

        for i in range(COLUMNS):
            for j in range(ROWS):
                if screen[i][j].drawn:
                    screen[i][j].color(window, (0, 0, 0))

        pygame.display.flip()