from datetime import datetime
from datetime import timedelta
from config.config_reader import ConfigReader


class AppointmentSlotGenerator:
    @staticmethod
    def get_session_duration(
        start_time,
        end_time
    ):

        start = datetime.strptime(

            start_time,

            "%I:%M %p"

        )

        end = datetime.strptime(

            end_time,

            "%I:%M %p"

        )

        duration = int(

            (

                end -

                start

            ).total_seconds()

            // 60

        )

        return duration
    
    @staticmethod
    def calculate_slot_distribution(
        session_duration,
        consultation_duration
    ):

        if consultation_duration <= 0:

            raise ValueError(
                "INVALID CONSULTATION DURATION"
            )

        max_patients = (

            session_duration //

            consultation_duration

        )

        if max_patients <= 0:

            raise ValueError(
                "SESSION DURATION IS TOO SHORT"
            )

        distributed_minutes = (

            session_duration %

            consultation_duration

        )

        slot_durations = [

            consultation_duration

            for _ in range(
                max_patients
            )

        ]

        for index in range(

            distributed_minutes

        ):

            slot_durations[
                index
            ] += 1

        return {

            "session_duration":

            session_duration,

            "consultation_duration":

            consultation_duration,

            "max_patients":

            max_patients,

            "distributed_minutes":

            distributed_minutes,

            "slot_durations":

            slot_durations

        }
            
    @staticmethod
    def generate_slots(
        start_time,
        end_time
    ):

        consultation_duration = int(

            ConfigReader.get(

                "consultation_duration.txt",

                "CONSULTATION_DURATION"

            )

        )

        session_duration = (

            AppointmentSlotGenerator.get_session_duration(

                start_time,

                end_time

            )

        )

        slot_details = (

            AppointmentSlotGenerator.calculate_slot_distribution(

                session_duration,

                consultation_duration

            )

        )

        current_time = datetime.strptime(

            start_time,

            "%I:%M %p"

        )

        slots = []

        for index, duration in enumerate(

            slot_details[
                "slot_durations"
            ],

            start=1

        ):

            slot_start = current_time

            slot_end = (

                slot_start

                +

                timedelta(

                    minutes=duration

                )

            )

            slots.append({

                "slot_no":

                index,

                "start_time":

                slot_start.strftime(

                    "%I:%M %p"

                ),

                "end_time":

                slot_end.strftime(

                    "%I:%M %p"

                ),

                "duration":

                duration

            })

            current_time = slot_end

        return {

            "session_duration":

            slot_details[
                "session_duration"
            ],

            "consultation_duration":

            slot_details[
                "consultation_duration"
            ],

            "max_patients":

            slot_details[
                "max_patients"
            ],

            "distributed_minutes":

            slot_details[
                "distributed_minutes"
            ],

            "slots":

            slots

        }