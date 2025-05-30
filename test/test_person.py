# coding: utf-8

"""
    My API

    Description of my API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hseagent_sdk.models.person import Person

class TestPerson(unittest.TestCase):
    """Person unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Person:
        """Test Person
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Person`
        """
        model = Person()
        if include_optional:
            return Person(
                id = 56,
                department = '',
                role = '',
                status = '',
                first_name = '',
                last_name = '',
                father_name = '',
                gender = 'male',
                national_code = '',
                insurance_code = '',
                employee_code = '',
                birthdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                education_level = None,
                marital_status = None,
                number_of_children = 0,
                military_service = None,
                exemption_reason = '',
                is_active = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = 56
            )
        else:
            return Person(
                id = 56,
                department = '',
                role = '',
                status = '',
                first_name = '',
                last_name = '',
                father_name = '',
                gender = 'male',
                national_code = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = 56,
        )
        """

    def testPerson(self):
        """Test Person"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
