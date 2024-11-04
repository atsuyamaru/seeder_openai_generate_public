import streamlit as st
from my_functions.streamlit_util_func import read_json_file

def clear_session_state_for_overwrite_confirmation():
    st.session_state['confirm_overwrite_settings'] = False
    st.session_state['done_overwrite_settings'] = False

def load_default_values() -> dict:
    # Load preset values from JSON files
    # Scene
    scene_defaults = read_json_file("openai_prompts_json/scene_prompts.json")
    scene_model = scene_defaults["scene_model"]
    scene_system_prompt = scene_defaults["scene_system_prompt"]
    scene_user_prompt = scene_defaults["scene_user_prompt"]
    
    # Persona
    persona_defaults = read_json_file("openai_prompts_json/persona_prompts.json")
    persona_model = persona_defaults["persona_model"]
    persona_system_prompt = persona_defaults["persona_system_prompt"]
    persona_user_prompt = persona_defaults["persona_user_prompt"]
    
    # Idea v1
    idea_v1_defaults = read_json_file("openai_prompts_json/idea_prompts.json")
    idea_v1_model = idea_v1_defaults["idea_v1_model"]
    idea_v1_system_prompt = idea_v1_defaults["idea_v1_system_prompt"]
    idea_v1_user_prompt = idea_v1_defaults["idea_v1_user_prompt"]
    
    # Idea v2
    idea_v2_defaults = read_json_file("openai_prompts_json/idea_prompts.json")
    idea_v2_model = idea_v2_defaults["idea_v2_model"]
    idea_v2_system_prompt = idea_v2_defaults["idea_v2_system_prompt"]
    idea_v2_user_prompt = idea_v2_defaults["idea_v2_user_prompt"]
    
    # Idea v3
    idea_v3_defaults = read_json_file("openai_prompts_json/idea_prompts.json")
    idea_v3_model = idea_v3_defaults["idea_v3_model"]
    idea_v3_system_prompt = idea_v3_defaults["idea_v3_system_prompt"]
    idea_v3_user_prompt = idea_v3_defaults["idea_v3_user_prompt"]
    
    # Righteous Indignation
    righteous_indignation_defaults = read_json_file("openai_prompts_json/righteous_indignation_prompts.json")
    righteous_indignation_model = righteous_indignation_defaults["righteous_indignation_model"]
    righteous_indignation_system_prompt = righteous_indignation_defaults["righteous_indignation_system_prompt"]
    righteous_indignation_user_prompt = righteous_indignation_defaults["righteous_indignation_user_prompt"]
    
    # Appeal Method
    appeal_defaults = read_json_file("openai_prompts_json/appeal_method_prompts.json")
    appeal_model = appeal_defaults["appeal_model"]
    appeal_system_prompt = appeal_defaults["appeal_system_prompt"]
    appeal_user_prompt = appeal_defaults["appeal_user_prompt"]
    
    return {
        "scene": (scene_model, scene_system_prompt, scene_user_prompt),
        "persona": (persona_model, persona_system_prompt, persona_user_prompt),
        "idea_v1": (idea_v1_model, idea_v1_system_prompt, idea_v1_user_prompt),
        "idea_v2": (idea_v2_model, idea_v2_system_prompt, idea_v2_user_prompt),
        "idea_v3": (idea_v3_model, idea_v3_system_prompt, idea_v3_user_prompt),
        "righteous_indignation": (righteous_indignation_model, righteous_indignation_system_prompt, righteous_indignation_user_prompt),
        "appeal": (appeal_model, appeal_system_prompt, appeal_user_prompt)
    }


def initialize_session_state(defaults: dict) -> None:
    # Unpack defaults
    scene_model, scene_system_prompt, scene_user_prompt = defaults["scene"]
    persona_model, persona_system_prompt, persona_user_prompt = defaults["persona"]
    idea_v1_model, idea_v1_system_prompt, idea_v1_user_prompt = defaults["idea_v1"]
    idea_v2_model, idea_v2_system_prompt, idea_v2_user_prompt = defaults["idea_v2"]
    idea_v3_model, idea_v3_system_prompt, idea_v3_user_prompt = defaults["idea_v3"]
    righteous_indignation_model, righteous_indignation_system_prompt, righteous_indignation_user_prompt = defaults["righteous_indignation"]
    appeal_model, appeal_system_prompt, appeal_user_prompt = defaults["appeal"]

    # Initialize session state with preset values
    # Scenes
    if 'scene_model' not in st.session_state:
        st.session_state['scene_model'] = scene_model
    if 'scene_model_select' not in st.session_state:
        st.session_state['scene_model_select'] = st.session_state['scene_model']
    if 'scene_system_prompt' not in st.session_state:
        st.session_state['scene_system_prompt'] = scene_system_prompt
    if 'scene_user_prompt' not in st.session_state:
        st.session_state['scene_user_prompt'] = scene_user_prompt

    # Personas
    if 'persona_model' not in st.session_state:
        st.session_state['persona_model'] = persona_model
    if 'persona_model_select' not in st.session_state:
        st.session_state['persona_model_select'] = st.session_state['persona_model']
    if 'persona_system_prompt' not in st.session_state:
        st.session_state['persona_system_prompt'] = persona_system_prompt
    if 'persona_user_prompt' not in st.session_state:
        st.session_state['persona_user_prompt'] = persona_user_prompt

    # Idea v1
    if 'idea_v1_model' not in st.session_state:
        st.session_state['idea_v1_model'] = idea_v1_model
    if 'idea_v1_system_prompt' not in st.session_state:
        st.session_state['idea_v1_system_prompt'] = idea_v1_system_prompt
    if 'idea_v1_user_prompt' not in st.session_state:
        st.session_state['idea_v1_user_prompt'] = idea_v1_user_prompt

    # Idea v2
    if 'idea_v2_model' not in st.session_state:
        st.session_state['idea_v2_model'] = idea_v2_model
    if 'idea_v2_system_prompt' not in st.session_state:
        st.session_state['idea_v2_system_prompt'] = idea_v2_system_prompt
    if 'idea_v2_user_prompt' not in st.session_state:
        st.session_state['idea_v2_user_prompt'] = idea_v2_user_prompt

    # Idea v3
    if 'idea_v3_model' not in st.session_state:
        st.session_state['idea_v3_model'] = idea_v3_model
    if 'idea_v3_system_prompt' not in st.session_state:
        st.session_state['idea_v3_system_prompt'] = idea_v3_system_prompt
    if 'idea_v3_user_prompt' not in st.session_state:
        st.session_state['idea_v3_user_prompt'] = idea_v3_user_prompt

    # Righteous Indignation
    if 'righteous_indignation_model' not in st.session_state:
        st.session_state['righteous_indignation_model'] = righteous_indignation_model
    if 'righteous_indignation_system_prompt' not in st.session_state:
        st.session_state['righteous_indignation_system_prompt'] = righteous_indignation_system_prompt
    if 'righteous_indignation_user_prompt' not in st.session_state:
        st.session_state['righteous_indignation_user_prompt'] = righteous_indignation_user_prompt

    # Appeal Method
    if 'appeal_model' not in st.session_state:
        st.session_state['appeal_model'] = appeal_model
    if 'appeal_system_prompt' not in st.session_state:
        st.session_state['appeal_system_prompt'] = appeal_system_prompt
    if 'appeal_user_prompt' not in st.session_state:
        st.session_state['appeal_user_prompt'] = appeal_user_prompt