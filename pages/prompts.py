from datetime import datetime
import json
from time import sleep

import streamlit as st
from openai import OpenAI

# Import Schema for OpenAI generation outputs
from my_functions.openai_structured_schema import Scenes, Scene, Personas, Persona, Idea, RighteousIndignation, AppealMethod

# Import My functions for OpenAI generation
from my_functions.openai_func import generate_contents

# Import My functions for Streamlit
from my_functions.streamlit_util_func import read_json_file, write_json_file, display_code_of_model, update_model

# Import My functions for Session State
from my_functions.session_state_st import initialize_session_state, load_default_values, clear_session_state_for_overwrite_confirmation


### ------ Streamlit App ------ ###
# Load Default Values
default_values = load_default_values()
# Initialize Session State
initialize_session_state(default_values)

### --- Side Bar --- ###
st.sidebar.write("")
### Download Common Prompt Settings
# Concatinate all default prompts to save as a single file with JSON format
all_prompts = {
    "scene_model": default_values['scene'][0],
    "scene_system_prompt": default_values['scene'][1],
    "scene_user_prompt": default_values['scene'][2],
    "persona_model": default_values['persona'][0],
    "persona_system_prompt": default_values['persona'][1],
    "persona_user_prompt": default_values['persona'][2],
    "idea_v1_model": default_values['idea_v1'][0],
    "idea_v1_system_prompt": default_values['idea_v1'][1],
    "idea_v1_user_prompt": default_values['idea_v1'][2],
    "idea_v2_model": default_values['idea_v2'][0],
    "idea_v2_system_prompt": default_values['idea_v2'][1],
    "idea_v2_user_prompt": default_values['idea_v2'][2],
    "idea_v3_model": default_values['idea_v3'][0],
    "idea_v3_system_prompt": default_values['idea_v3'][1],
    "idea_v3_user_prompt": default_values['idea_v3'][2],
    "righteous_indignation_model": default_values['righteous_indignation'][0],
    "righteous_indignation_system_prompt": default_values['righteous_indignation'][1],
    "righteous_indignation_user_prompt": default_values['righteous_indignation'][2],
    "appeal_model": default_values['appeal'][0],
    "appeal_system_prompt": default_values['appeal'][1],
    "appeal_user_prompt": default_values['appeal'][2]
}
# Create a filename for the downloaded file
today = datetime.now().strftime("%Y_%m_%d")
filename = f"default_prompt_settings_{today}.json"
# Download the file
if st.sidebar.download_button(label="デフォルト・共通プロンプト設定ファイル(JSON)をダウンロード", data=json.dumps(all_prompts, ensure_ascii=False, indent=4), file_name=filename, key="download_common_prompt_settings"):
    sleep(1)
    st.sidebar.success("ダウンロードしました")

st.sidebar.write("")
## Download Temporary Prompt on Screen Settings
# Concatinate all prompts to save as a single file with JSON format
all_prompts = {
    "scene_model": st.session_state['scene_model'],
    "scene_system_prompt": st.session_state['scene_system_prompt'],
    "scene_user_prompt": st.session_state['scene_user_prompt'],
    "persona_model": st.session_state['persona_model'],
    "persona_system_prompt": st.session_state['persona_system_prompt'],
    "persona_user_prompt": st.session_state['persona_user_prompt'],
    "idea_v1_model": st.session_state['idea_v1_model'],
    "idea_v1_system_prompt": st.session_state['idea_v1_system_prompt'],
    "idea_v1_user_prompt": st.session_state['idea_v1_user_prompt'],
    "idea_v2_model": st.session_state['idea_v2_model'],
    "idea_v2_system_prompt": st.session_state['idea_v2_system_prompt'],
    "idea_v2_user_prompt": st.session_state['idea_v2_user_prompt'],
    "idea_v3_model": st.session_state['idea_v3_model'],
    "idea_v3_system_prompt": st.session_state['idea_v3_system_prompt'],
    "idea_v3_user_prompt": st.session_state['idea_v3_user_prompt'],
    "righteous_indignation_model": st.session_state['righteous_indignation_model'],
    "righteous_indignation_system_prompt": st.session_state['righteous_indignation_system_prompt'],
    "righteous_indignation_user_prompt": st.session_state['righteous_indignation_user_prompt'],
    "appeal_model": st.session_state['appeal_model'],
    "appeal_system_prompt": st.session_state['appeal_system_prompt'],
    "appeal_user_prompt": st.session_state['appeal_user_prompt']
}
# Create a filename for the downloaded file
today = datetime.now().strftime("%Y_%m_%d")
filename = f"temporary_prompt_settings_{today}.json"
# Download the file
if st.sidebar.download_button(label="画面上の仮プロンプト設定ファイル(JSON)をダウンロード", data=json.dumps(all_prompts, ensure_ascii=False, indent=4), file_name=filename, key="download_temporary_prompt_settings"):
    sleep(1)
    st.sidebar.success("ダウンロードしました")

st.sidebar.divider()

## Overwrite Common Prompt Settings
# Session State for Confirmation
if 'confirm_overwrite_settings' not in st.session_state:
    st.session_state['confirm_overwrite_settings'] = False
if 'done_overwrite_settings' not in st.session_state:
    st.session_state['done_overwrite_settings'] = False
# Confirmation
st.sidebar.write("本画面上のプロンプト設定を永続・全体適用する場合は、共通プロンプト設定（デフォルト設定）を上書き保存してください。")
if st.sidebar.button("デフォルト設定・共通プロンプト設定を画面上のプロンプト設定で上書き保存する", key="overwrite_common_prompt_settings") or st.session_state['confirm_overwrite_settings'] == True:
    st.session_state['confirm_overwrite_settings'] = True
    st.sidebar.warning("共通設定を上書き保存します。よろしいですか？")
    if st.sidebar.button("上書き保存する", key="confirm_overwrite_settings_yes") or st.session_state['done_overwrite_settings'] == True:
        st.session_state['done_overwrite_settings'] = True
        # Create a dictionary to store scene prompts
        scene_prompts_for_json   = {
        "scene_model": st.session_state['scene_model'],
        "scene_system_prompt": st.session_state['scene_system_prompt'],
        "scene_user_prompt": st.session_state['scene_user_prompt']
        }
        write_json_file("openai_prompts_json/scene_prompts.json", scene_prompts_for_json)
        # Create a dictionary to store persona prompts
        persona_prompts_for_json = {
            "persona_model": st.session_state['persona_model'],
            "persona_system_prompt": st.session_state['persona_system_prompt'],
            "persona_user_prompt": st.session_state['persona_user_prompt']
        }
        write_json_file("openai_prompts_json/persona_prompts.json", persona_prompts_for_json)
        # Create a dictionary to store all ideas prompts
        idea_prompts_for_json = {
            "idea_v1_model": st.session_state['idea_v1_model'],
            "idea_v1_system_prompt": st.session_state['idea_v1_system_prompt'],
            "idea_v1_user_prompt": st.session_state['idea_v1_user_prompt'],
            "idea_v2_model": st.session_state['idea_v2_model'],
            "idea_v2_system_prompt": st.session_state['idea_v2_system_prompt'],
            "idea_v2_user_prompt": st.session_state['idea_v2_user_prompt'],
            "idea_v3_model": st.session_state['idea_v3_model'],
            "idea_v3_system_prompt": st.session_state['idea_v3_system_prompt'],
            "idea_v3_user_prompt": st.session_state['idea_v3_user_prompt']
        }
        write_json_file("openai_prompts_json/idea_prompts.json", idea_prompts_for_json)
        # Create a dictionary to store righteous indignation prompts
        righteous_indignation_prompts_for_json = {
            "righteous_indignation_model": st.session_state['righteous_indignation_model'],
            "righteous_indignation_system_prompt": st.session_state['righteous_indignation_system_prompt'],
            "righteous_indignation_user_prompt": st.session_state['righteous_indignation_user_prompt']  
        }
        write_json_file("openai_prompts_json/righteous_indignation_prompts.json", righteous_indignation_prompts_for_json)
        # Create a dictionary to store appeal method prompts
        appeal_prompts_for_json = {
            "appeal_model": st.session_state['appeal_model'],
            "appeal_system_prompt": st.session_state['appeal_system_prompt'],
            "appeal_user_prompt": st.session_state['appeal_user_prompt']
        }
        write_json_file("openai_prompts_json/appeal_method_prompts.json", appeal_prompts_for_json)
        st.sidebar.success("共通設定を上書き保存しました")

        # Clear Session State for Confirmation
        sleep(3)
        clear_session_state_for_overwrite_confirmation()
        st.rerun()

### --- End of Side Bar --- ###

### --- Main Screen --- ###
# MainScreen Title
st.write("## プロンプト設定")
st.info("本画面上のプロンプト設定は、セッションを維持している間のみ仮保存の状態として維持されます。ダウンロード・全体共通設定への反映はサイドバーから行ってください。")

# Model List for dropdown selection
model_list = ["gpt-4o-mini", "gpt-4o"]

## Define tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["シーン", "ペルソナ", "アイデアv1", "アイデアv2", "アイデアv3", "義憤", "アピールポイント"])

with tab1:
    # initialize_session_state()
    st.write("### シーン 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['scene_system_prompt'] = st.text_area(label="シーン: システム用プロンプト", value=st.session_state['scene_system_prompt'], height=350, key="scene_system_prompt_text_area")
    with col2:
        st.session_state['scene_user_prompt'] = st.text_area(label="シーン: ユーザー用プロンプト", value=st.session_state['scene_user_prompt'], height=350, key="scene_user_prompt_text_area")
    st.write("")
    # Display the output schema of scene
    with st.expander("シーンの出力における型"):
        st.write("シーンは5つ同時に生成されます。")
        display_code_of_model(Scenes)
        display_code_of_model(Scene)
    # Dropdown selection for scene model
    st.selectbox(label="シーン生成に適用するAIモデルを選択:", options=model_list, key="scene_model_select", index=model_list.index(st.session_state['scene_model']), on_change=update_model, args=("scene",))

# Personas Step
with tab2:
    # initialize_session_state()
    st.write("### ペルソナ 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['persona_system_prompt'] = st.text_area(label="ペルソナ: システム用プロンプト", value=st.session_state['persona_system_prompt'], height=350, key="persona_system_prompt_text_area")
    with col2:
        st.session_state['persona_user_prompt'] = st.text_area(label="ペルソナ: ユーザー用プロンプト", value=st.session_state['persona_user_prompt'], height=350, key="persona_user_prompt_text_area")
    st.write("")
    # Display the output schema of persona
    with st.expander("ペルソナの出力における型"):
        st.write("ペルソナはシーンごとに2人ずつ生成されます。")
        display_code_of_model(Personas)
        display_code_of_model(Persona)
    # Dropdown selection for persona model
    st.selectbox(label="ペルソナ生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['persona_model']), key="persona_model_select", on_change=update_model, args=("persona",))

with tab3:
    st.write("### アイデアv1 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['idea_v1_system_prompt'] = st.text_area(label="アイデアv1: システム用プロンプト", value=st.session_state['idea_v1_system_prompt'], height=350, key="idea_v1_system_prompt_text_area")
    with col2:
        st.session_state['idea_v1_user_prompt'] = st.text_area(label="アイデアv1: ユーザー用プロンプト", value=st.session_state['idea_v1_user_prompt'], height=350, key="idea_v1_user_prompt_text_area")
    st.write("")
    # Display the output schema of idea v1
    with st.expander("アイデアv1の出力における型（アイデアv1〜v3共通）"):
        display_code_of_model(Idea)
    # Dropdown selection for idea v1 model
    st.selectbox(label="アイデアv1生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['idea_v1_model']), key="idea_v1_model_select", on_change=update_model, args=("idea_v1",))

with tab4:
    st.write("### アイデアv2 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['idea_v2_system_prompt'] = st.text_area(label="アイデアv2: システム用プロンプト", value=st.session_state['idea_v2_system_prompt'], height=350, key="idea_v2_system_prompt_text_area")
    with col2:
        st.session_state['idea_v2_user_prompt'] = st.text_area(label="アイデアv2: ユーザー用プロンプト", value=st.session_state['idea_v2_user_prompt'], height=350, key="idea_v2_user_prompt_text_area")
    st.write("")
    # Display the output schema of idea v2
    with st.expander("アイデアv2の出力における型（アイデアv1〜v3共通）"):
        display_code_of_model(Idea)
    # Dropdown selection for idea v2 model
    st.selectbox(label="アイデアv2生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['idea_v2_model']), key="idea_v2_model_select", on_change=update_model, args=("idea_v2",))

with tab5:
    st.write("### アイデアv3 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['idea_v3_system_prompt'] = st.text_area(label="アイデアv3: システム用プロンプト", value=st.session_state['idea_v3_system_prompt'], height=350, key="idea_v3_system_prompt_text_area")
    with col2:
        st.session_state['idea_v3_user_prompt'] = st.text_area(label="アイデアv3: ユーザー用プロンプト", value=st.session_state['idea_v3_user_prompt'], height=350, key="idea_v3_user_prompt_text_area")
    st.write("")
    # Display the output schema of idea v3
    with st.expander("アイデアv3の出力における型（アイデアv1〜v3共通）"):
        display_code_of_model(Idea)
    # Dropdown selection for idea v3 model
    st.selectbox(label="アイデアv3生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['idea_v3_model']), key="idea_v3_model_select", on_change=update_model, args=("idea_v3",))

with tab6:
    st.write("### 義憤 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['righteous_indignation_system_prompt'] = st.text_area(label="義憤: システム用プロンプト", value=st.session_state['righteous_indignation_system_prompt'], height=350, key="righteous_indignation_system_prompt_text_area")
    with col2:
        st.session_state['righteous_indignation_user_prompt'] = st.text_area(label="義憤: ユーザー用プロンプト", value=st.session_state['righteous_indignation_user_prompt'], height=350, key="righteous_indignation_user_prompt_text_area")
    st.write("")
    # Display the output schema of righteous indignation
    with st.expander("義憤の出力における型"):
        display_code_of_model(RighteousIndignation)
    # Dropdown selection for righteous indignation model
    st.selectbox(label="義憤生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['righteous_indignation_model']), key="righteous_indignation_model_select", on_change=update_model, args=("righteous_indignation",))

with tab7:
    st.write("### アピールポイント 生成ステップ")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.session_state['appeal_system_prompt'] = st.text_area(label="アピールポイント: システム用プロンプト", value=st.session_state['appeal_system_prompt'], height=350, key="appeal_system_prompt_text_area")
    with col2:
        st.session_state['appeal_user_prompt'] = st.text_area(label="アピールポイント: ユーザー用プロンプト", value=st.session_state['appeal_user_prompt'], height=350, key="appeal_user_prompt_text_area")
    st.write("")
    # Display the output schema of appeal method
    with st.expander("アピールポイントの出力における型"):
        display_code_of_model(AppealMethod)
    # Dropdown selection for appeal method model
    st.selectbox(label="アピールポイント生成に適用するAIモデルを選択:", options=model_list, index=model_list.index(st.session_state['appeal_model']), key="appeal_model_select", on_change=update_model, args=("appeal",))

st.divider()
## -- The Bottom of the Main Screen -- ##
st.write("##### 使用可能なシステム変数")
st.info("以下のシステム変数は、プロンプトの中で[]で囲むことで使用できます。例: [直前の出力]")
st.write("""
* [直前の出力] : 直前の出力を表します。（最初の出力である「シーン」ステップでは利用不可）
* [他のコンテンツ] : 同じステップ内ですでに出力した他のコンテンツを表します。（2個目以降の出力に自動適用）
* [商品名] : 商品名 = ナノ分類名を表します。
* [ペルソナ情報] : 詳細を含むペルソナ情報を表します。「義憤」・「アピールポイント」ステップでのみ使用できます。
* [アイデア情報] : 詳細を含むアイデア情報を表します。「アピールポイント」ステップでのみ使用できます。
""")
### --- End of Main Screen --- ###

### --- End of Streamlit App --- ###
