import pygame
import time

class Display: #Cet héritage n'apporte pas grand chose ici, je trouve juste ça plus propre car si on voulait ajouter de nouvelles fonctionalitées aux modes d'affichages, on pourrait en avoir besoin
    def aff_config(self,config):
        pass
    def aff_message(self,message):
        pass
    def aff_error(self,message):
        print('\033[91m'+str(message)+'\033[0m')

class Terminal(Display):
    """ Terminal display """
    def __init__(self,size):
        pass
    def aff_config(self,config):
        print('\033[92m'+str(config)+'\033[0m')
    def aff_message(self,message):
        print(message)
    def destroy(self):
        pass
    def aff_loop(self):
        pass

DISPLAY_TIME = 0 #The number of sec a configuration will be displayed
MSG_TIME = 1
class Window(Display):
    """ Display in a pygame window """
    def __init__(self,size,display_time,msg_time):
        self.__size = size
        self.display_time = display_time
        self.msg_time = msg_time
        pygame.init()
        pygame.display.set_caption("Queens")
        self.__width = size*32
        self.__height = size*32
        self.__screen = pygame.display.set_mode((self.__width,self.__height))
        for i in range(size):
            for j in range(size):
                pygame.draw.rect(self.__screen, (0,0,255), (i*32,j*32,32,32))
        self.__font = pygame.font.Font('freesansbold.ttf',18)

    def reset_screen(self):
        for i in range(self.__size):
            for j in range(self.__size):
                pygame.draw.rect(self.__screen, (0,0,255), (i*32,j*32,32,32))
                
    def aff_config(self,config):
        self.reset_screen()
        for i,j in enumerate(config):
            pygame.draw.rect(self.__screen, (255,0,0), (i*32,j*32,32,32))
        pygame.display.flip()
        time.sleep(self.display_time)
        
    def aff_message(self,message):
        text = self.__font.render(message,True,(255,255,255))
        textrect = text.get_rect()
        textrect.center = (self.__width//2,self.__height//6)
        self.__screen.blit(text,textrect)
        pygame.display.update()
        time.sleep(self.msg_time)
        
    def destroy(self):
        pygame.quit()

    def aff_loop(self):
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    continuer = False
        self.destroy()
