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
plane = pygame.image.load("./plane2.png").convert_alpha()
plane = pygame.transform.scale(plane, (80,80))
plane_size_x, plane_size_y = plane.get_size()
plane_x = round(size[0]/2-plane_size_x/2)
plane_y = round(size[1]-plane_size_y-15)

black = (0,0,0)
white = (255,255,255)
# 4. 메인 이벤트 
switch = 0
while switch==0:
  # 4-1. FPS 설정 
  clock.tick(60)
    # 4-2. 각종 입력 감지 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      switch = 1
  # 4-3. 입력, 시간에 따른 변화 
  # 4-4. 그리기
  screen.fill(black)
  screen.blit(plane, (plane_x,plane_y))
  
  # 4-5. 렌더링 
  pygame.display.flip()
# 5. 게임 종료 
pygame.QUIT()
