import pygame, requests
import pygame.image
import io
import sys
from urllib.request import urlopen, Request
import time
imageurl = "https://www.inspirobot.me/api?generate=true"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

refreshrate = 60.0 # set this to how long you want the quote to stay (in seconds)

def a():
    req1 = requests.get(imageurl, params=hdr)
    imgurl = req1.content
    req2 = requests.get(imgurl, params=hdr)
    img = io.BytesIO(req2.content)
    gameDisplay = pygame.display.set_mode((640, 640), pygame.FULLSCREEN)
    pygame.display.set_caption('AI Generated Quote')
    bg = pygame.image.load(img)
    gameDisplay.blit(bg, (0, 0))
    pygame.display.flip()
running = True
a()
keys = pygame.key.get_pressed()
timing = time.time()
while running:
    if time.time() - timing > refreshrate:
        timing = time.time()
        a()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
        running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()
