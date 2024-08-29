from dataclasses import dataclass
import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()


sql = """
CREATE TABLE IF NOT EXISTS todo_list (
    id    INTEGER NOT NULL UNIQUE,
    task_name TEXT,
    type TEXT,
    active INTEGER,

    PRIMARY KEY("id")
);
"""

cur.execute(sql)
#CREATE
def create_todo(id, task_name: str, todo_type: str, active: bool):
    create_todo_sql = f"""
    INSERT INTO todo_list VALUES({id}, '{task_name}', '{todo_type}', {active})
    """
    cur.execute(create_todo_sql)
    con.commit()

#READ
def get_all_active_todos():
    pass

def get_all_todos():
    read_all_sql = """
    SELECT * FROM todo_list
    """
    read_all_query = cur.execute(read_all_sql)
    result = read_all_query.fetchall()
    return result

#UPDATE
def update_todo(id: int, task_name: str, todo_type: str, active: int):
    update_sql = f"""
    UPDATE todo_list
    SET task_name = '{task_name}', type = '{todo_type}', active = {active}
    WHERE id = {id}
    """
    cur.execute(update_sql)
    con.commit()

#DELETE
def delete_todo(id):
    delete_sql = f"""
    DELETE FROM todo_list WHERE id = {id}
    """
    cur.execute(delete_sql)
    con.commit()
