from pygame import * 
 
# Define the GameSprite class 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
     
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
# Define the Player class 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 80: 
            self.rect.x += self.speed 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed 
 
# Define the Enemy class 
class Enemy(GameSprite): 
    direction = 'left' 
     
    def update(self): 
        if self.rect.x <= 470: 
            self.direction = 'right' 
        if self.rect.x >= win_width - 85: 
            self.direction = 'left' 
        if self.direction == 'left': 
            self.rect.x -= self.speed 
        else: 
            self.rect.x += self.speed 
 
# Game setup 
win_width = 700 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
display.set_caption('Maze') 
background = transform.scale(image.load('background.jpg'), (win_width, win_height)) 
 
# Game characters 
player = Player('hero.png', 5, win_height - 80, 4) 
monster = Enemy('cyborg.png', win_width - 80, 280, 2) 
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0) 
 
# Game variables 
game = True 
finish = False 
clock = time.Clock() 
FPS = 60 
 
# Music setup 
mixer.init() 
mixer.music.load('jungles.ogg') 
mixer.music.play() 
 
# Fonts for messages 
font.init() 
font = font.Font(None, 70) 
win_message = font.render('YOU WIN!', True, (255, 215, 0)) 
lose_message = font.render('GAME OVER', True, (255, 0, 0)) 
 
# Game loop 
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
 
    if not finish: 
        # Update background and sprites 
        window.blit(background, (0, 0)) 
        player.update() 
        monster.update() 
 
        # Draw sprites 
        player.reset() 
        monster.reset() 
        final.reset() 
 
        # Check for collision 
        if sprite.collide_rect(player, monster): 
            finish = True 
            window.blit(lose_message, (200, 200)) 
         
        if sprite.collide_rect(player, final): 
            finish = True 
            window.blit(win_message, (200, 200)) 
 
    else: 
        # Show end game message 
        display.update() 
        time.delay(2000) 
        game = False 
 
    display.update() 
    clock.tick(FPS)