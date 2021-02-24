import pygame, keyboard, datetime, random, time
import screen_brightness_control as sbc
from win32api import GetSystemMetrics
from pygame.locals import *
print("Setup alarm time: ")
day = input("Day: ")
hour = input("Hour (24-hour time): ")
minute = input("Minute: ")
sec = "0"
print("Opening window...")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
a = True
b = True
c = True
q = False
while a:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            a = False
    if keyboard.is_pressed("q"):
        a = False
    if datetime.datetime.now().strftime("%d") == day and c:
        if datetime.datetime.now().strftime("%H") == hour:
            if datetime.datetime.now().strftime("%M") == minute:
                sbc.set_brightness(100)
                pygame.mixer.music.play()
                while b:
                    screen.fill((random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)))
                    pygame.display.update()
                    time.sleep(0.01)
                    if keyboard.is_pressed("q"):
                        b = False
                if not b:
                    c = False
                    q = True
    if q:
        pygame.quit()
        exit()
            
