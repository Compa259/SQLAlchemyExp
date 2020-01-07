import configparser
import sqlalchemy


def create_engine():
    config = configparser.ConfigParser()
    config.read('../cnf.ini')

    HOST = config.get('mysql', 'host')
    USER = config.get('mysql', 'user')
    PASSWD = config.get('mysql', 'passwd')
    DB = config.get('mysql', 'db')

    # Create engine to connect DB using MySQL Connector/Python
    conn_str = 'mysql+mysqlconnector://{0}:{1}@{2}:3306/{3}' \
        .format(USER, PASSWD, HOST, DB)
    engine = sqlalchemy.create_engine(
        conn_str,
        echo=False
    )
    return engine
