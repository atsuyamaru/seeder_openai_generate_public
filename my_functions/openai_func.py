import time
from typing import TypeVar, Type
from pydantic import BaseModel
import openai
from openai import OpenAIError, RateLimitError
T = TypeVar('T', bound=BaseModel)

### Contents Generator
def generate_contents(client, system_prompt: str, user_prompt: str, response_format: Type[T], previous_output: str | list | None = None, other_contents: str | list[str] | None = None, product_name: str | None = None, persona_info: str | None = None, idea_info: str | None = None, model: str = "gpt-4o-2024-08-06") -> dict['choices': list, 'usage']:
    """
    Generates content based on the provided prompts and previous output using the OpenAI client.

    Parameters:
    - client: The OpenAI client instance used to generate the content.
    - previous_output (str): The output from the previous step, used as context for the current generation.
    - system_prompt (str): The system prompt that sets the context for the AI.
    - user_prompt (str): The user prompt that specifies the task for the AI.
    - response_format (Type[T]): The expected format of the response.
    - other_contents (str | list, optional): Other contents from previous steps. This helps the AI to refrain from duplicating the same content, if applicable. Default is None.
    - product_name (str, optional): The name of the product, if applicable. Default is None.
    - persona_info (str, optional): Information about the persona, if applicable. Default is None.
    - idea_info (str, optional): Information about the idea, if applicable. Default is None.
    - model (str, optional): The model to be used for generation. Default is "gpt-4o-2024-08-06".

    Returns:
    - dict: The generated content in the specified format.
      - content: result['choices'][0].message.parsed
      - usage token count: result['usage'] -> JSON like object
        - .completion_tokens
        - .prompt_tokens
        - .total_tokens
    """

    # Create a previous_output prompt if previous_output is provided
    if previous_output is not None:
        previous_output_prompt = f"""
        -----
        # 直前の出力: {previous_output}
        以下、 {previous_output} = [直前の出力] とします。
        """
    else:
        previous_output_prompt = ""

    # Create a other_contents prompt if other_contents is provided
    if other_contents is not None or other_contents != [] or other_contents != "":
        other_contents_prompt = f"""
        -----
        # 他のコンテンツ: {other_contents}
        以下、 {other_contents} = [他のコンテンツ] とします。
        出力内容は、この[他のコンテンツ]に重複しないようにしてください。
        """
    else:
        other_contents_prompt = ""

    # Create a product prompt if a product name is provided
    if product_name is not None:
        product_prompt = f"""
        -----
        # 商品名: {product_name}
        以下、 {product_name} = [商品名] とします。
        """
    else:
        product_prompt = ""

    # Create a persona prompt if persona information is provided
    if persona_info is not None:
        persona_prompt = f"""
        -----
        # ペルソナ情報: {persona_info}
        以下、 {persona_info} = [ペルソナ情報] とします。
        """
    else:
        persona_prompt = ""
    
    # Create an idea prompt if idea information is provided
    if idea_info is not None:
        idea_prompt = f"""
        -----
        # アイデア情報: {idea_info}
        以下、 {idea_info} = [アイデア情報] とします。
        """
    else:
        idea_prompt = ""

    # Generate the content using the OpenAI client
    result = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"""
                {previous_output_prompt}
                {other_contents_prompt}
                {product_prompt}
                {persona_prompt}
                {idea_prompt}
                -----
                # 今回の指示内容:
                {user_prompt}"""
                }
            ],
            response_format=response_format
        )
    
    # Check if the result has a valid response without any refusal
    if result.choices[0].message.refusal is not None:
        raise ValueError(f"The result was refused: {result.choices[0].message.refusal}")

    # Return the result as a dictionary
    return dict(result)


# ### English Translation
# # Define the model for the English
# class TranslatedJapaneseText(BaseModel):
#     content: str


# def translate_2en(client, ja_text: str, model="gpt-4o-2024-08-06") -> str:

#     en_result = client.beta.chat.completions.parse(
#         model=model,
#         messages=[
#             {"role": "system", "content": "You are a translator from the given Japanese text into English."},
#             {
#                 "role": "user",
#                 "content": f"Just translate the following Japanese text into English: {ja_text}"
#             }
#         ],
#         response_format=TranslatedJapaneseText
#     )

#     print(f"The selected model: {model}")
#     return en_result.choices[0].message.parsed.content

