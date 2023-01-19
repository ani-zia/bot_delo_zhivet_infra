from bot.handlers.state_constants import (
    ADDING_VOLUNTEER,
    END,
    SPECIFY_ACTIVITY_RADIUS,
    SPECIFY_CAR_AVAILABILITY,
    SPECIFY_CITY,
)

BASE_PATTERN = "^({command})$"

REPORT_SOCIAL_PROBLEM_CMD = BASE_PATTERN.format(command="Сообщить о социальной проблеме")
REPORT_ECO_PROBLEM_CMD = BASE_PATTERN.format(command="Сообщить о экологической проблеме")
BECOME_VOLUNTEER_CMD = BASE_PATTERN.format(command=ADDING_VOLUNTEER)
MAKE_DONATION_CMD = BASE_PATTERN.format(command="Сделать пожертвование")
SPECIFY_CITY_CMD = BASE_PATTERN.format(command="Указать город")
END_CMD = BASE_PATTERN.format(command=END)

SPECIFY_CITY_CMD = BASE_PATTERN.format(command=SPECIFY_CITY)
SPECIFY_ACTIVITY_RADIUS_CMD = BASE_PATTERN.format(command=SPECIFY_ACTIVITY_RADIUS)
SPECIFY_CAR_AVAILABILITY_CMD = BASE_PATTERN.format(command=SPECIFY_CAR_AVAILABILITY)
