from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_bags(value):
    if value % 0.5 or value < 1 or value > 2:
        print(value)
        raise ValidationError(
            _("%(value)s is not allowable."),
            params={"value": value},
        )


