import time

### --- Update Info to Notion --- ###
# Update Page Property: Sample. The below is to update only the scene property
def update_page_properties(client, page_id):
    response = client.pages.update(
        **{
            "page_id": page_id,
            "properties": {
                "シーン": {
                    "rich_text":
                        [{
                        "type": "text",
                        "text": {
                            "content":"Hello, World!"
                        }
                        }]
                }
            }
        }
    )


# Update Scene properties on Nano DB
def update_scenes_on_nano_db(client, nano_page_id, scene_contents:list, delay_post:float = 0.2) -> None:
    """
    Update the scenes on the nano DB.
    Post 5 scenes to the nano DB corresponding from A to E. These A-E symbols are appended automatically on the given scene contents list.
    Args:
        client: The Notion client object.
        nano_page_id (str): The ID of the nano page to update.
        scene_contents (list): A list of scene contents to update.
        delay_post (float): The delay time between each post.
    """

    symbols = ["A", "B", "C", "D", "E"]
    for symbol, scene_content in zip(symbols, scene_contents):
        response = client.pages.update(
            **{
                "page_id": nano_page_id,
                "properties": {
                    f"シーン{symbol}": {
                        "rich_text":
                            [{
                            "type": "text",
                            "text": {
                                "content": scene_content
                            }
                            }]
                    }
                }
            }
        )
        time.sleep(delay_post)