import pygame, random, time

pygame.init()
pygame.display.init()

class Button():
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 22)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


WHITE = (255, 255, 255)
GREEN = (0, 204, 102)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
CYAN = (0,206,209)
ORANGE = (255,140,0)


WIDTH = 900
HEIGHT = 540
win_size = (WIDTH, HEIGHT)

FPS = 60

WIDTH_OF_BAR = 12

length_of_arr = WIDTH // WIDTH_OF_BAR

method = "bubble_sort"

start_button = Button(BLACK, 0, 5, 120, 25, "Start")
reset_button = Button(BLACK, 0, 35, 120, 25, "Reset")
bubble_sort_button = Button(BLACK, 130,5, 120, 25, "Bubble sort")
insertion_sort_button = Button(BLACK, 130, 35, 120, 25, "Inersertion sort")

array = []
states = []
#0 - changing state
#1 - normal state
#2 - solved state

clock = pygame.time.Clock()

WIN = pygame.display.set_mode(win_size)
pygame.display.set_caption("Sorting Alogrithm Visualizer")

sorted = False

def create_array(number_of_elements):
    for i in range(number_of_elements):
        array.append(random.randint(10,HEIGHT-100))
        states.append(1)

def start():
    global method
    if method == "bubble_sort":
        bubble_sort(array)
    elif method == "insertion_sort":
        insertion_sort(array)

def reset():
    for i in range(len(array)):
        array[i] = random.randint(10,HEIGHT-100)
        states[i] = 1

def draw_window():
    #Draw the UI and array to the screen
    WIN.fill(WHITE)
    #Draw all buttons
    start_button.draw(WIN)
    reset_button.draw(WIN)
    bubble_sort_button.draw(WIN)
    insertion_sort_button.draw(WIN)
    #Draw Border
    pygame.draw.rect(WIN, BLACK, pygame.Rect((0,95),(WIDTH,5)))
    #Draw array
    for i in range(len(array)):
        #Apply colors and draw the bars
        if states[i] == 0:
            color = ORANGE
        elif states[i] == 1:
            color = GREEN
        else:
            color = CYAN
        #Draw bar
        pygame.draw.rect(WIN, color, pygame.Rect(int(i*WIDTH_OF_BAR), HEIGHT - array[i], WIDTH_OF_BAR, array[i]))
    pygame.display.update()
    pygame.event.pump()
    time.sleep(0.01)

def mouse(event, pos):
    global method
    if event.type == pygame.MOUSEMOTION:
         if start_button.isOver(pos):
            start_button.color = ORANGE
         else:
            start_button.color = BLACK

         if reset_button.isOver(pos):
            reset_button.color = ORANGE
         else:
            reset_button.color = BLACK

         if bubble_sort_button.isOver(pos):
            bubble_sort_button.color = ORANGE
         else:
            bubble_sort_button.color = BLACK

         if insertion_sort_button.isOver(pos):
            insertion_sort_button.color = ORANGE
         else:
            insertion_sort_button.color = BLACK

    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.isOver(pos):
            start()
        if reset_button.isOver(pos):
            reset()
        if bubble_sort_button.isOver(pos):
            method = "bubble_sort"
        if insertion_sort_button.isOver(pos):
            method = "insertion_sort"

#Sort the array
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)-1-i):
            states[j] = 0
            if j > 0:
                states[j-1] = 1
            if states[j+1] != 2:
                states[j+1] = 1
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
            draw_window()
        if states[j] != 2:
            states[j] = 1
        states[j+1] = 2
    states[0] = 2
    draw_window()
    global sorted
    sorted = True

def insertion_sort(unsorted_list):
    states[0] = 2
    for i in range(1, len(unsorted_list)):
        draw_window()
        key = unsorted_list[i]
        states[i] = 2
        j = i-1
        while (j>=0 and key<unsorted_list[j]):
            states[j] = 0
            unsorted_list[j+1] = unsorted_list[j]
            draw_window()
            states[j] = 2
            j -= 1
        unsorted_list[j+1] = key
        draw_window()
        states[i] = 2
    global sorted
    sorted = True

def main():
    run = True
    create_array(WIDTH//WIDTH_OF_BAR)
    while run:
        draw_window()
        pos = pygame.mouse.get_pos()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                break
            mouse(event, pos)

if __name__ == '__main__':
    main()
