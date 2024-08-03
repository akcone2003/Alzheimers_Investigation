# Data Dictionary
## Patient Information
* __PatientID__: A unique identifier assigned to each patient (4751 to 6900).
<br>
## Demographic Details
* __Age__: The age of the patients ranges from 60 to 90 years.
* __Gender__: Gender of the patients, where 0 represents Male and 1 represents Female.
* __Ethnicity__: The ethnicity of the patients, coded as follows:
    * 0: Caucasian
    * 1: African American
    * 2: Asian
    * 3: Other
* __EducationLevel__: The education level of the patients, coded as follows:
    * 0: None
    * 1: High School
    * 2: Bachelor's
    * 3: Higher
<br>
## Lifestyle Factors
* __BMI__: Body Mass Index of the patients, ranging from 15 to 40.
* __Smoking__: Smoking status, where 0 indicates No and 1 indicates Yes.
* __AlcoholConsumption__: Weekly alcohol consumption in units, ranging from 0 to 20.
* __PhysicalActivity__: Weekly physical activity in hours, ranging from 0 to 10.
* __DietQuality__: Diet quality score, ranging from 0 to 10.
* __SleepQuality__: Sleep quality score, ranging from 4 to 10.
<br>
## Medical History
* __FamilyHistoryAlzheimers__: Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
* __CardiovascularDisease__: Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.
* __Diabetes__: Presence of diabetes, where 0 indicates No and 1 indicates Yes.
* __Depression__: Presence of depression, where 0 indicates No and 1 indicates Yes.
* __HeadInjury__: History of head injury, where 0 indicates No and 1 indicates Yes.
* __Hypertension__: Presence of hypertension, where 0 indicates No and 1 indicates Yes.
## Clinical Measurements
* __SystolicBP__: Systolic blood pressure, ranging from 90 to 180 mmHg.
* __DiastolicBP__: Diastolic blood pressure, ranging from 60 to 120 mmHg.
* __CholesterolTotal__: Total cholesterol levels, ranging from 150 to 300 mg/dL.
* __CholesterolLDL__: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
* __CholesterolHDL__: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
* __CholesterolTriglycerides__: Triglycerides levels, ranging from 50 to 400 mg/dL.
## Cognitive and Functional Assessments
* __MMSE__: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
* __FunctionalAssessment__: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
* __MemoryComplaints__: Presence of memory complaints, where 0 indicates No and 1 indicates Yes.
* __BehavioralProblems__: Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.
* __ADL__: Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.
## Symptoms
* __Confusion__: Presence of confusion, where 0 indicates No and 1 indicates Yes.
* __Disorientation__: Presence of disorientation, where 0 indicates No and 1 indicates Yes.
* __PersonalityChanges__: Presence of personality changes, where 0 indicates No and 1 indicates Yes.
* __DifficultyCompletingTasks__: Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.
* __Forgetfulness__: Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.
## Diagnosis Information
* __Diagnosis__: Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
## Confidential Information
* __DoctorInCharge__: This column contains confidential information about the doctor in charge, with "XXXConfid" as the value for all patients.
