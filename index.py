import pygame

# 1. pygame 초기화 
pygame.init()
# 2. 게임창 설정
size = [400,800]
screen = pygame.display.set_mode(size)
title = "Plane Shooting"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

class Game_obj:
  def __init__(self):
    self.x = 0 #좌표
    self.y = 0
    self.move = 0
  def put_img(self, path):
    if path[-3:]=="png":
      self.img = pygame.image.load(path).convert_alpha()
    else:
      self.img = pygame.image.load(path)
    self.size_x, self.size_y = self.img.get_size()
  def change_size(self, new_size_x, new_size_y):
    self.img = pygame.transform.scale(self.img, (new_size_x,new_size_y))
    self.size_x, self.size_y = self.img.get_size()
  def show(self):
    screen.blit(self.img, (self.x, self.y))

plane = Game_obj()
plane.put_img("./images/plane1.png")
plane.change_size(70,70)
plane.x = round(size[0]/2-plane.size_x/2)
plane.y = round(size[1]-plane.size_y-15)
plane.move = 5

move_right=False
move_left=False
missile_on = False

missile_list = []

def create_missile():
  missile = Game_obj()
  missile.put_img("./images/missile.png")
  missile.change_size(12,20)
  missile.x = round(plane.x + plane.size_x/2-missile.size_x/2)
  missile.y = plane.y-missile.size_y-3
  missile.move = 8
  missile_list.append(missile)

# 4. 메인 이벤트 
shut_down = 0
while shut_down==0:
  # 4-1. FPS 설정 
  clock.tick(60)
    # 4-2. 각종 입력 감지 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      shut_down = 1
    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_RIGHT: #1073741903
        move_right=True
      elif event.key ==1073741904: #1073741904
        move_left=True
      elif event.key == pygame.K_SPACE: #missile on
        print("down")
        create_missile()

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        move_right = False
      elif event.key ==pygame.K_LEFT:
        move_left = False
      elif event.key == pygame.K_SPACE:
        print("up")
        missile_on=False
    
  # 4-3. 입력, 시간에 따른 변화 
  if move_right==True:
    plane.x =plane.x+plane.move
    if plane.x>size[0]-plane.size_x:
      plane.x = size[0]-plane.size_x
  elif move_left==True:
    plane.x = plane.x-plane.move
    if plane.x<0:
      plane.x = 0

  # 4-4. 그리기
  screen.fill(black)
  plane.show()
  for item in missile_list:
    item.y = item.y-item.move
    item.show()
    print(item.y)
    if item.y<0:
      print("사라짐")
      missile_list.remove(item)
      print(item)
      print(len(missile_list))

 
  
  


  
  # 4-5. 렌더링 
  pygame.display.flip()
# 5. 게임 종료 
pygame.quit()
