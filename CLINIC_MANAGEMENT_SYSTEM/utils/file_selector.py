import os


class FileSelector:

    @staticmethod
    def get_files(
        folder,
        extension
    ):

        files = []

        if not os.path.exists(
            folder
        ):

            return files

        for file in os.listdir(
            folder
        ):

            if file.lower().endswith(
                extension.lower()
            ):

                files.append(
                    file
                )

        files.sort()

        return files

    @staticmethod
    def select_files(
        folder,
        extension,
        file_type
    ):

        while True:

            files = FileSelector.get_files(
                folder,
                extension
            )

            if not files:

                print(
                    f"\nNO {file_type} FILES FOUND."
                )

                return None

            print("\n========================================")
            print(
                f"      AVAILABLE {file_type} FILES"
            )
            print("========================================")

            for index, file in enumerate(
                files,
                start=1
            ):

                print(
                    f"{index}. {file}"
                )

            print()
            print("A. IMPORT ALL")
            print("B. BACK")

            choice = input(
                "\nENTER CHOICE : "
            ).strip().upper()

            if choice == "B":

                return None

            if choice == "A":

                return [

                    os.path.join(
                        folder,
                        file
                    )

                    for file in files

                ]

            try:

                selected = []

                used = set()

                for value in choice.split(","):

                    value = value.strip()

                    index = int(
                        value
                    )

                    if index < 1 or index > len(files):

                        raise ValueError

                    if index in used:

                        continue

                    used.add(
                        index
                    )

                    selected.append(

                        os.path.join(

                            folder,

                            files[
                                index - 1
                            ]

                        )

                    )

                return selected

            except ValueError:

                print(
                    "\nINVALID CHOICE. PLEASE TRY AGAIN."
                )