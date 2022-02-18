# 遊び方
* 内容
    * 突進してくる犬をジャンプで避け続け、その持続記録を競うゲームである。
* ルール
    * ランダムに動く犬をジャンプで避ける
    * 避けた時間がスコアとなる。
    * 最高記録はハイスコアとして保存される。自己ベスト更新を狙おう。
* 操作方法
    * ゲーム前
        * Aキー：Easyモードでスタート
        * Wキー：Normalモードでスタート
        * Dキー：Hardモードでスタート
    * ゲーム中
        * ←キー： プレイヤーを左へ移動
        * →キー： プレイヤーを右へ移動
        * スペースキー：プレイヤーがジャンプする。
    * ゲーム後
        * Aキー：Easyモードで再スタート
        * Wキー：Normalモードで再スタート
        * Dキー：Hardモードで再スタート
        * Escキー：プログラム終了
## プログラム内で作成しているクラスの説明
* Man
    * プレイヤーを表現するクラス
    * Pygame ZeroのActorクラスを継承
* Dog
    * 犬を表現するクラス
    * Pygame ZeroのActorクラスを継承
## 工夫した点・評価してもらいたい点
* 犬の動きを乱数で決定することで、急発進や、急旋回など予測できない動きを表現した点。
* プレイヤーの状態を”通常”、”ジャンプ”、”降下時”の3つに分類することで二段ジャンプなどの不具合を解消した点。
* ジャンプする力や、重力、最大降下量を定義することでジャンプの質を向上させた点
* ジャンプの力を調整することで少し助走をつけなければ犬を超えられないようにした点
⇒ 犬を飛び越えるべきか逃げるべきかという駆け引きが生まれた。
* 犬の速度を連想配列を使用し変化できるようにしたことで、難易度設定を容易にした点。
* ハイスコアを更新した際には、更新したことを告げるメッセージが表示されるようにした点。
## 基にした・参考にしたプログラムとその利用方法
* 12/7のkadai03.py
    * プレイヤー及び、犬の移動方法、モード切り替え、衝突判定の参考にした。
* 12/14のsample06.py
    * クラスの定義、コンストラクタの呼び出しの参考にした。
 
* 【Pygame zero】ジャンプ処理と落下処理を実装してみた https://yukiusagipcblog.com/archives/297
 
    *  ジャンプ処理の参考にした。
## 画像や音のデータの入手方法・作成方法
* man.png
    * いらすとやの臆病な人のイラスト（男性）を78＊132 px に縮小し名称を変更した。
* dog.png
    * いらすとやの秋田犬のイラストを79＊94 px に縮小し名称を変更した。
* bg-ground.png
    * https://kenney.nl/assets/pixel-platformer に含まれる tile_0038.pngを800＊100 pxに拡大し、名称を変更した。
* bg-sand.png
    * https://kenney.nl/assets/pixel-platformer に含まれる tile_0004.pngを800*50 px に拡大し、名称を変更した。
* bg-sky.png
    * https://kenney.nl/assets/pixel-platformer に含まれる background_0000.pngを800*500 px に拡大し、名称を変更した。