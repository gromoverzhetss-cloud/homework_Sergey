from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[3] == 'app_users'

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1["name"] == "QA Студия 'ТестировщикЪ'"

def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"


def test_select_1_row_with_two_filtres():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company "
                        "WHERE \"is_active\" = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {"id": 65, "is_active": True})
    rows = result.mappings().all()

    assert len(rows) == 0

# Добавить компанию
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO company(\"name\") VALUES (:new_name)")
    connection.execute(sql, {"new_name":"Skipro"})
    transaction.commit()
    connection.close()

# обновить компанию
def test_updete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    connection.execute(sql, {"descr": 'New descr', "id": 8})
    transaction.commit()
    connection.close()

# Удалить компанию
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE id = :id")
    connection.execute(sql, {"id": 8})

    transaction.commit()
    connection.close()