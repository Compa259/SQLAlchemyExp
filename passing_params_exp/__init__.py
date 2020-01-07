import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:123456@localhost:3306/sqlalchemy',
    echo=False
)

connection = engine.raw_connection()
try:
    cursor = connection.cursor()
    cursor.callproc('GetUsersByAge', [25])
    # fetch result parameters
    for result in cursor.stored_results():
        people = result.fetchall()

    for user in people:
        print(user)
    cursor.close()
    connection.commit()
finally:
    connection.close()
