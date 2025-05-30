# coding: utf-8

"""
    My API

    Description of my API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hseagent_sdk.models.action_ai import ActionAI

class TestActionAI(unittest.TestCase):
    """ActionAI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionAI:
        """Test ActionAI
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionAI`
        """
        model = ActionAI()
        if include_optional:
            return ActionAI(
                id = 56,
                action_type = hseagent_sdk.models.observation_type.ObservationType(
                    id = 56, 
                    sections = [
                        hseagent_sdk.models.section.Section(
                            id = 56, 
                            name = '', 
                            code = '', 
                            description = '', 
                            section_type = hseagent_sdk.models.section_type.SectionType(
                                id = 56, 
                                name = '', 
                                code = '', 
                                description = '', ), )
                        ], 
                    name = '', 
                    description = '', 
                    code = '', 
                    required = True, 
                    schema = null, 
                    value_type = null, 
                    category = null, 
                    unit = '', 
                    hint = '', 
                    examination_types = [
                        hseagent_sdk.models.examination_type.ExaminationType(
                            id = 56, 
                            name = '', 
                            parent = '', 
                            description = '', 
                            code = '', )
                        ], ),
                person = 56,
                based_on_examination = hseagent_sdk.models.examination.Examination(
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
                        ], ),
                based_on_report = hseagent_sdk.models.hse_report.HSEReport(
                    id = 56, 
                    person = 56, 
                    physician_id = 56, 
                    physician = null, 
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
                    final_opinion = null, 
                    recommendations = '', 
                    status = null, 
                    report_file = '', 
                    examination_ids = [
                        56
                        ], 
                    status_fa = '', 
                    actions = [
                        56
                        ], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                data = None,
                result = '',
                based_on_examination_id = 56,
                based_on_report_id = 56,
                status = 'hold',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_observation = '',
                target_examination = ''
            )
        else:
            return ActionAI(
                id = 56,
                action_type = hseagent_sdk.models.observation_type.ObservationType(
                    id = 56, 
                    sections = [
                        hseagent_sdk.models.section.Section(
                            id = 56, 
                            name = '', 
                            code = '', 
                            description = '', 
                            section_type = hseagent_sdk.models.section_type.SectionType(
                                id = 56, 
                                name = '', 
                                code = '', 
                                description = '', ), )
                        ], 
                    name = '', 
                    description = '', 
                    code = '', 
                    required = True, 
                    schema = null, 
                    value_type = null, 
                    category = null, 
                    unit = '', 
                    hint = '', 
                    examination_types = [
                        hseagent_sdk.models.examination_type.ExaminationType(
                            id = 56, 
                            name = '', 
                            parent = '', 
                            description = '', 
                            code = '', )
                        ], ),
                based_on_examination = hseagent_sdk.models.examination.Examination(
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
                        ], ),
                based_on_report = hseagent_sdk.models.hse_report.HSEReport(
                    id = 56, 
                    person = 56, 
                    physician_id = 56, 
                    physician = null, 
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
                    final_opinion = null, 
                    recommendations = '', 
                    status = null, 
                    report_file = '', 
                    examination_ids = [
                        56
                        ], 
                    status_fa = '', 
                    actions = [
                        56
                        ], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                result = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_observation = '',
                target_examination = '',
        )
        """

    def testActionAI(self):
        """Test ActionAI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
