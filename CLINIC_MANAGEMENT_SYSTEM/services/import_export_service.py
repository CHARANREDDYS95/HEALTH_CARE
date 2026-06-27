from connection import get_session
from sqlalchemy import select
from models.patient_master import PatientMaster
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