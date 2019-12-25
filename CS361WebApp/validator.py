from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError(
            _('data must not contain numbers or symbols')
        )
        return False
    return True


def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError(
            _('data must be comprised only of numbers')
        )
        return False
    return True


def validate_course(course):
    if validate_alpha(course.department):
        if validate_numeric(course.number):
            if validate_numeric(course.section):
                if validate_alpha(course.day):
                    return True
    return False
