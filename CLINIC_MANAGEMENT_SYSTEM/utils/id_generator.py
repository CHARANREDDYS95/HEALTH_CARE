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
        
def get_next_id(
    table_name,
    column_name,
    prefix,
    next_number=None
):

    if next_number is None:

        session = get_session()

        try:

            query = text(
                f"""
                SELECT MAX({column_name})
                FROM {table_name}
                """
            )

            result = session.execute(
                query
            ).scalar()

            if result is None:

                next_number = 1

            else:

                next_number = (

                    int(

                        result.replace(
                            prefix,
                            ""
                        )

                    )

                    + 1

                )

        finally:

            session.close()

    generated_id = (

        f"{prefix}{next_number:03d}"

    )

    return (

        generated_id,

        next_number + 1

    )
