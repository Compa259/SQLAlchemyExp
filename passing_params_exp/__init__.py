import sys

sys.path.append('../')
import engine_factory

# Get database information
engine = engine_factory.create_engine()

connection = engine.raw_connection()
try:
    cursor = connection.cursor()
    cursor.callproc('GetUsersByAge', [24])
    # fetch result parameters
    for result in cursor.stored_results():
        people = result.fetchall()

    for user in people:
        print(user)
    cursor.close()
    connection.commit()
finally:
    connection.close()
