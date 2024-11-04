from pydantic import BaseModel, Field
from typing import Literal, List


### Scene
class Scene(BaseModel):
    scene_symbol: Literal["A", "B", "C", "D", "E"]
    scene_description: str
    scene_type: Literal['Iconic', 'Unexpected']

class Scenes(BaseModel):
    scenes: List[Scene]


### Persona
class Timeline(BaseModel):
    morning: str = Field(..., description="ペルソナの朝のタイムライン。平日と週末で変わる。")
    afternoon: str = Field(..., description="ペルソナの午後のタイムライン。平日と週末で変わる。")
    night: str = Field(..., description="ペルソナの夜のタイムライン。平日と週末で変わる。")
    class Config:
        extra = "forbid"  # This sets additionalProperties to false

class Persona(BaseModel):
    full_name: str = Field(..., description="ペルソナのフルネーム")
    age: int = Field(..., description="ペルソナの年齢")
    gender: str = Field(..., description="ペルソナの性別")
    occupation: str = Field(..., description="ペルソナの職業")
    income: str = Field(..., description="ペルソナの年収。500万円、というように具体的な金額と万円の単位で記載。")
    family_structure: str = Field(..., description="ペルソナの家族構成")
    location: str = Field(..., description="ペルソナの居住地")
    hometown: str = Field(..., description="ペルソナの出身地")
    lifestyle: str = Field(..., description="ペルソナのライフスタイル")
    interests: str = Field(..., description="ペルソナの興味・関心")
    how_to_collect_info: str = Field(..., description="ペルソナの情報収集方法。メディア、プラットフォーム、デバイス、ソーシャルメディアなどを記載。")
    weekday_timeline: Timeline = Field(..., description="ペルソナの平日のタイムライン")
    weekend_timeline: Timeline = Field(..., description="ペルソナの週末のタイムライン")
    love_categories: str = Field(..., description="ペルソナの好きなカテゴリやアイテム")
    trends_of_spending: str = Field(..., description="ペルソナの消費傾向")
    concrete_demands: str = Field(..., description="ペルソナの具体的な要求")
    concrete_pain: str = Field(..., description="ペルソナが商品に対して抱える具体的な痛み")
    category_value_1: str = Field(..., description="ペルソナが商品に求める具体的な商品イメージ。実在する商品であること。")
    category_value_2: str = Field(..., description="ペルソナの要求を現在満たしている商品や代替品。実在する商品であること。")
    class Config:
        extra = "forbid"  # This sets additionalProperties to false

class Personas(BaseModel):
    scene_symbol: Literal["A", "B", "C", "D", "E"] = Field(..., description="シーンのアルファベット。scene_symbolと同じアルファベットを記載。")
    persona_1: Persona = Field(..., description="シーンに基づくペルソナの1人目。")
    persona_2: Persona = Field(..., description="シーンに基づくペルソナの2人目。ペルソナ1人目とは異なるペルソナであること。")


### Idea
class CustomerExperienceSteps(BaseModel):
    step1: str = Field(..., description="顧客体験イメージのステップ1。100文字程度。")
    step2: str = Field(..., description="顧客体験イメージのステップ2。100文字程度。")
    step3: str = Field(..., description="顧客体験イメージのステップ3。100文字程度。")

class HitFactors(BaseModel):
    factor1: str = Field(..., description="ヒット要因1。50文字程度。")
    factor2: str = Field(..., description="ヒット要因2。50文字程度。")
    factor3: str = Field(..., description="ヒット要因3。50文字程度。")

class Idea(BaseModel):
    product_category: str = Field(..., description="商品のカテゴリー。[商品名] と同一にする。")
    new_product_name: str = Field(..., description="新商品の名前。商品の特徴を身近にある物や事に例えた名称にすること。")
    new_product_feature: str = Field(..., description="新商品の特徴・新しさ。商品の概要、ユニークネスな部分がわかるような文章を日本語100文字程度で作成。")
    new_product_point: str = Field(..., description="新商品のポイント。既存商品との違いを明確にするために「これまでの商品は〇〇〇〇だったがこの商品ではxxxxである」というフォーマットで記載。")
    new_product_spec: str = Field(..., description="新商品の仕様。容量、容器の種類、形状、成分などを記載。")
    new_product_function: str = Field(..., description="新商品の機能。簡潔に箇条書きで記載。")
    new_product_price: str = Field(..., description="新商品の価格。税抜き価格で記載、（税抜き）と表記。")
    # new_product_personas: Personas = Field(..., description="ペルソナ。ペルソナの名前・性別・年代とアルファベットを記載。")
    new_product_customer_experience: CustomerExperienceSteps = Field(..., description="新商品の顧客体験イメージ。商品のCMを作る想定でや{#新商品の特徴・新しさ}や{#新商品のポイント}が伝わるようなCMのシナリオとして3ステップで簡潔に表現。各ステップ100文字程度。")
    new_product_sales_channel: str = Field(..., description="新商品の販売チャネル。オンライン、オフライン問わず、箇条書きで固有名詞を入れて記載。")
    new_product_hit_factor: HitFactors = Field(..., description="新商品のヒット要因。市場に受け入れられた理由やムーブメント・話題になった理由を朝のニュース番組が新商品を紹介すると仮定して箇条書き・3点でまとめ。各ヒット要因は50文字程度。")


### Righteous Indignation
class RighteousIndignation(BaseModel):
    righteous_indignation: str = Field(..., description="[ペルソナ情報]が抱える義憤")


### Appeal Method
class Benefit(BaseModel):
    benefit_type: Literal["機能価値", "情緒価値"] = Field(..., description="新商品が消費者に提供する「機能価値」と「情緒価値」のどちらかを選択。")
    benefit_description: str = Field(..., description="新商品が消費者に提供する「機能価値」と「情緒価値」のどちらかを50字程度で記載。")

class Benefits(BaseModel):
    benefits: List[Benefit] = Field(..., description="新商品が消費者に提供する「機能価値」と「情緒価値」の2つをどちらも作成。それぞれ、その価値についての説明を50字程度で記載。")

class ReasonToBelieve(BaseModel):
    rtb_type: Literal["機能価値", "情緒価値"] = Field(..., description="新商品が消費者に提供する「機能価値」と「情緒価値」のどちらかを選択。")
    rtb_description: str = Field(..., description="消費者がその商品を信頼するに足る理由や根拠」のこと。「機能価値」と「情緒価値」それぞれのReasonToBelieveについて50字程度で記載。")

class ReasonToBeliefs(BaseModel):
    reason_to_beliefs: List[ReasonToBelieve] = Field(..., description="「消費者がその商品を信頼するに足る理由や根拠」のこと。「機能価値」と「情緒価値」の2つをどちらも作成。それぞれ、その価値についての説明を50字程度で記載。")

class AppealMethod(BaseModel):
    usp: str = Field(..., description="Unique Selling Proposition（＝「自社だけが、顧客に提供を約束できる価値」）のこと。50字程度で記載。")
    benefits: Benefits = Field(..., description="新商品が消費者に提供する「機能価値」と「情緒価値」のどちらかを選択し、その価値についての説明を50字程度で記載。")
    reason_to_believe: ReasonToBeliefs = Field(..., description="「消費者がその商品を信頼するに足る理由や根拠」のこと。「機能価値」と「情緒価値」それぞれのReasonToBelieveについて50字程度で記載。")
    what_to_say: str = Field(..., description="新商品の訴求として消費者に伝えるべきことを50字程度で記載。")
    how_to_say: List[str] = Field(..., description="新商品の{#What to say}をどのように表現して訴求するべきかを箇条書きで記載。")
    appeal_phrase: str = Field(..., description="{#What to say}と{#How to say}を踏まえて、中学生でもわかるような一般的な言葉で考案。")


