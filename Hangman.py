import pygame
import os
import math
from random_word import RandomWords

#setup display
pygame.init()
WIDTH,HEIGHT = 800,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HANGMAN GAME USING PYGAME MODULE ! ")
FPS = 60
clock = pygame.time.Clock()
images = []

for i in range(7):
	images.append(pygame.image.load(os.path.join("Images","hangman"+str(i)+".png")))

#game variables
hangman_status=0
r = RandomWords()
word = r.get_random_word().upper()
while len(word) > 12 or '-' in word:
	word = r.get_random_word().upper()

guessed=[]

WHITE=(255,255,255)
BLACK=(0,0,0)


#button variables
letters=[]
RADIUS=20
GAP=(WIDTH+2*RADIUS)/14-RADIUS
printL=True
for i in range(26):
	x=(i%13+1)*GAP+(i%13)*RADIUS
	y=400+(GAP+RADIUS)*math.floor(i/13)
	letters.append([x,y,chr(65+i),printL])

#fonts
LETTER_FONT=pygame.font.SysFont("Arial Black",25)
WORD_FONT=pygame.font.SysFont("Arial Black",35)
WORD_LAST_FONT=pygame.font.SysFont("Arial Black",45)
TITLE_FONT=pygame.font.SysFont("Arial Black",40)

#load images

def draw_window():

	WIN.fill(WHITE)
	WIN.blit(images[hangman_status],(150,100))
	#draw title
	text=TITLE_FONT.render("DEVELOPER HANGMAN ! ",1,BLACK)
	WIN.blit(text,(WIDTH/2-text.get_width()/2,20))
	#draw word
	display_word=""
	for letter in word:
		if letter in guessed :
			display_word+=letter+" "
		else:
			display_word+='_ '
	text=WORD_FONT.render(display_word,1,BLACK)
	WIN.blit(text,(350,200))
	for letter in letters:
		x,y,ltr,printL=letter
		if printL==True:
			pygame.draw.circle(WIN,BLACK,(x,y),RADIUS,3)
			text=LETTER_FONT.render(ltr,1,BLACK)
			WIN.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
	pygame.display.update()




def main():
	global hangman_status,word,guessed
	run=True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				m_x,m_y=pygame.mouse.get_pos()
				for letter in letters:
					x,y,ltr,printL=letter 
					dis=math.sqrt((x-m_x)**2+(y-m_y)**2)
					if dis<RADIUS:
						guessed.append(ltr)

						# if choosen the wrong word or clicking the wrong key again and again
						if ltr not in word and letter[3] :
							hangman_status+=1
						letter[3]=False

		draw_window()
		won=True
		for letter in word:
			if letter not in guessed:
				won=False
				break
		if won:
			WIN.fill(WHITE)
			pygame.time.delay(100)
			text = WORD_LAST_FONT.render("YOU WON !" , 1 , BLACK)
			WIN.blit(text,(WIDTH//2-text.get_width()//2, HEIGHT//2 - text.get_height()//2 ))
			hangman_status=0 
			guessed=[]

			r = RandomWords()
			word = r.get_random_word().upper()
			while len(word) > 12 or '-' in word:
				word = r.get_random_word().upper()

			for letter in letters:
				letter[3]=True
			pygame.display.update()
			pygame.time.delay(1500)	
			break		

		if hangman_status==6:
			WIN.fill(WHITE)
			pygame.time.delay(100)
			text = WORD_LAST_FONT.render("YOU ARE HANGED !" , 1 , BLACK)
			WIN.blit(text,(WIDTH//2-text.get_width()//2, HEIGHT//2 - text.get_height()//2  - 50))
			text = WORD_LAST_FONT.render(f"Correct word : {word}" , 1 , BLACK)
			WIN.blit(text,(WIDTH//2-text.get_width()//2, HEIGHT//2 - text.get_height()//2  + 50))
			hangman_status=0 
			guessed=[]
			r = RandomWords()
			word = r.get_random_word().upper()
			while len(word) > 12 or '-' in word:
				word = r.get_random_word().upper()

			for letter in letters:
				letter[3]=True
			pygame.display.update()
			pygame.time.delay(1500)	
			break	

	if run:
		main()
	else:		
		pygame.quit()
main()