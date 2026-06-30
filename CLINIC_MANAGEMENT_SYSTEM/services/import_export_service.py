from connection import get_session
from sqlalchemy import select
from models.patient_master import PatientMaster
from models.doctor_master import DoctorMaster
from utils.import_helper import ImportHelper
from utils.export_helper import ExportHelper
from utils.validators import (
    validate_required,
    validate_phone,
    validate_gender,
    validate_blood_group,
    validate_date_not_future)
from utils.date_utils import (DateUtils)
from utils.id_generator import generate_id



class ImportExportService:

    IMPORT_FOLDER = (
        "imports/patients"
    )

    EXPORT_FOLDER = (
        "downloads/exports"
    )
    EXPORT_FILE_NAME = (
        "PATIENTS"
    )
    
    DOCTOR_IMPORT_FOLDER = (
        "imports/doctors"
    )

    DOCTOR_EXPORT_FILE_NAME = (
        "DOCTORS"
    )


    @staticmethod
    def _import_patient_record(
        record,
        session
    ):

        record = {

            key:

            value.strip()

            if isinstance(
                value,
                str
            )

            else value

            for key, value in record.items()

        }

        patient_name = record.get(
            "PATIENT_NAME"
        )

        validate_required(
            patient_name,
            "Patient Name"
        )

        gender = record.get(
            "GENDER"
        )

        phone = record.get(
            "PHONE"
        )

        blood_group = record.get(
            "BLOOD_GROUP"
        )
        
        address = record.get(
            "ADDRESS"
        )

        city = record.get(
            "CITY"
        )

        occupation = record.get(
            "OCCUPATION"
        )

        marital_status = record.get(
            "MARITAL_STATUS"
        )

        allergies = record.get(
            "ALLERGIES"
        )

        emergency_contact_name = record.get(
            "EMERGENCY_CONTACT_NAME"
        )
        
        emergency_phone = record.get(
            "EMERGENCY_PHONE"
        )

        dob = DateUtils.parse_date(

            record.get(
                "DOB"
            )

        )

        validate_required(
            phone,
            "Phone"
        )

        validate_required(
            gender,
            "Gender"
        )

        validate_phone(
            phone
        )

        validate_gender(
            gender
        )

        if blood_group:

            validate_blood_group(
                blood_group
            )

        phone_exists = session.execute(
            select(
                PatientMaster
            ).where(
                PatientMaster.phone
                ==
                phone
            )
        ).scalar_one_or_none()

        if phone_exists:

            raise ValueError(
                "PHONE NUMBER ALREADY EXISTS"
            )
            
        validate_date_not_future(
            dob
        )
        
        patient = PatientMaster(

            patient_id=generate_id(
                "PATIENT_MASTER",
                "PATIENT_ID",
                "P"
            ),

            patient_name=patient_name,

            gender=gender,

            dob=dob,

            phone=phone,

            address=address,

            city=city,

            blood_group=blood_group,

            occupation=occupation,

            marital_status=marital_status,

            allergies=allergies,

            emergency_contact_name=emergency_contact_name,

            emergency_phone=emergency_phone,

            registration_date=DateUtils.today(),

            patient_status="ACTIVE"

        )

        session.add(
            patient
        )
        
    @staticmethod
    def _import_doctor_record(
        record,
        session
    ):

        record = {

            key:

            value.strip()

            if isinstance(
                value,
                str
            )

            else value

            for key, value in record.items()

        }

        doctor_name = record.get(
            "DOCTOR_NAME"
        )

        gender = record.get(
            "GENDER"
        )

        dob = DateUtils.parse_date(

            record.get(
                "DOB"
            )

        )

        specialization = record.get(
            "SPECIALIZATION"
        )

        qualification = record.get(
            "QUALIFICATION"
        )

        license_no = record.get(
            "LICENSE_NO"
        )

        experience_years = record.get(
            "EXPERIENCE_YEARS"
        )

        phone = record.get(
            "PHONE"
        )

        email = record.get(
            "EMAIL"
        )

        address = record.get(
            "ADDRESS"
        )

        consultation_fee = record.get(
            "CONSULTATION_FEE"
        )

        consultation_duration = record.get(
            "CONSULTATION_DURATION"
        )
        
        validate_required(
            doctor_name,
            "Doctor Name"
        )

        validate_required(
            gender,
            "Gender"
        )

        validate_required(
            specialization,
            "Specialization"
        )

        validate_required(
            qualification,
            "Qualification"
        )

        validate_required(
            license_no,
            "License Number"
        )

        validate_required(
            phone,
            "Phone"
        )

        validate_required(
            experience_years,
            "Experience Years"
        )

        validate_required(
            consultation_fee,
            "Consultation Fee"
        )

        validate_required(
            consultation_duration,
            "Consultation Duration"
        )

        validate_phone(
            phone
        )

        validate_gender(
            gender
        )

        validate_date_not_future(
            dob
        )
        
        phone_exists = session.execute(
            select(
                DoctorMaster
            ).where(
                DoctorMaster.phone
                ==
                phone
            )
        ).scalar_one_or_none()

        if phone_exists:

            raise ValueError(
                "PHONE NUMBER ALREADY EXISTS"
            )
            
        if email:

            email_exists = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.email
                    ==
                    email
                )
            ).scalar_one_or_none()

            if email_exists:

                raise ValueError(
                    "EMAIL ALREADY EXISTS"
                )

        license_exists = session.execute(
            select(
                DoctorMaster
            ).where(
                DoctorMaster.license_no
                ==
                license_no
            )
        ).scalar_one_or_none()

        if license_exists:

            raise ValueError(
                "LICENSE NUMBER ALREADY EXISTS"
            )

        doctor = DoctorMaster(

            doctor_id=generate_id(
                "DOCTOR_MASTER",
                "DOCTOR_ID",
                "D"
            ),

            doctor_name=doctor_name,

            gender=gender,

            dob=dob,

            specialization=specialization,

            qualification=qualification,

            license_no=license_no,

            experience_years=int(
                experience_years
            ),

            phone=phone,

            email=email,

            address=address,

            consultation_fee=float(
                consultation_fee
            ),

            consultation_duration=int(
                consultation_duration
            ),

            doctor_status="ACTIVE",

            joining_date=DateUtils.today()

        )

        session.add(
            doctor
        )
        
    @staticmethod
    def import_patients(
        file_path,
        file_format
    ):

        session = get_session()

        imported = 0

        skipped = 0

        errors = []

        try:

            file_format = (
                file_format.upper()
            )

            if file_format == "CSV":

                records = (
                    ImportHelper.import_from_csv(
                        file_path
                    )
                )

            elif file_format == "EXCEL":

                records = (
                    ImportHelper.import_from_excel(
                        file_path
                    )
                )

            elif file_format == "JSON":

                records = (
                    ImportHelper.import_from_json(
                        file_path
                    )
                )

            elif file_format == "TXT":

                records = (
                    ImportHelper.import_from_txt(
                        file_path
                    )
                )

            else:

                raise ValueError(
                    "INVALID FILE FORMAT"
                )

            total = len(
                records
            )

            for index, record in enumerate(
                records,
                start=1
            ):

                try:

                    with session.begin_nested():

                        ImportExportService._import_patient_record(
                            record,
                            session
                        )

                        session.flush()

                    imported += 1

                except Exception as e:

                    skipped += 1

                    errors.append(

                        f"ROW {index} : {e}"

                    )

            session.commit()

            return {

                "total":
                total,

                "imported":
                imported,

                "skipped":
                skipped,

                "errors":
                errors

            }

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
            
    @staticmethod
    def import_doctors(
        file_path,
        file_format
    ):

        session = get_session()

        imported = 0

        skipped = 0

        errors = []

        try:

            file_format = (
                file_format.upper()
            )

            if file_format == "CSV":

                records = (
                    ImportHelper.import_from_csv(
                        file_path
                    )
                )

            elif file_format == "EXCEL":

                records = (
                    ImportHelper.import_from_excel(
                        file_path
                    )
                )

            elif file_format == "JSON":

                records = (
                    ImportHelper.import_from_json(
                        file_path
                    )
                )

            elif file_format == "TXT":

                records = (
                    ImportHelper.import_from_txt(
                        file_path
                    )
                )

            else:

                raise ValueError(
                    "INVALID FILE FORMAT"
                )

            total = len(
                records
            )

            for index, record in enumerate(
                records,
                start=1
            ):

                try:

                    with session.begin_nested():

                        ImportExportService._import_doctor_record(
                            record,
                            session
                        )

                        session.flush()

                    imported += 1

                except Exception as e:

                    skipped += 1

                    errors.append(

                        f"ROW {index} : {e}"

                    )

            session.commit()

            return {

                "total":
                total,

                "imported":
                imported,

                "skipped":
                skipped,

                "errors":
                errors

            }

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
            
    @staticmethod
    def export_patients(
        file_format
    ):

        session = get_session()

        try:

            patients = session.execute(
                select(
                    PatientMaster
                )
            ).scalars().all()

            records = []

            for patient in patients:

                records.append({

                    "PATIENT_ID":
                    patient.patient_id,

                    "PATIENT_NAME":
                    patient.patient_name,

                    "GENDER":
                    patient.gender,

                    "DOB":
                    DateUtils.format_date(
                        patient.dob
                    ),

                    "PHONE":
                    patient.phone,

                    "ADDRESS":
                    patient.address,

                    "CITY":
                    patient.city,

                    "BLOOD_GROUP":
                    patient.blood_group,

                    "OCCUPATION":
                    patient.occupation,

                    "MARITAL_STATUS":
                    patient.marital_status,

                    "ALLERGIES":
                    patient.allergies,

                    "EMERGENCY_CONTACT_NAME":
                    patient.emergency_contact_name,

                    "EMERGENCY_PHONE":
                    patient.emergency_phone,

                    "REGISTRATION_DATE":
                    DateUtils.format_date(
                        patient.registration_date
                    ),

                    "PATIENT_STATUS":
                    patient.patient_status

                })

            file_format = (
                file_format.upper()
            )

            if file_format == "CSV":

                return ExportHelper.export_to_csv(

                    records,
                    
                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.EXPORT_FILE_NAME

                )

            elif file_format == "EXCEL":

                return ExportHelper.export_to_excel(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.EXPORT_FILE_NAME

                )

            elif file_format == "JSON":

                return ExportHelper.export_to_json(

                    records,
                    
                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.EXPORT_FILE_NAME

                )

            elif file_format == "TXT":

                return ExportHelper.export_to_txt(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.EXPORT_FILE_NAME

                )

            else:

                raise ValueError(
                    "INVALID FILE FORMAT"
                )

        finally:

            session.close()
            
    @staticmethod
    def export_doctors(
        file_format
    ):

        session = get_session()

        try:

            doctors = session.execute(
                select(
                    DoctorMaster
                )
            ).scalars().all()

            records = []

            for doctor in doctors:

                records.append({

                    "DOCTOR_ID":
                    doctor.doctor_id,

                    "DOCTOR_NAME":
                    doctor.doctor_name,

                    "GENDER":
                    doctor.gender,

                    "DOB":
                    DateUtils.format_date(
                        doctor.dob
                    ),

                    "SPECIALIZATION":
                    doctor.specialization,

                    "QUALIFICATION":
                    doctor.qualification,

                    "LICENSE_NO":
                    doctor.license_no,

                    "EXPERIENCE_YEARS":
                    doctor.experience_years,

                    "PHONE":
                    doctor.phone,

                    "EMAIL":
                    doctor.email,

                    "ADDRESS":
                    doctor.address,

                    "CONSULTATION_FEE":
                    doctor.consultation_fee,

                    "CONSULTATION_DURATION":
                    doctor.consultation_duration,

                    "JOINING_DATE":
                    DateUtils.format_date(
                        doctor.joining_date
                    ),

                    "DOCTOR_STATUS":
                    doctor.doctor_status

                })

            file_format = (
                file_format.upper()
            )

            if file_format == "CSV":

                return ExportHelper.export_to_csv(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.DOCTOR_EXPORT_FILE_NAME

                )

            elif file_format == "EXCEL":

                return ExportHelper.export_to_excel(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.DOCTOR_EXPORT_FILE_NAME

                )

            elif file_format == "JSON":

                return ExportHelper.export_to_json(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.DOCTOR_EXPORT_FILE_NAME

                )

            elif file_format == "TXT":

                return ExportHelper.export_to_txt(

                    records,

                    ImportExportService.EXPORT_FOLDER,

                    ImportExportService.DOCTOR_EXPORT_FILE_NAME

                )

            else:

                raise ValueError(
                    "INVALID FILE FORMAT"
                )

        finally:

            session.close()