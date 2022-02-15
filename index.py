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
test = 0
# 4. 메인 이벤트 
SB = 0
while SB==0:
  # 4-1. FPS 설정 
  clock.tick(2)
    # 4-2. 각종 입력 감지 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      SB = 1
  # 4-3. 입력, 시간에 따른 변화 
  test += 1
  if test%2==0:
    color = black
  else:
    color = white
  # 4-4. 그리기
  screen.fill(color)
  # 4-5. 렌더링 
  pygame.display.flip()
# 5. 게임 종료 
pygame.QUIT()
