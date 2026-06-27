from sqlalchemy import func
from sqlalchemy import select

from connection import get_session

from models.doctor_master import DoctorMaster
from models.doctor_availability import DoctorAvailability
from models.appointment_master import AppointmentMaster
from models.patient_master import PatientMaster
from models.consultation_master import ConsultationMaster
from models.billing_master import BillingMaster


class ReportsService:

    @staticmethod
    def doctor_wise_appointment_count():

        session = get_session()

        try:

            records = session.execute(

                select(

                    DoctorMaster.doctor_id,

                    DoctorMaster.doctor_name,

                    func.count(
                        AppointmentMaster.appointment_id
                    ).label(
                        "appointment_count"
                    )

                )

                .join(

                    DoctorAvailability,

                    DoctorMaster.doctor_id
                    ==
                    DoctorAvailability.doctor_id

                )

                .join(

                    AppointmentMaster,

                    DoctorAvailability.availability_id
                    ==
                    AppointmentMaster.availability_id

                )

                .group_by(

                    DoctorMaster.doctor_id,

                    DoctorMaster.doctor_name

                )

                .order_by(

                    DoctorMaster.doctor_id

                )

            ).all()

            report = []

            for record in records:

                report.append(

                    {

                        "Doctor ID":
                        record.doctor_id,

                        "Doctor Name":
                        record.doctor_name,

                        "Appointment Count":
                        record.appointment_count

                    }

                )

            return report

        finally:

            session.close()

    @staticmethod
    def city_wise_patient_count():

        session = get_session()

        try:

            records = session.execute(

                select(

                    PatientMaster.city,

                    func.count(
                        PatientMaster.patient_id
                    ).label(
                        "patient_count"
                    )

                )

                .group_by(

                    PatientMaster.city

                )

                .order_by(

                    PatientMaster.city

                )

            ).all()

            report = []

            for record in records:

                report.append(

                    {

                        "City":
                        record.city,

                        "Patient Count":
                        record.patient_count

                    }

                )

            return report

        finally:

            session.close()
            
    @staticmethod
    def doctor_wise_revenue():

        session = get_session()

        try:

            records = session.execute(

                select(

                    DoctorMaster.doctor_id,

                    DoctorMaster.doctor_name,

                    func.sum(
                        BillingMaster.total_amount
                    ).label(
                        "total_revenue"
                    )

                )

                .join(

                    DoctorAvailability,

                    DoctorMaster.doctor_id
                    ==
                    DoctorAvailability.doctor_id

                )

                .join(

                    AppointmentMaster,

                    DoctorAvailability.availability_id
                    ==
                    AppointmentMaster.availability_id

                )

                .join(

                    ConsultationMaster,

                    AppointmentMaster.appointment_id
                    ==
                    ConsultationMaster.appointment_id

                )

                .join(

                    BillingMaster,

                    ConsultationMaster.consultation_id
                    ==
                    BillingMaster.consultation_id

                )

                .group_by(

                    DoctorMaster.doctor_id,

                    DoctorMaster.doctor_name

                )

                .order_by(

                    DoctorMaster.doctor_id

                )

            ).all()

            report = []

            for record in records:

                report.append(

                    {

                        "Doctor ID":
                        record.doctor_id,

                        "Doctor Name":
                        record.doctor_name,

                        "Revenue":
                        float(
                            record.total_revenue
                        )

                    }

                )

            return report

        finally:

            session.close()
            
    @staticmethod
    def daily_appointment_summary():

        session = get_session()

        try:

            records = session.execute(

                select(

                    AppointmentMaster.appointment_status,

                    func.count(
                        AppointmentMaster.appointment_id
                    ).label(
                        "appointment_count"
                    )

                )

                .group_by(

                    AppointmentMaster.appointment_status

                )

                .order_by(

                    AppointmentMaster.appointment_status

                )

            ).all()

            report = []

            for record in records:

                report.append(

                    {

                        "Appointment Status":
                        record.appointment_status,

                        "Count":
                        record.appointment_count

                    }

                )

            return report

        finally:

            session.close()