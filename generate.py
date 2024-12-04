import streamlit as st
import time

# ### --- Import for Notion --- ###
# from notion_client import Client

# # Import My functions for Notion
# from my_functions.notion_func_get import get_all_pages_info_from_db_id, get_page_info_from_its_page_id
# from my_functions.notion_func_update import update_scenes_on_nano_db
# from my_functions.notion_func_post import create_persona_on_persona_db, create_idea_on_idea_db

# ## If run on local, load the environment variables
# # Load Environment Variables
# from dotenv import load_dotenv
# load_dotenv(override=True)

# --- End of Import for Notion --- #

### --- Import for OpenAI Generation --- ###
from openai import OpenAI

# # Import Schema for OpenAI generation outputs
# from my_functions.openai_structured_schema import Scenes, Personas, Idea, RighteousIndignation, AppealMethod

# # Import My functions for OpenAI generation
# from my_functions.openai_func import generate_contents

### --- End of Import for OpenAI --- ###

### --- Streamlit Settings and Session State --- ###
# # Import My functions for Streamlit
# from my_functions.streamlit_util_func import read_json_file
# # Import My functions for Session State
# from my_functions.session_state_st import initialize_session_state, load_default_values, clear_session_state_for_overwrite_confirmation

# Set the page config
st.set_page_config(
    page_title="コンテンツ生成",
    page_icon="🚀")

# ## Initialize Session State
# # Load Default Values
# default_values = load_default_values()
# # Initialize Session State
# initialize_session_state(default_values)
# # Clear Session State for Confirmation
# clear_session_state_for_overwrite_confirmation()
# ### --- End of Streamlit Settings and Session State --- ###


## Set API Clients
# OpenAI client
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Notion client
# notion_client = Client(auth=st.secrets["NOTION_TOKEN"])


## Settings for OpenAI
# Set the model for OpenAI
model = "gpt-4o-mini"
# Set the delay time for the OpenAI API when generating contents
delay_time = 0.2
# Initialize the usage_dict for the generation
usage_dict = {
    'scene_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'persona_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'idea_v1_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'idea_v2_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'idea_v3_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'righteous_indignation_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'appeal_method_step': {'completion_tokens': 0, 'prompt_tokens': 0, 'total_tokens': 0},
    'completion_tokens_sum': 0,
    'prompt_tokens_sum': 0,
    'total_tokens_sum': 0
}

st.write("## Hello, world!")

if st.button("Send Request"):
    response = openapi_client(model="gpt-4o-mini", messages={"role": "user", "content": "Hello, world!"})
    st.write(response)

# ## Define Database IDs as constants: Notion DB IDs
# # Subclass DB ID: 細分類DB_ID
# SUBCLASS_DB_ID = st.secrets["SUBCLASS_DB_ID"]
# # Persona DB ID
# PERSONA_DB_ID = st.secrets["PERSONA_DB_ID"]
# # Idea DB ID
# IDEA_DB_ID = st.secrets["IDEA_DB_ID"]


# # Get the subclass pages info
# # 後でフィルタをかけたうえで取得に改修（「生成済」カラムにチェックが入っていないページのみ取得_）
# # subclass_pages_info = get_all_pages_info_from_db_id(notion_client, SUBCLASS_DB_ID)

# ## Store the subclass ids and titles （細分類）
# # Structure of subclass_ids_and_titles: 
# # [{"id": "subclass-page-id", "title": "subclass-page-title"}, ...]
# subclass_ids_and_titles = []
# # Get the subclass ids and titles
# for subclass_page_info in subclass_pages_info:
#     try:
#         subclass_title = subclass_page_info["properties"]["細分類名"]["title"][0]["text"]["content"]
#     except:
#         subclass_title = "No Title"

#     subclass_ids_and_titles.append({"id": subclass_page_info["id"], "title": subclass_title})


# ### --- Streamlit --- ###
# # Title on Streamlit
# st.write("## 商品カテゴリに基づくコンテンツ生成")
# st.write("")

# # Select Subclass by the user
# selected_subclass_id = None
# selected_subclass_title = st.selectbox(
#     label="細分類を選択してください。", 
#     options=[subclass["title"] for subclass in subclass_ids_and_titles],
#     index=None
# )
# # Get the selected subclass info
# if selected_subclass_title is not None:
#     selected_subclass = None
#     for subclass in subclass_ids_and_titles:
#         if subclass["title"] == selected_subclass_title:
#             selected_subclass = subclass
#             break
#     selected_subclass_id = selected_subclass["id"]

# if selected_subclass_id is not None:
#     st.write(f"選択中: {selected_subclass_title}")


# ### --- Generate Contents --- ###
# if selected_subclass_id is not None and st.button("生成"):
#     # Check if the category_names is not empty
#     if selected_subclass_title == "No Title" or selected_subclass_title == "" or selected_subclass_title == None:
#         st.error("タイトル名称のある細分類を選択してください。")
#     else:
#         ### Trace Settings for Generation
#         # Start Time Tracking
#         start_time = time.time()

#         # Retrieve the Related Classes from the selected Subclass
#         if selected_subclass_id is not None:
#             # Get the related miniclass pages
#             related_miniclass_pages = []
#             for subclass_page_info in subclass_pages_info:
#                 if subclass_page_info["id"] == selected_subclass_id:
#                     related_miniclass_pages = subclass_page_info["properties"]["ミニ分類DB"]["relation"]
#                     break

#             ## Get the related MiniClass pages titles from the related MiniClass pages ids
#             related_miniclass_pages_info = []
#             with st.spinner(f"{selected_subclass_title}に関連するミニ分類のタイトルを取得中..."):
#                 for related_miniclass_page in related_miniclass_pages:
#                     # Retrieve the miniclass page info based on the related miniclass page id
#                     response = get_page_info_from_its_page_id(notion_client, related_miniclass_page['id'])
#                     time.sleep(0.2)
                    
#                     # Try to extract related miniclass page title
#                     try: 
#                         related_miniclass_page_title = response["properties"]["ミニ分類名"]["title"][0]["text"]["content"]
#                     except:
#                         related_miniclass_page_title = "No Title"
#                     related_miniclass_pages_info.append({"id": related_miniclass_page["id"], "title": related_miniclass_page_title})

#                 # Display the related miniclass titles
#                 st.write(f"#### {selected_subclass_title}に関連するミニ分類のタイトル:")
#                 for related_miniclass_page_info in related_miniclass_pages_info:
#                     st.write(f"* {related_miniclass_page_info['title']}")
#                 st.write("")


#             ## Get the related NanoClass
#             with st.spinner(f"{selected_subclass_title}に関連するナノ分類のタイトルを取得中..."):
#                 related_nanoclass_pages_info = []
#                 for related_miniclass_page_info in related_miniclass_pages_info:
#                     # Retrieve the NanoClass page info based on the related MiniClass page id
#                     miniclass_info = get_page_info_from_its_page_id(notion_client, related_miniclass_page_info['id'])
#                     time.sleep(0.2)
                    
#                     # Try to Extract the NanoClass page IDs from response: Response is MiniClass page info
#                     try:
#                         related_nanoclass_page_ids_info = miniclass_info['properties']['ナノ分類DB']['relation']

#                         # Get the NanoClass Info from its Page ID
#                         nanoclass_infos = []
#                         for related_nanoclass_page_id_info in related_nanoclass_page_ids_info:
#                             nanoclass_info = get_page_info_from_its_page_id(notion_client, related_nanoclass_page_id_info['id'])
#                             nanoclass_infos.append(nanoclass_info)
#                             time.sleep(0.2)

#                     except:
#                         st.write(f"No NanoClass Page with {related_miniclass_page_info}")
#                         continue

#                     # Try to extract related MiniClass page title
#                     for nanoclass_info in nanoclass_infos:
#                         try:
#                             related_nanoclass_page_title = nanoclass_info["properties"]["ナノ分類名"]["title"][0]["text"]["content"]
#                         except:
#                             related_nanoclass_page_title = "No Title"

#                         # Append the NanoClass ID and Title to info list
#                         related_nanoclass_pages_info.append({"id": nanoclass_info['id'], "title": related_nanoclass_page_title})

#                 ## NanoClass Page Info Structure:
#                 # related_nanoclass_pages_info = [
#                 #     {
#                 #         "id": "nanoclass-page-id",
#                 #     "title": "nanoclass-page-title"
#                 # },
#                 # ...
#                 # ]

#                 # Display the related NanoClass titles
#                 st.write(f"#### {selected_subclass_title}に関連するナノ分類のタイトル:")
#                 for related_nanoclass_page_info in related_nanoclass_pages_info:
#                     st.write(f"* {related_nanoclass_page_info['title']}")
#                 st.write("")

        
#         ### Generate contents with OpenAI
#         with st.spinner(f"{selected_subclass_title}の各コンテンツを生成中..."):

#             if len(related_nanoclass_pages_info) == 0:
#                 st.error("生成させるためのナノ分類データが存在しません。細分類を再度選択し直してください。")
#             else:
#                 # Loop through each nanoclass page info
#                 for related_nanoclass_page_info in related_nanoclass_pages_info:
#                     # Set the product name as the nanoclass title
#                     product_name = related_nanoclass_page_info['title']
#                     st.write(f"### ■ {product_name}")

#                     # Skip if the product name is "No Title"
#                     if product_name == "No Title":
#                         st.write(f"タイトル名がないため、生成スキップします。")
#                         continue
#                     else:
#                         ### Generate 5 scenes
#                         scenes_result = generate_contents(openai_client, system_prompt=scene_system_prompt, user_prompt=scene_user_prompt, response_format=Scenes, previous_output=related_nanoclass_page_info['title'], model=model)
#                         time.sleep(delay_time)
#                         ## Unzip the return values
#                         # Extract the scenes content from the result
#                         scenes = scenes_result['choices'][0].message.parsed
#                         ## Store the usage tokens
#                         # Store the usage tokens in the usage_dict as a scene step
#                         usage_dict['scene_step'] = {
#                             'completion_tokens': scenes_result['usage'].completion_tokens,
#                             'prompt_tokens': scenes_result['usage'].prompt_tokens,
#                             'total_tokens': scenes_result['usage'].total_tokens
#                         }

#                         ## Retry if the number of scenes is not 5
#                         retry_count = 0
#                         while len(scenes.scenes) != 5:
#                             # Display the retry message
#                             retry_count += 1
#                             print(f"Retry to generate scenes: {retry_count}")
#                             # Generate scenes
#                             scenes_result = generate_contents(openai_client, system_prompt=scene_system_prompt, user_prompt=scene_user_prompt, response_format=Scenes, previous_output=product_name, model=model)
#                             ## Unzip the return values
#                             # Extract the scenes content from the result
#                             scenes = scenes_result['choices'][0].message.parsed
#                             # Store the usage tokens in the usage_dict as a scene step
#                             usage_dict['scene_step'] = {
#                                 'completion_tokens': scenes_result['usage'].completion_tokens,
#                                 'prompt_tokens': scenes_result['usage'].prompt_tokens,
#                                 'total_tokens': scenes_result['usage'].total_tokens
#                             }
#                             time.sleep(delay_time)
#                         # Print the scenes
#                         st.write(f"#### {product_name}のシーン:")
#                         st.write(scenes.scenes)
#                         # Display the usage tokens on the generating Scenes step
#                         st.write(f"Completion Tokens on Scenes step: {usage_dict['scene_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Scenes step: {usage_dict['scene_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Scenes step: {usage_dict['scene_step']['total_tokens']}")

#                         # Store the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] = scenes_result['usage'].completion_tokens
#                         usage_dict['prompt_tokens_sum'] = scenes_result['usage'].prompt_tokens
#                         usage_dict['total_tokens_sum'] = scenes_result['usage'].total_tokens



#                         ### Create a list of dictionaries for contents like: [{"pattern": "A-1", "scene": scene-A}, {"pattern": "A-2", "scene": scene-A}, ..., "pattern": "E-2", "scene": scene-E}]

#                         # Define patterns and scenes
#                         patterns = ["A-1", "A-2", "B-1", "B-2", "C-1", "C-2", "D-1", "D-2", "E-1", "E-2"]
#                         scenes_list = scenes.scenes
#                         # Populate the contents list
#                         contents = [{"pattern": patterns[i], "scene": scenes_list[i//2]} for i in range(len(patterns))]

#                         ### Generate 10 personas: Generate 2 personas by each a scene
#                         all_personas = []
#                         for i in range(5):
#                             personas_result = generate_contents(openai_client, system_prompt=persona_system_prompt, user_prompt=persona_user_prompt, response_format=Personas, previous_output=scenes_list[i], other_contents=all_personas, product_name=product_name, model=model)
#                             ## Unpack the return values
#                             # Extract the personas content from the result
#                             personas = personas_result['choices'][0].message.parsed
#                             # Update the usage tokens on the persona_step
#                             usage_dict['persona_step']['completion_tokens'] = usage_dict.get('persona_step', {}).get('completion_tokens', 0) + personas_result['usage'].completion_tokens
#                             usage_dict['persona_step']['prompt_tokens'] = usage_dict.get('persona_step', {}).get('prompt_tokens', 0) + personas_result['usage'].prompt_tokens
#                             usage_dict['persona_step']['total_tokens'] = usage_dict.get('persona_step', {}).get('total_tokens', 0) + personas_result['usage'].total_tokens
#                             # Append the generated 2 personas to the all_personas list for refrain from duplicate
#                             all_personas.append(personas.persona_1)
#                             all_personas.append(personas.persona_2)
#                             time.sleep(delay_time)
#                         # Update the personas to the contents
#                         for i in range(10):
#                             contents[i]["persona"] = all_personas[i]


#                         # # Generate 10 personas: Previous Method: Generate 10 personas by each scene one by one
#                         # personas = []
#                         # for i in range(10):
#                         #     print(f"Generating personas... {i+1}/10")
#                         #     persona = generate_contents(openai_client, system_prompt=persona_system_prompt, user_prompt=persona_user_prompt, response_format=Persona, previous_output=contents[i], other_contents=personas, model=model)
#                         #     # Append the persona to the personas list for refrain from duplicate
#                         #     personas.append(persona)
#                         #     # Update the persona to the contents
#                         #     contents[i]["persona"] = persona
#                         #     print(f"Personas generated: {i+1}/10")
#                         #     time.sleep(0.5)
                        
#                         # Print the personas
#                         st.write(f"#### {product_name}のペルソナ:")
#                         st.write(all_personas)

#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Personas step
#                         st.write(f"Completion Tokens on Personas step: {usage_dict['persona_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Personas step: {usage_dict['persona_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Personas step: {usage_dict['persona_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('persona_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('persona_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('persona_step', {}).get('total_tokens', 0)



#                         ### Generate ideas
#                         ## Idea v1
#                         # Generate 10 ideas for Idea v1
#                         ideas_v1 = []
#                         for i in range(10):
#                             print(f"Generating v1 ideas... {i+1}/10")
#                             idea_v1_result = generate_contents(openai_client, system_prompt=idea_v1_system_prompt, user_prompt=idea_v1_user_prompt, response_format=Idea, previous_output=all_personas[i], product_name=product_name, other_contents=ideas_v1, model=model)
#                             ## Unpack the return values
#                             # Extract the idea content from the result
#                             idea_v1 = idea_v1_result['choices'][0].message.parsed
#                             # Update the usage tokens on the idea_v1_step
#                             usage_dict['idea_v1_step']['completion_tokens'] = usage_dict.get('idea_v1_step', {}).get('completion_tokens', 0) + idea_v1_result['usage'].completion_tokens
#                             usage_dict['idea_v1_step']['prompt_tokens'] = usage_dict.get('idea_v1_step', {}).get('prompt_tokens', 0) + idea_v1_result['usage'].prompt_tokens
#                             usage_dict['idea_v1_step']['total_tokens'] = usage_dict.get('idea_v1_step', {}).get('total_tokens', 0) + idea_v1_result['usage'].total_tokens
#                             # Append the idea to the ideas_v1 list for refrain from duplicate
#                             ideas_v1.append(idea_v1)
#                             # Update the idea to the contents
#                             contents[i]["idea_v1"] = idea_v1
#                             print(f"Ideas v1 generated: {i+1}/10")
#                             time.sleep(delay_time)
#                         # Print the ideas
#                         st.write(f"#### {product_name}のアイデアver.1:")
#                         st.write(ideas_v1)
#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Ideas v1 step
#                         st.write(f"Completion Tokens on Ideas v1 step: {usage_dict['idea_v1_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Ideas v1 step: {usage_dict['idea_v1_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Ideas v1 step: {usage_dict['idea_v1_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('idea_v1_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('idea_v1_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('idea_v1_step', {}).get('total_tokens', 0)

#                         ## Idea v2
#                         # Generate 10 ideas for Idea v2
#                         ideas_v2 = []
#                         for i in range(10):
#                             print(f"Generating v2 ideas... {i+1}/10")
#                             idea_v2_result = generate_contents(openai_client, system_prompt=idea_v2_system_prompt, user_prompt=idea_v2_user_prompt, response_format=Idea, product_name=product_name, previous_output=ideas_v1[i], other_contents=ideas_v2, model=model)
#                             ## Unpack the return values
#                             # Extract the idea content from the result
#                             idea_v2 = idea_v2_result['choices'][0].message.parsed
#                             # Update the usage tokens on the idea_v2_step
#                             usage_dict['idea_v2_step']['completion_tokens'] = usage_dict.get('idea_v2_step', {}).get('completion_tokens', 0) + idea_v2_result['usage'].completion_tokens
#                             usage_dict['idea_v2_step']['prompt_tokens'] = usage_dict.get('idea_v2_step', {}).get('prompt_tokens', 0) + idea_v2_result['usage'].prompt_tokens
#                             usage_dict['idea_v2_step']['total_tokens'] = usage_dict.get('idea_v2_step', {}).get('total_tokens', 0) + idea_v2_result['usage'].total_tokens
#                             # Append the idea to the ideas_v2 list for refrain from duplicate
#                             ideas_v2.append(idea_v2)
#                             # Update the idea to the contents
#                             contents[i]["idea_v2"] = idea_v2
#                             print(f"Ideas v2 generated: {i+1}/10")
#                             time.sleep(delay_time)
#                         # Print the ideas
#                         st.write(f"#### {product_name}のアイデアver.2:")
#                         st.write(ideas_v2)
#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Ideas v2 step
#                         st.write(f"Completion Tokens on Ideas v2 step: {usage_dict['idea_v2_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Ideas v2 step: {usage_dict['idea_v2_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Ideas v2 step: {usage_dict['idea_v2_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('idea_v2_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('idea_v2_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('idea_v2_step', {}).get('total_tokens', 0)

#                         ## Idea v3
#                         # Generate 10 ideas for Idea v3 
#                         ideas_v3 = []
#                         for i in range(10):
#                             print(f"Generating v3 ideas... {i+1}/10")
#                             idea_v3_result = generate_contents(openai_client, system_prompt=idea_v3_system_prompt, user_prompt=idea_v3_user_prompt, response_format=Idea, previous_output=ideas_v2[i], product_name=product_name, other_contents=ideas_v3, model=model)
#                             ## Unpack the return values
#                             # Extract the idea content from the result
#                             idea_v3 = idea_v3_result['choices'][0].message.parsed
#                             # Update the usage tokens on the idea_v3_step
#                             usage_dict['idea_v3_step']['completion_tokens'] = usage_dict.get('idea_v3_step', {}).get('completion_tokens', 0) + idea_v3_result['usage'].completion_tokens
#                             usage_dict['idea_v3_step']['prompt_tokens'] = usage_dict.get('idea_v3_step', {}).get('prompt_tokens', 0) + idea_v3_result['usage'].prompt_tokens
#                             usage_dict['idea_v3_step']['total_tokens'] = usage_dict.get('idea_v3_step', {}).get('total_tokens', 0) + idea_v3_result['usage'].total_tokens
#                             # Append the idea to the ideas_v3 list for refrain from duplicate
#                             ideas_v3.append(idea_v3)
#                             # Update the idea to the contents
#                             contents[i]["idea_v3"] = idea_v3
#                             print(f"Ideas v3 generated: {i+1}/10")
#                             time.sleep(delay_time)
#                         # Print the ideas
#                         st.write(f"#### {product_name}のアイデアver.3:")
#                         st.write(ideas_v3)
#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Ideas v3 step
#                         st.write(f"Completion Tokens on Ideas v3 step: {usage_dict['idea_v3_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Ideas v3 step: {usage_dict['idea_v3_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Ideas v3 step: {usage_dict['idea_v3_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('idea_v3_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('idea_v3_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('idea_v3_step', {}).get('total_tokens', 0)


#                         ### Righteous Indignation
#                         # Generate 10 righteous indignations
#                         righteous_indignations = []
#                         for i in range(10):
#                             print(f"Generating righteous indignation... {i+1}/10")
#                             righteous_indignation_result = generate_contents(openai_client, system_prompt=righteous_indignation_system_prompt, user_prompt=righteous_indignation_user_prompt, previous_output=ideas_v3[i], response_format=RighteousIndignation, persona_info=all_personas[i], other_contents=righteous_indignations, model=model)
#                             ## Unpack the return values
#                             # Extract the righteous indignation content from the result
#                             righteous_indignation = righteous_indignation_result['choices'][0].message.parsed
#                             # Update the usage tokens on the righteous_indignation_step
#                             usage_dict['righteous_indignation_step']['completion_tokens'] = usage_dict.get('righteous_indignation_step', {}).get('completion_tokens', 0) + righteous_indignation_result['usage'].completion_tokens
#                             usage_dict['righteous_indignation_step']['prompt_tokens'] = usage_dict.get('righteous_indignation_step', {}).get('prompt_tokens', 0) + righteous_indignation_result['usage'].prompt_tokens
#                             usage_dict['righteous_indignation_step']['total_tokens'] = usage_dict.get('righteous_indignation_step', {}).get('total_tokens', 0) + righteous_indignation_result['usage'].total_tokens
#                             # Append the righteous indignation to the righteous_indignations list for refrain from duplicate
#                             righteous_indignations.append(righteous_indignation)
#                             # Update the righteous indignation to the contents
#                             contents[i]["righteous_indignation"] = righteous_indignation
#                             print(f"Righteous indignation generated: {i+1}/10")
#                             time.sleep(delay_time)
#                         # Print the ideas
#                         st.write(f"#### {product_name}の義憤:")
#                         st.write(righteous_indignations)
#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Righteous Indignation step
#                         st.write(f"Completion Tokens on Righteous Indignation step: {usage_dict['righteous_indignation_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Righteous Indignation step: {usage_dict['righteous_indignation_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Righteous Indignation step: {usage_dict['righteous_indignation_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('righteous_indignation_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('righteous_indignation_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('righteous_indignation_step', {}).get('total_tokens', 0)


#                         ### Appeal Method
#                         # Generate 10 appeal methods
#                         appeal_methods = []
#                         for i in range(10):
#                             print(f"Generating appeal method... {i+1}/10")
#                             appeal_method_result = generate_contents(openai_client, system_prompt=appeal_system_prompt, user_prompt=appeal_user_prompt, previous_output=righteous_indignations[i], response_format=AppealMethod, persona_info=all_personas[i], idea_info=ideas_v3[i], other_contents=appeal_methods, model=model)
#                             ## Unpack the return values
#                             # Extract the appeal method content from the result
#                             appeal_method = appeal_method_result['choices'][0].message.parsed
#                             # Update the usage tokens on the appeal_method_step
#                             usage_dict['appeal_method_step']['completion_tokens'] = usage_dict.get('appeal_method_step', {}).get('completion_tokens', 0) + appeal_method_result['usage'].completion_tokens
#                             usage_dict['appeal_method_step']['prompt_tokens'] = usage_dict.get('appeal_method_step', {}).get('prompt_tokens', 0) + appeal_method_result['usage'].prompt_tokens
#                             usage_dict['appeal_method_step']['total_tokens'] = usage_dict.get('appeal_method_step', {}).get('total_tokens', 0) + appeal_method_result['usage'].total_tokens
#                             # Append the appeal method to the appeal_methods list for refrain from duplicate
#                             appeal_methods.append(appeal_method)
#                             # Update the appeal method to the contents
#                             contents[i]["appeal_method"] = appeal_method
#                             print(f"Appeal method generated: {i+1}/10")
#                             time.sleep(delay_time)
#                         # Print the ideas
#                         st.write(f"#### {product_name}の訴求方法:")
#                         st.write(appeal_methods)
#                         ## Token Usage Counts
#                         # Display the usage tokens on the generating Appeal Method step
#                         st.write(f"Completion Tokens on Appeal Method step: {usage_dict['appeal_method_step']['completion_tokens']}")
#                         st.write(f"Prompt Tokens on Appeal Method step: {usage_dict['appeal_method_step']['prompt_tokens']}")
#                         st.write(f"Total Tokens on Appeal Method step: {usage_dict['appeal_method_step']['total_tokens']}")
#                         # Sum the usage tokens in the usage_dict as a total counts
#                         usage_dict['completion_tokens_sum'] += usage_dict.get('appeal_method_step', {}).get('completion_tokens', 0)
#                         usage_dict['prompt_tokens_sum'] += usage_dict.get('appeal_method_step', {}).get('prompt_tokens', 0)
#                         usage_dict['total_tokens_sum'] += usage_dict.get('appeal_method_step', {}).get('total_tokens', 0)


#                         ## Display the sum of usage tokens as a total counts
#                         st.write(f"#### トータルの使用トークン数:")
#                         st.write(f"Completion Tokens sum: {usage_dict['completion_tokens_sum']}")
#                         st.write(f"Prompt Tokens sum: {usage_dict['prompt_tokens_sum']}")
#                         st.write(f"Total Tokens sum: {usage_dict['total_tokens_sum']}")

#                         # Finish
#                         # End Time Tracking
#                         end_time = time.time()

#                         # Calculate the total time taken
#                         total_time = end_time - start_time
#                         minutes, seconds = divmod(total_time, 60)

#                         ### Save the contents as a json file
#                         st.success(f"{product_name}のコンテンツ生成が完了しました")
#                         ### Prepare contents as a text file for download
#                         text_content = f"Category(Product Name): {product_name}\n"
#                         minutes, seconds = divmod(total_time, 60)
#                         text_content += f"Used Model: {model}\n"
#                         text_content += f"Total time taken: {int(minutes)} minutes and {seconds:.2f} seconds\n"
#                         text_content += "------\n"
#                         text_content += f"Completion Tokens as a total counts: {usage_dict['completion_tokens_sum']}\n"
#                         text_content += f"Prompt Tokens as a total counts: {usage_dict['prompt_tokens_sum']}\n"
#                         text_content += f"Total Tokens as a total counts: {usage_dict['total_tokens_sum']}\n"
#                         text_content += "================================================\n\n"
#                         for content in contents:
#                             text_content += f"----- Pattern: {content['pattern']} ----- \n"
#                             text_content += f"Scene: {content['scene']}\n"
#                             text_content += f"Persona: {content['persona']}\n"
#                             text_content += f"Idea v1: {content['idea_v1']}\n"
#                             text_content += f"Idea v2: {content['idea_v2']}\n"
#                             text_content += f"Idea v3: {content['idea_v3']}\n"
#                             text_content += f"Righteous Indignation: {content['righteous_indignation']}\n"
#                             text_content += f"Appeal Method: {content['appeal_method']}\n"
#                             text_content += "\n"
#                             text_content += "-----------------------------------------\n"

#                         # Provide a download button for the text file
#                         if st.download_button(
#                             label="ログ・コンテンツファイル(JSON)をダウンロード",
#                             data=text_content,
#                             file_name=f"{product_name}_{model}.txt",
#                             mime="text/plain"
#                         ):
#                             st.info(f"{product_name}のログとコンテンツをダウンロードしました")
                    

#                         ##### Post generated contents onto Notion
#                         # Stop for debugging
#                         st.stop()
                        
#                         ## Paste Here as a Batch Update onto Notion after the whole generation

#                         # Post updated scenes
#                         scene_contents = [scene.scene_description for scene in scenes.scenes]
#                         update_scenes_on_nano_db(notion_client, related_nanoclass_page_info['id'], scene_contents)

#                         # Post personas
#                         for persona in personas:
#                             create_persona_on_persona_db(notion_client, PERSONA_DB_ID, persona)
                        
#                         # Post ideas, righteous indignation, and appeal method
#                         for content in contents:
#                             # Version 1
#                             create_idea_on_idea_db(notion_client, IDEA_DB_ID, content, idea_version_number=1)
#                             # Version 2
#                             create_idea_on_idea_db(notion_client, IDEA_DB_ID, content, idea_version_number=2)
#                             # Version 3
#                             create_idea_on_idea_db(notion_client, IDEA_DB_ID, content, idea_version_number=3)

#                         # Display the finish message
#                         print(f"Created contents of {product_name}")
#                         st.info(f"「{product_name}」に関して生成したコンテンツをNotionへ投稿しました")

#                 # Finish
#                 # End Time Tracking
#                 # end_time = time.time()

#                 # Calculate the total time taken
#                 # total_time = end_time - start_time
#                 # minutes, seconds = divmod(total_time, 60)

#                 # Display the finish message
#                 st.success(f"{selected_subclass_title}の生成が完了しました！")
#                 st.write(f"所要時間: {int(minutes)}分{seconds:.2f}秒")

# ### --- End of Generate Contents --- ###
