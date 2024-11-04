import inspect
import json
import streamlit as st

### --- Load and Save JSON File --- ###
### JSON File Reader
def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

### JSON File Writer
def write_json_file(file_path: str, data: dict):
    """
    Writes data to a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.
    - data (dict): The data to be written to the JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

### Display the code of the model
def display_code_of_model(model):
    # Get the source code of the model
    source_code = inspect.getsource(model)
    st.code(source_code, language='python')

# Update Model in Session State on dropdown selection with Callback Function
def update_model(step_name):
    # Update the session state if the model has changed
    if st.session_state[f"{step_name}_model_select"] != st.session_state[f"{step_name}_model"]:
        st.session_state[f"{step_name}_model"] = st.session_state[f"{step_name}_model_select"]

