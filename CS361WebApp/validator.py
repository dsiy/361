from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError(
            _('data must not contain numbers or symbols')
        )


def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError(
            _('data must be comprised only of numbers')
        )
