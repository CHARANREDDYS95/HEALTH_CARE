import os

from datetime import datetime


class ImportLog:

    LOG_FOLDER = (
        "downloads/import_logs"
    )

    @staticmethod
    def save_log(
        module_name,
        all_errors
    ):

        if not all_errors:

            return None

        os.makedirs(

            ImportLog.LOG_FOLDER,

            exist_ok=True

        )

        file_name = (

            f"{module_name.lower()}_import_log_"

            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"

            ".txt"

        )

        file_path = os.path.join(

            ImportLog.LOG_FOLDER,

            file_name

        )

        with open(

            file_path,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "=" * 60 + "\n"

            )

            file.write(

                f"{module_name.upper()} IMPORT LOG\n"

            )

            file.write(

                "=" * 60 + "\n\n"

            )

            for item in all_errors:

                file.write(

                    f"FILE : {item['file']}\n\n"

                )

                for error in item["errors"]:

                    file.write(

                        error + "\n"

                    )

                file.write(

                    "\n"
                )

        return file_path