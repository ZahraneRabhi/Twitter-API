import pyodbc


def verify_connection_db(server_name, database_name):
    """
    Verify the connection with the specified SQL Server database and server.

    Args:
        server_name (str): The name of the SQL Server.
        database_name (str): The name of the database.
    """
    print(f"{'-'*40}\nConnecting to  {server_name}...\n{'-'*40}")  
    connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes"
    connection = pyodbc.connect(connection_string)
    connection.close()
    print(f"\033[92m{'-'*40}\nConnected successfully to {server_name}\n{'-'*40}\033[0m")  
    
    
def add_comment_to_sql_server(server_name, database_name, comment):
    """
    Inserts or updates comments data into the specified SQL Server database and server.

    Args:
        server_name (str): The name of the SQL Server.
        database_name (str): The name of the database.
    """
    connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes"
    connection = pyodbc.connect(connection_string)
    db = connection.cursor()
    """
    This SQL query:
      - replaces/update a comment row if there is a Primary Key match
      - inserts a comment row if there is no Primary Key match 

    It was implemented to consider if the client/user has updated his review/comment
    so we'll only need his latest comment
    """
    query = f'''
    MERGE INTO comment AS target
    USING (VALUES (
        {comment["comment_id"]},
        {comment["comment_text"]},
        {comment["comment_date"]},
        {comment["comment_author"]},
        {comment["platform"]}
    )) AS source (comment_id, comment_text, comment_date, comment_author, platform)
    ON target.comment_id = source.comment_id
    WHEN MATCHED THEN
        UPDATE SET
            comment_text = source.comment_text,
            comment_date = source.comment_date,
            comment_author = source.comment_author,
            platform = source.platform
    WHEN NOT MATCHED THEN
        INSERT (comment_id, comment_text, comment_date, comment_author, platform)
        VALUES (source.comment_id, source.comment_text, source.comment_date, source.comment_author, source.platform);
    '''
    
    select = "SELECT * FROM comment"
    try: 
        data = db.execute(query) # print(data) 
        data = db.execute(select) # print(data)
        print(f"\033[92m{'-'*40}\nRow Inserted/Updated successfully to {database_name}\n{'-'*40}\033[0m")  
    except pyodbc.Error as e:
        print(f"\033[91m{'-'*40}\nError {e}\n{'-'*40}\033[0m")          
    connection.commit()  
    connection.close()


