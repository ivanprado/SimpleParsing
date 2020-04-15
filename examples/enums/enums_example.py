import enum
from dataclasses import dataclass
from typing import List, Tuple

from simple_parsing import ArgumentParser, field, list_field


class Temperature(enum.Enum):
    HOT = 1
    WARM = 0
    COLD = -1
    MONTREAL = -35


class Color(enum.Enum):
    RED = "RED"
    ORANGE = "ORANGE"
    BLUE = "BLUE"
    MAGENTA = "MAGENTA"

from typing import Type
def possible_str(some_enum: Type[enum.Enum]) -> str:
    names: List[str] = [f"'{e.name}'" for e in some_enum]
    return "(Possible: {" + ", ".join(names) + "})"

@dataclass
class MyPreferences:
    """You can use Enums"""
    color: Color = Color.BLUE # my favorite colour
    # A list of colors I hate.
    hated_colors: List[Color] = list_field(
        Color.MAGENTA, Color.ORANGE, # the default values, if any.
        help=f"Some Colors I hate. {possible_str(Color)}",
    )

parser = ArgumentParser()
parser.add_arguments(MyPreferences, "my_preferences")


args = parser.parse_args()
prefs: MyPreferences = args.my_preferences
print(prefs)

expected = """\
MyPreferences(color=<Color.BLUE: 'BLUE'>, hated_colors=[<Color.MAGENTA: 'MAGENTA'>, <Color.ORANGE: 'ORANGE'>])
"""

# Example where a value is passed:
args = parser.parse_args("--hated_colors ORANGE".split())
print(args.my_preferences)

expected += """\
MyPreferences(color=<Color.BLUE: 'BLUE'>, hated_colors=[<Color.ORANGE: 'ORANGE'>])
"""

# Nicely formatted help string:
parser.print_help()
expected += """\
usage: enums_example.py [-h] [--color {RED,ORANGE,BLUE,MAGENTA}]
                        [--hated_colors [Color [Color ...]]]

optional arguments:
  -h, --help            show this help message and exit

MyPreferences ['my_preferences']:
  You can use Enums

  --color {RED,ORANGE,BLUE,MAGENTA}
                        my favorite colour (default: BLUE)
  --hated_colors [Color [Color ...]]
                        Some Colors I hate. (Possible: {'RED', 'ORANGE',
                        'BLUE', 'MAGENTA'}) (default: [<Color.MAGENTA:
                        'MAGENTA'>, <Color.ORANGE: 'ORANGE'>])
"""
