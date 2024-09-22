from pygame.sysfont import SysFont
from enum import Enum


class FontType(Enum):
    TEXT = 'text'
    BUTTON = 'button'


class FontSize(Enum):
    MEDIUM = 'medium'
    LARGE = 'large'


def get_default_sys_font(type: FontType, size: FontSize):
    selected_font = _default_fonts[type]
    return SysFont(selected_font['font'], selected_font['sizes'][size])


def get_default_font(type: FontType):
    return _default_fonts[type]['font']


_default_fonts = {
    FontType.TEXT: {
        'font': 'Arial',
        'sizes': {
            FontSize.MEDIUM: 32,
            FontSize.LARGE: 64
        }
    },
    FontType.BUTTON: {
        'font': 'Arial',
        'sizes': {
            FontSize.MEDIUM: 32,
            FontSize.LARGE: 64
        }
    }
}
