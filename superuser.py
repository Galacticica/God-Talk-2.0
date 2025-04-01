import sqlite3


def make_user_admin(user_id):
    conn = sqlite3.connect('db.sqlite3')
    sql = ''' UPDATE accounts_user
              SET is_superuser = 1,
                  is_staff = 1
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    user_id = input("Enter the user id: ") 
    make_user_admin(user_id)
    print(f"User with ID {user_id} has been made admin.")