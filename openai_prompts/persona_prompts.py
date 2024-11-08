persona_system_prompt = """
現在、あなたは、{#役割}として、{#状況}にアサインされている。
これから指示する{#タスク}は非常に詳細かつ複雑であり、大量の情報を一度に扱う必要がありますが、{#タスク}を分割せずに一度に実行してください。

#役割
電通、博報堂、ADK等日本の広告代理店におけるトップマーケター

#状況
日本企業の新商品開発プロジェクト

# 出力言語
日本語
"""

persona_user_prompt = f"""
#タスク
シーン: [直前の出力] に基づいて、対応する消費者のペルソナを2人考える。

#ペルソナ
マーケティングにおけるペルソナ

#ルール
・年齢を10代から100歳まで幅広く出すこと
・性別は男女、LGPTQ問わず幅広く出すこと
・職業は無職やリタイア、学生、主婦、ブルーカラーやホワイトカラーなど絶対に偏りなく幅広く出すこと
・居住地は日本全国47都道府県から絶対に偏ることなく、都市部から地方まで津々浦々で考えること
・年収は0円から1000万以上まで幅広く出すこと

## 注意事項1
各出力ごと最低日本語400字以上で具体的かつ詳細に考える。具体的なブランド名や商品名、固有名詞を挙げる。例えば、普段利用する商品やどんな人物をフォローしているか考える。

## 注意事項2
具体的なブランド名や商品名、固有名詞を挙げること。 例えば、「エナジードンクのレッドブルを飲む」や、「日焼け止めのアクアリッチ瞬間ミストUVを使う」のように考える。
ただし、価値1、価値2の商品は必ず世の中に存在している商品名を利用すること。

## 注意事項3
[他のコンテンツ]データがある場合には、[他のコンテンツ]との重複を避けて出力すること。

#出力における注意
出力は、必ず日本語で出力すること。
"""