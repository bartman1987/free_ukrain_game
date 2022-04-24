import pygame

class Putin(pygame.sprite.Sprite):
    """класс одного путина"""
    
    def __init__(self, screen):
        """инициализируем путина"""
        super(Putin, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/nft.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """перемещает путина"""
        self.y += 0.1
        self.rect.y = self.y