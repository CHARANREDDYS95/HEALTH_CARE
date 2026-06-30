import os


class ConfigReader:

    @staticmethod
    def get(
        file_name,
        key
    ):

        file_path = os.path.join(
            os.path.dirname(__file__),
            file_name
        )

        with open(
            file_path,
            "r"
        ) as file:

            for line in file:

                line = line.strip()

                if (
                    line == ""
                    or
                    line.startswith("#")
                ):

                    continue

                config_key, config_value = line.split(
                    "=",
                    1
                )

                if config_key.strip() == key:

                    return config_value.strip()

        raise ValueError(
            f"{key} NOT FOUND IN {file_name}"
        )