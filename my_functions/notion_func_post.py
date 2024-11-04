import time

### --- Create a new Page onto Notion --- ###
# Sample for creating a new page onto Notion DB
def add_row_to_notion_database(client, database_id):
    response = client.pages.create(
        **{
            "parent": { "database_id": database_id },
            # Define the properties of the new page
            "properties": {
                "Title": {
                    "title": [
                        {
                            "text": {
                                "content": "yyyyMMddHHmmss"
                            }
                        }
                    ]
                },
            },  # end properties
        }
    )

    print("notion database create completed")
    print(response) # 追加した内容を表示する


# Create a new Persona page onto Persona DB
def create_persona_on_persona_db(client, persona_database_id, persona_object):
    """
    Create a new Persona page onto Persona DB
    """

    # Unpack the persona info
    full_name = persona_object.full_name
    age = int(persona_object.age)
    gender = persona_object.gender
    occupation = persona_object.occupation
    income = persona_object.income
    family_structure = persona_object.family_structure
    location = persona_object.location
    hometown = persona_object.hometown
    lifestyle = persona_object.lifestyle
    interest = persona_object.interests
    how_to_collect_info = persona_object.how_to_collect_info
    weekday_timeline_morning = persona_object.weekday_timeline.morning
    weekday_timeline_afternoon = persona_object.weekday_timeline.afternoon
    weekday_timeline_night = persona_object.weekday_timeline.night
    weekend_timeline_morning = persona_object.weekend_timeline.morning
    weekend_timeline_afternoon = persona_object.weekend_timeline.afternoon
    weekend_timeline_night = persona_object.weekend_timeline.night
    love_categories = persona_object.love_categories
    trends_of_spending = persona_object.trends_of_spending
    concrete_demands = persona_object.concrete_demands
    concrete_pain = persona_object.concrete_pain
    category_value_1 = persona_object.category_value_1
    category_value_2 = persona_object.category_value_2

    response = client.pages.create(
        # Create a new Persona page on Notion DB
        **{
            "parent": { "database_id": persona_database_id },
            # Define the properties of the new page
            "properties": {
                "ペルソナ名": {
                    "title": [
                        {
                            "text": {
                                "content": full_name
                            }
                        }
                    ]
                },
                "年齢": {
                    "id": "_%7BFs",
                    "type": "number",
                    "number": age
                },
                "性別": {
                    'id': 'Vj%5EQ',
                    "rich_text":
                            [{
                            "type": "text",
                            "text": {
                                "content": gender
                            }
                            }]
                },
                "職業": {
                    'id': '%3CgbW', 'rich_text': [{'type': 'text', 'text': {'content': occupation}}]
                },
                "年収": {
                    'id': 'Fej%40',
                    'rich_text': [{'type': 'text', 'text': {'content': income}}]
                },
                "家族構成":{
                    'id': 'Mh%7De',
                    'rich_text': [{'type': 'text', 'text': {'content': family_structure}}]
                },
                '居住地': {'id': 'FTme', 'rich_text': [{'type': 'text', 'text': {'content': location}}]},
                '出身地': {'id': '%60%3D%7DV',
                        'rich_text': [{'type': 'text', 'text': {'content': hometown}}]},
                'ライフスタイル': {'id': 'h~%7Co',
                            'rich_text': [{'type': 'text', 'text': {'content': lifestyle}}]},
                '興味・関心': {'id': 'aqn%3E', 'rich_text': [{'type': 'text', 'text': {'content': interest}}]},
                '情報収集の方法': {'id': 'Obsa', 'rich_text': [{'type': 'text', 'text': {'content': how_to_collect_info}}]},
                '平日の過ごし方: 朝': {'id': 'lN%3Fu',
                               'rich_text': [{'type': 'text', 'text': {'content': weekday_timeline_morning}}]},
                '平日の過ごし方: 昼': {'id': 'Vlg%3B',
                               'rich_text': [{'type': 'text', 'text': {'content': weekday_timeline_afternoon}}]},
                '平日の過ごし方: 夜': {'id': 'c%40%7Cq',
                               'rich_text': [{'type': 'text', 'text': {'content': weekday_timeline_night}}]},
                '休日の過ごし方: 朝': {'id': 'lN%3Fu',
                                  'rich_text': [{'type': 'text', 'text': {'content': weekend_timeline_morning}}]},
                '休日の過ごし方: 昼': {'id': 'Vlg%3B',
                               'rich_text': [{'type': 'text', 'text': {'content': weekend_timeline_afternoon}}]},
                 '休日の過ごし方: 夜': {'id': 'TGQd',
                               'rich_text': [{'type': 'text', 'text': {'content': weekend_timeline_night}}]},
                '好きなカテゴリ': {'id': '%40zjw',
                            'rich_text': [{'type': 'text', 'text': {'content': love_categories}}]},
                '過ごし方トレンド': {'id': '%3D%5DCq',
                             'rich_text': [{'type': 'text', 'text': {'content': trends_of_spending}}]},
                '具体的なニーズ': {'id': 'f~nO', 'rich_text': [{'type': 'text', 'text': {'content': concrete_demands}}]},
                '具体的な痛み': {'id': '%3FEbR',
                           'rich_text': [{'type': 'text', 'text': {'content': concrete_pain}}]},
                'カテゴリ価値1': {'id': 'hy%60F',
                            'rich_text': [{'type': 'text', 'text': {'content': category_value_1}}]},
                'カテゴリ価値2': {'id': 'YD%3EI',
                            'rich_text': [{'type': 'text', 'text': {'content': category_value_2}}]}
            }
        }
    )

    print("notion database create completed")
    return response


# Create a new Idea page onto Idea DB
def create_idea_on_idea_db(client, idea_database_id, content: dict, idea_version_number: int):
    """
    Create a new Idea page onto Idea DB.
    Args:
        *content (dict): The content dictionary.
        idea_version (int): The version of the idea. 1, 2, or 3.
    """

    # Check and set the idea version
    if idea_version_number == 1:
        idea_version_name = "V1"
    elif idea_version_number == 2:
        idea_version_name = "V2"
    elif idea_version_number == 3:
        idea_version_name = "V3"
    else:
        raise ValueError(f"Invalid idea version number: {idea_version_number}")


    ## Unpack the content_dict
    # Extract the idea object from the content_dict
    idea_object = content[f"idea_v{idea_version_number}"]
    # Extract the righteous_indignation from the idea_object
    righteous_indignation_object = content["righteous_indignation"]
    # Extract the appeal_method from the content_dict
    appeal_method_object = content["appeal_method"]

    # Get the idea name
    idea_name = idea_object.new_product_name
    # Set the format for the idea_abstract
    idea_dict = dict(idea_object)
    idea_abstract = ""
    for key, value in idea_dict.items():
        # Skip the new_product_name and product_category
        if not key in ["new_product_name", "product_category"]:
            idea_abstract += f"{key}: {value}\n"

    # Set the righteous_indignation
    righteous_indignation = righteous_indignation_object.righteous_indignation

    # Set the appeal_method
    ##### Need get pretty print later
    appeal_method = str(appeal_method_object)


    response = client.pages.create(
        **{
            "parent": { "database_id": idea_database_id },
            "properties": {
                "アイデア名": {
                    "title": [
                        {
                            "text": {
                                "content": idea_name
                            }
                        }
                    ]
                },
                "アイデアVersion": {
                    "select": {
                        "name": idea_version_name
                    }
                },
                'PersonaDB': {
                    'has_more': False,
                    'id': 'FKgQ',
                    'relation': [],
                    'type': 'relation'
                },
                'アイデアが解決する義憤': {
                    'id': 'Kkjx',
                    'rich_text': [
                        {
                            "type": "text",
                            "text": {
                                "content": righteous_indignation
                            }
                        }
                    ],
                    'type': 'rich_text'
                },
                'アイデア概要': {
                    'id': '_Rm%40',
                    'rich_text': [{'type': 'text', 'text': {'content': idea_abstract}}],
                    'type': 'rich_text'
                },
                '中分類DB': {
                    'has_more': False,
                    'id': '%3BP%60R',
                    'relation': [],
                    'type': 'relation'
                },
                '国・地域DB': {
                    'has_more': False,
                    'id': 'Y%3BKW',
                    'relation': [],
                    'type': 'relation'
                },
                '大分類（業界タグ）': {
                    'has_more': False,
                    'id': 'LOnV',
                    'relation': [
                    ],
                    'type': 'relation'
                },
                '訴求メッセージ': {
                    'id': 'e~rq',
                    'rich_text': [
                        {
                            "type": "text",
                            "text": {
                                "content": appeal_method
                            }
                        }
                    ],
                    'type': 'rich_text'
                }
            }
        }
    )

    return response