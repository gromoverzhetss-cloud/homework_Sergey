from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:(мой пароль)@localhost:5432/Test S"
db = create_engine(db_connection_string)

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO users(\"user_email\") VALUES (:new_email)")
    connection.execute(sql, {"new_email":"Alex@test.com"})
    transaction.commit()
    connection.close()
    

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET subject_id = :id WHERE user_email = :user_email")
    connection.execute(sql, {"id": '10', "user_email": 'Alex@test.com'})
    transaction.commit()
    connection.close()
    

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_email = :user_email")
    connection.execute(sql, {"user_email": "Alex@test.com"})

    transaction.commit()
    connection.close()
