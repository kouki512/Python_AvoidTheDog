
from pse2pgzrun import * 
import random
import time
WIDTH = 800
HEIGHT = 600
# モード
PREPLAY,INPLAY,POSTPLAY,CLEAR = range(4)
mode = PREPLAY
# プレイヤー管理
NORMAL,JUMP,FALL = range(3)
MAN_STATUS = NORMAL
vx = 0
# プレイヤーのジャンプの挙動
JUMP_POWER = 40
GRAVITY = 2
MAX_FALL = 20
move_jump = 0
# 犬の動き
MOVE_LEFT,MOVE_RIGHT = range(2)
DOG_STATUS = MOVE_LEFT
toneHardCrash = tone.create('A1',0.02)
# 難易度
level = {'easy': 4, 'normal':3, 'hard':2}
play_level = 100
# 時間の計測(初期化)
start_time = time.time()
elapsed_time = 0
# ハイスコアの管理
high_score = 0
score_updated = 0


class Man(Actor):
    def __init__(self,name,x,y):
        super().__init__(name,center=(x,y))
        self.vx = 0
    def update(self,dt):
        self.x += self.vx * dt
        # ウィンドウの先へ行かないようにする
        if self.right > WIDTH:
            self.right = WIDTH
            self.vx = 0
        if self.left < 0:
            self.left = 0    
            self.vx = 0      
        # プレイヤーの移動 
        if keyboard.right:
            self.vx += 20
        if keyboard.left:
            self.vx -= 20
        if keyboard.down:
            self.vx = 0

class Dog(Actor):
    def __init__(self,name,x,y):
        super().__init__(name,center=(x,y))
        self.vx = 0
    def update(self,dt,DOG_STATUS):
        self.x += self.vx * dt
        # 犬がウィンドウの外へ行かないようにする
        if self.right > WIDTH:
            self.right = WIDTH
            self.vx = 0
            DOG_STATUS = MOVE_LEFT
        if self.left < 0:
            self.left = 0    
            self.vx = 0  
            DOG_STATUS = MOVE_RIGHT
man = Man('man',400,500)
dog = Dog('dog',200,500)

def start():
    global mode
    mode = PREPLAY
    
def on_key_down(key):
    global MAN_STATUS
    # 地面についていたらジャンプ
    if (key == keys.SPACE) and (MAN_STATUS == NORMAL):
        MAN_STATUS = JUMP

def draw():
    global mode, elapsed_time,high_score,score_updated
    # 背景画像の設定
    screen.clear()
    screen.fill((128, 128, 128))
    screen.blit("bg-ground",(0,500))
    screen.blit("bg-sand",(0,550))
    screen.blit("bg-sky",(0,0))

    # スタート画面の描画
    if mode == PREPLAY:
        screen.blit("man",(680,50))
        screen.blit("dog",(25,50))
        score_updated = 0
        screen.draw.text(
            'Avoid The Dog',
            center=(400,100), fontsize=100, color='orange')
        screen.draw.text(
            'Easy => A',
            center=(250,280), fontsize=50, color='magenta')
        screen.draw.text(
            'Normal => W',
            center=(400,200), fontsize=50, color='magenta')
        screen.draw.text(
            'Hard => D',
            center=(550,280), fontsize=50, color='magenta')
    # プレイ中の描画   
    elif mode == INPLAY:
        man.draw()
        dog.draw()
        # スコア（タイム）の計算
        # 現在時刻-開始時刻で計算
        elapsed_time = int(time.time() - start_time)
        screen.draw.text(
            "Avoid the dogs",left=300,top=15,fontsize=40,color= 'black')
        screen.draw.text(
            "times: " + str(elapsed_time) + " s",left=300,top=40,fontsize=40,color= 'black')
    # リザルト画面の描画
    else:
        if high_score < elapsed_time:
            high_score = elapsed_time
            score_updated = 1
        if score_updated == 1:
            screen.draw.text(
            'High Score is updated!! ',
            center=(400,250),fontsize=40,color="orange")     
            
        screen.draw.text(
            'GAME OVER',       
            center=(400,320),fontsize=100,color="red")
        screen.draw.text(
            'SCORE: ' + str(elapsed_time)+ ' seconds',
            center=(400,120),fontsize=80,color="blue")
        screen.draw.text(
            'HIGH SCORE: ' + str(high_score)+ ' seconds',
            center=(400,190),fontsize=50,color="blue")
        screen.draw.text(
            'Easy => A',
            center=(250,450), fontsize=50, color='magenta')
        screen.draw.text(
            'Normal => W',
            center=(400,400), fontsize=50, color='magenta')
        screen.draw.text(
            'Hard => D',
            center=(550,450), fontsize=50, color='magenta')


def update(dt):
    global MAN_STATUS,JUMP_POWER,GRAVITY,MAX_FALL,move_jump,mode,DOG_STATUS,start_time,play_level,elapsed_time
    # ゲームスタート難易度
    if mode == PREPLAY:
        if keyboard.a: # easy
            start_time = time.time()
            play_level = level['easy']
            mode = INPLAY
        if keyboard.w:# normal
            start_time = time.time()
            play_level = level['normal']
            mode = INPLAY
        if keyboard.d:# hard
            start_time = time.time()
            play_level = level['hard']
            mode = INPLAY

    elif mode == POSTPLAY:
        # ゲームを初期化
        start_time = 0
        man.x = 400
        man.vx = 0
        dog.x = 0
        dog.vx = 0
        if keyboard.escape:
            exit()
        elif keyboard.a:
            start()
            play_level = level['easy']
        elif keyboard.w:
            start()
            play_level = level['normal']
        elif keyboard.d:
            start()
            play_level = level['hard']
    else:        
        man.update(dt)
        if MAN_STATUS == JUMP:
            man.y -= (JUMP_POWER - move_jump)
            if move_jump >= JUMP_POWER:
                MAN_STATUS = FALL
                move_jump = 0
            else:
                move_jump += GRAVITY
        if MAN_STATUS == FALL:
            if MAX_FALL > move_jump:
                move_jump += GRAVITY
            while man.y < 500:
                man.y += move_jump   
                MAN_STATUS = NORMAL

        dog.update(dt,DOG_STATUS)
        dog_x = random.randint(1,600) # 動く量の設定
            
        if DOG_STATUS == MOVE_RIGHT: # 犬が右に進む
            dog.vx += dog_x / play_level # レベルに応じた速度
            DOG_STATUS = MOVE_LEFT # 左に方向転換
        else:
            dog.vx -= dog_x / play_level
            DOG_STATUS = MOVE_RIGHT # 右に方向転換

        if man.colliderect(dog):
            # 衝突判定（ゲームオーバー）
            mode = POSTPLAY
            toneHardCrash.play()
    

start()
pgzrun.go()