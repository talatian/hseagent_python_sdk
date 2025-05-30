# coding: utf-8

"""
    My API

    Description of my API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hseagent_sdk.models.patched_hse_report import PatchedHSEReport

class TestPatchedHSEReport(unittest.TestCase):
    """PatchedHSEReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedHSEReport:
        """Test PatchedHSEReport
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedHSEReport`
        """
        model = PatchedHSEReport()
        if include_optional:
            return PatchedHSEReport(
                id = 56,
                person = 56,
                physician_id = 56,
                physician = hseagent_sdk.models.physician.Physician(
                    id = 56, 
                    first_name = '', 
                    last_name = '', 
                    gender = null, 
                    national_code = '', 
                    mobile = '09480728880', 
                    email = '', 
                    medical_code = '', 
                    specialty = '', 
                    is_active = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    occupational_clinic = 56, ),
                examinations = [
                    hseagent_sdk.models.examination.Examination(
                        id = 56, 
                        observations = [
                            hseagent_sdk.models.nested_observation.NestedObservation(
                                observation_type = null, 
                                observation_type_id = 56, 
                                value = '', 
                                note = '', 
                                based_on_observation_id = 56, 
                                based_on_examination_id = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        examination_type = null, 
                        examination_type_id = 56, 
                        person_id = 56, 
                        physician_id = 56, 
                        physician = null, 
                        note = '', 
                        interpretation = null, 
                        performed_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        actions = [
                            56
                            ], )
                    ],
                reason = '',
                final_opinion = 'no_restriction',
                recommendations = '',
                status = 'awaiting_clinic',
                report_file = '',
                examination_ids = [
                    56
                    ],
                status_fa = '',
                actions = [
                    56
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PatchedHSEReport(
        )
        """

    def testPatchedHSEReport(self):
        """Test PatchedHSEReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
