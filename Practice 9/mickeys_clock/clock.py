import pygame
import sys #program quit
from datetime import datetime #time

class Clock:
    def __init__(self):
        pygame.init() #initializing

        self.WIDTH = 500
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) #setting screen
        pygame.display.set_caption("Mickey Clock")

        self.bg = pygame.image.load("images/background.png")
        self.minute_hand = pygame.image.load("images/minute.png")
        self.second_hand = pygame.image.load("images/second.png")

        self.center = (self.WIDTH // 2, self.HEIGHT // 2) #screen center

        self.clock = pygame.time.Clock() #fps

    def rotate(self, image, angle): #rotate hands
        rotated_image = pygame.transform.rotozoom(image, -angle, 1) #-angle чтоб вращалось по часвоой стрелке
        rect = rotated_image.get_rect(center=self.center) #center hands
        return rotated_image, rect

    def get_time_angles(self):
        now = datetime.now() 

        minute = now.minute
        second = now.second + now.microsecond / 1_000_000 

        minute_angle = (minute + second / 60) * 6 
        second_angle = second * 6 

        return minute_angle, second_angle

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 

            self.screen.fill((0, 0, 0)) #clear bg
            self.screen.blit(self.bg, (0, 0)) #drawing bg

            minute_angle, second_angle = self.get_time_angles() #getting angles

            min_img, min_rect = self.rotate(self.minute_hand, minute_angle) 
            sec_img, sec_rect = self.rotate(self.second_hand, second_angle) #rotating using angles
            #minimg- already rotated image, minrect - where to place 

            self.screen.blit(min_img, min_rect)
            self.screen.blit(sec_img, sec_rect) 
            #first draw bg then minute strelka then second strelka

            pygame.display.flip() #updatin
            self.clock.tick(60) #plavnost