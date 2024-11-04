import time

### --- Get Info from Notion --- ###

### Working with Database ID
# Get All Page info from a specific DB
def get_all_pages_info_from_db_id(client, database_id: str) -> list:
    """
    Retrieves all information from a specified Notion database.

    Args:
        client: The Notion client object.
        database_id (str): The ID of the Notion database to query.

    Returns:
        list: A list of dictionaries, each containing all information for a page in the database.
    """
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )

    return response["results"]


# Retrieve a list of page IDs of records existing in the database
def get_page_ids_from_db_id(client, database_id):
    """
    Retrieves a list of page IDs from a specified Notion database.

    Args:
        client: The Notion client object.
        database_id: The ID of the Notion database to query.

    Returns:
        list: A list of page IDs from the database.
    """
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )

    # Extract only results from the whole response
    results = response["results"]
    page_ids = []
    for result in results:
        # Append each page ID to the list
        page_ids.append(result["id"])

    print(f"read_pages_from_database completed. (len={len(page_ids)})")
    return page_ids


# # Under Development
# def get_page_ids_and_titles_from_db_id(client, database_id: str) -> list: 
#     """
#     Retrieves page IDs and titles from a specified Notion database.

#     Args:
#         client: The Notion client object.
#         database_id (str): The ID of the Notion database to query.

#     Returns:
#         list: A list of dictionaries, each containing 'page_id' and 'page_title' for each page in the database.
#               If a page has no title, 'page_title' will be None.
#     """
#     response = client.databases.query(
#         **{
#             "database_id": database_id,
#         }
#     )

#     # Extract only results from the whole response
#     results = response["results"]
#     page_datum = []
#     for result in results:
#         page_id = result["id"]
#         page_title = None
#         if "Name" in result["properties"]:
#             try:
#                 # キーをDB特有の値（カラム名）にして指定する必要あり。このままでは動きません。
#                 page_title = result["properties"]["Name"]["title"][0]["text"]["content"]
#             except IndexError:
#                 page_title = None
#         page_datum.append({"page_id": page_id, "page_title": page_title})

#     return page_datum


### Working with Query
# Get DB info from query, title and id
def get_db_names_and_ids_from_query(client, query: str) -> list:
    """
    Search for databases in Notion using a query string and return a list of dictionaries containing database names and IDs.

    Args:
        client: The Notion client object.
        query (str): The search query string.

    Returns:
        list: A list of dictionaries, each containing 'db_title' and 'db_id' for found databases.
        If no databases are found, returns an empty list.
    """
    results = client.search(query=query).get("results")

    # Dict in List for db_info. [{db_title: db_id}, ...]
    db_names_ids = []
    db_count = 0

    for result in results:
        # Check if the result is a database
        if result["object"] == "database":
            db_count += 1
            db_info = {}
            db_info["db_title"] = result["title"][0]["plain_text"]
            db_info["db_id"] = result["id"]
            db_names_ids.append(db_info)
    
    if db_count:
        print(f"Found {db_count} databases.")
        return db_names_ids
    else:
        print(f"No databases found with query: {query}")
        return []


def get_db_properties_from_db_title_and_id(client, db_title: str, db_id: str) -> dict:
    """
    Retrieve the properties of a Notion database using its title and ID.
    CAUTION: The related database IDs that is retrieved are the 'Database ID's, not the 'Page ID's.

    Args:
        client: The Notion client object.
        db_title (str): The title of the database to search for.
        db_id (str): The ID of the database to match.

    Returns:
        dict: A dictionary containing the properties of the found database.
        If no matching database is found, returns an empty dictionary.
    """
    results = client.search(query=db_title).get("results")

    for result in results:
        if result["object"] == "database" and result['id'] == db_id:
            return result["properties"]
    
    print(f"No database found with title: {db_title} and id: {db_id}")
    return {}


### Working with Page ID
# Get page info from the page ID
def get_page_info_from_its_page_id(client, page_id):
    response = client.pages.retrieve(page_id)

    return response



