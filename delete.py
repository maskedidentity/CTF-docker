import sqlite3
def delete_user_by_id():
  conn = sqlite3.connect('db.sqlite3')
  cursor = conn.cursor()
  while True:
    table_name=input("tablename adik without error or 't to quit:")
    if table_name.lower()=='t':
       break
    try:
        while True:
            user_id = input("id para vazhe or q adik to erajhal from this table:")
            if user_id.lower() == 'q':
                break
            try:
                cursor.execute(f"DELETE FROM {table_name} WHERE id={int(user_id)};")
                conn.commit()
                print(f"UserID {user_id} delete akind....ini?")
            except ValueError:
                print(f"ee ID thetta:'{user_id}'.crt adik  :/  ")
    except ValueError:
        print(f"table name thetta")
    conn.close()
delete_user_by_id()

# import sqlite3
# def delete_user_by_id():
#   conn = sqlite3.connect('db.sqlite3')
#   cursor = conn.cursor()
#   while True:
#     table_name=input("tablename adik without error or 't to quit:")
#     if table_name.lower()=='t':
#        while True:
#             user_id = input("id para vazhe or q adik to erajhal from this table:")
#             if user_id.lower() == 'q':
#                 break
#             try:
#                 cursor.execute(f"DELETE FROM {table_name} WHERE id={int(user_id)};")
#                 conn.commit()
#                 print(f"UserID {user_id} delete akind....ini?")
#             except ValueError:
#                 print(f"ee ID thetta:'{user_id}'.crt adik  :/  ")
#     except ValueError:
#         print(f"table name thetta")
#         conn.close()
# delete_user_by_id()

