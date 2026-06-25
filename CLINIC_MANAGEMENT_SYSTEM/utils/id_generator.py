from sqlalchemy import text
from connection import get_session


def generate_id(table_name, column_name, prefix):
    session = get_session()

    try:
        query = text(f"""
            SELECT MAX({column_name})
            FROM {table_name}
        """)

        result = session.execute(query).scalar()

        if result is None:
            return f"{prefix}001"

        number = int(result.replace(prefix, ""))
        return f"{prefix}{number + 1:03d}"

    finally:
        session.close()