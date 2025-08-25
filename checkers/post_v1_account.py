from datetime import datetime

from hamcrest import (
    all_of,
    has_property,
    has_properties,
    instance_of,
    starts_with,
    equal_to,
    assert_that,
)


class PostV1Account:
    @classmethod
    def check_response_values(
            cls,
            response
    ):
        today = datetime.now().strftime('%Y-%m-%d')

        assert_that(
            response, all_of(
                has_property('resource', has_property('login', starts_with('pestov_test'))),
                has_property('resource', has_property('registration', instance_of(datetime))),
                has_property(
                    'resource', has_properties(
                        {
                            'rating': has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0)
                                }
                            )
                        }
                    )
                )
            )
        )
        assert_that(str(response.resource.registration), starts_with(today))
