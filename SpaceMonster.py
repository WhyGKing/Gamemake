import pygame
import random
import sys

# 함수선언문
# @기능 2-5 : 매개변수로 받은 객체를 화면에 그리는 함수를 선언한다.
def paintEntity(entity, x, y) :
    monitor.blit(entity, (int(x), int(y)))

def playGame():
    global monitor

    r = random.randrange(0,256)      # 255 + 1
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    # @기능 2-2 : 우주선의 초기 위치 키보드를 눌렀을 때 이동량을 저장할 변수를 선언한다.
    shipX = swidth / 2   # 우주선의 위치중에서 x좌표
    shipY = sheight * 0.8
    dx, dy = 0, 0  # 키보드 누를 때 우주선의 이동량

    # @기능 3-2 : 우주괴물을 랜덤하게 추출하고 크기와 위치를 설정한다.
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size                 # 우주괴물 크기
    monsterX = 0
    monsterY = random.randrange(0, int(swidth * 0.3)) # 상위 30% 위치까지만
    monsterSpeed = random.randrange(1, 5)


# 무한반복
    while True:
        (pygame.time.Clock()).tick(50)       # 루프에서 구동속도조절
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()


            # @기능 2-3 : 방향키에 따라 우주선이 움직이게 한다.
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = +5
                elif e.key == pygame.K_DOWN : dy = -5

            # @기능 2-3-1 : 이동을 멈추면 그 자리를 원점으로 삼기 위해 이동거리를 초기화화
            if e.type in [pygame.KEYUP] :
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0,0


         # @기능 2-4 : 우주선이 화면 안에서만 움직이게 한다.
        if(0 < shipX + dx and shipX + dx <= swidth - shipSize[0] \
                and sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]) :
            shipX += dx
            shipY -= dy
        # 우주선을 다시 화면에 표시해준다.
        paintEntity(ship, shipX, shipY)    # 우주선의 좌측이 기준임.

        # @기능 3-3 : 우주괴물이 자동으로 나타나 왼쪽에서 오른쪽으로 움직인다.
        monsterX += monsterSpeed

        if monsterX > swidth:
            monsterX = 0
            monsterY = random.randrange(0, int(swidth * 0.3))
            # 우주괴물 이미지를 무작위로 선택한다.
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1, 5)


        pygame.display.update()

    # end of while
# end of playGame()






## 여기서부터 프로그램 시작부입니다.




# 전역변수 선언
r,g,b = [0]*3     # 화면의 배경색: 0,0,0 ==> 검정색
swidth, sheight = 500, 700   # 화면의 크기
monitor = None    # 게임화면
ship, shipSize = None, 0

# @기능 3-1 : 랜덤하게 사용할 우주괴물의 이미지 10개를 준비한다.
monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', \
                'monster05.png', 'monster06.png', 'monster07.png', 'monster08.png', \
                'monster09.png', 'monster10.png']
monster = None   # 우주괴물

missile = None     # 미사일


# 메인코드부

# 게임 초기화
pygame.init()   # 게임초기화 코드
monitor = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("우주괴물게임")

# @기능 2-1 : 우주선 이미지를 준비하고 크기를 구한다.
ship = pygame.image.load('ship01.png')
shipSize = ship.get_rect().size





# 실제 게임 플레이
playGame()