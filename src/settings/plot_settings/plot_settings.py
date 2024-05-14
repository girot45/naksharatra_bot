# -*- coding: utf-8 -*-
class Preamble:

    # Этот код представляет собой преамбулу LaTeX-документа.
    # Преамбула - это область документа, которая находится
    # перед началом основного текста и содержит настройки
    # форматирования, подключение пакетов и определение
    # пользовательских команд.
    #
    # \usepackage{fontspec} - Подключение пакета fontspec,
    # который позволяет использовать системные шрифты в LaTeX.
    #
    # \usepackage{polyglossia} - Подключение пакета polyglossia,
    # который предоставляет поддержку многоязычности в LaTeX.
    #
    # \usepackage[T1]{fontenc} - Установка кодировки шрифта в T1,
    # что позволяет использовать латинские символы в тексте.
    #
    # \usepackage{tikz} - Подключение пакета tikz для создания графики и изображений в LaTeX.
    #
    # \usepackage{amsmath} - Подключение пакета amsmath,
    # который предоставляет расширенные математические возможности.
    #
    # \setmainlanguage{english} - Установка английского языка
    # как основного.
    #
    # \setotherlanguage{russian} - Установка русского языка
    # как дополнительного.
    #
    # \setmainfont{Times New Roman} - Установка Times New Roman
    # в качестве основного шрифта.
    #
    # \setromanfont{Times New Roman} - Установка Times New Roman
    # в качестве шрифта для латинских символов.
    #
    # \setsansfont{Arial} - Установка Arial в качестве шрифта без засечек.
    #
    # \setmonofont{Courier New} - Установка Courier New
    # в качестве моноширинного шрифта.
    #
    # \newfontfamily{\cyrillicfont}{Times New Roman} - Определение нового шрифта
    # для кириллических символов.
    #
    # \newfontfamily{\cyrillicfontrm}{Times New Roman} - Определение нового шрифта
    # для кириллических символов в режиме обычного текста.
    #
    # \newfontfamily{\cyrillicfonttt}{Courier New} - Определение нового шрифта
    # для кириллических символов в моноширинном режиме.
    #
    # \newfontfamily{\cyrillicfontsf}{Arial} - Определение нового шрифта
    # для кириллических символов без засечек.
    #
    # \newcommand{\sam}[1]{\text{#1}} - Определение новой команды \sam,
    # которая выводит свой аргумент как обычный текст.


    preamble = (r"\usepackage{fontspec}"
                r"\usepackage{polyglossia}"
                r"\usepackage[T1]{fontenc}"
                r"\usepackage{tikz}"
                r"\usepackage{amsmath}"
                r"\setmainlanguage{english}"
                r"\setotherlanguage{russian}"
                r"\setmainfont{Times New Roman}"
                r"\setromanfont{Times New Roman}"
                r"\setsansfont{Arial}"
                r"\setmonofont{Courier New}"
                r"\newfontfamily{\cyrillicfont}{Times New Roman}"
                r"\newfontfamily{\cyrillicfontrm}{Times New Roman}"
                r"\newfontfamily{\cyrillicfonttt}{Courier New}"
                r"\newfontfamily{\cyrillicfontsf}{Arial}"
                r"\newcommand{\sam}[1]{\text{#1}}")

class PlotSettings:
    """
    Класс PlotSettings

    Назначение: класс PlotSettings используется для хранения настроек графика.

    Инициализация:

    bg: цвет фона графика, по умолчанию — dark_background.
    outer_radial_lines_colour: цвет внешних радиальных линий, по умолчанию — #fff.
    inner_radial_lines_colour: цвет внутренних радиальных линий, по умолчанию — #fff.
    active_zodiac_colour: цвет активного зодиака, по умолчанию — #fff.
    inactive_zodiac_colour: цвет неактивного зодиака, по умолчанию — #fff.
    active_nakshatra_colour: цвет активной накшатры, по умолчанию — #fff.
    inactive_nakshatra_colour: цвет неактивной накшатры, по умолчанию — #fff.
    zodiac_transparency: прозрачность зодиака, по умолчанию — 0.45.
    nakshatra_transparency: прозрачность накшатры, по умолчанию — 0.45.
    size_inches: размер графика в дюймах, по умолчанию — (13, 10).
    reading_format: настройка для чтения значения из .tex файлов
    """

    bg: str = "dark_background"
    outer_radial_lines_colour: str = "#fff"
    inner_radial_lines_colour: str = "#fff"
    active_zodiac_colour: str = "#fff"
    inactive_zodiac_colour: str = "#fff"
    active_nakshatra_colour: str = "#fff"
    inactive_nakshatra_colour: str = "#fff"
    lines_transparency: float = 0.3
    zodiac_transparency: float = 0.45
    nakshatra_transparency: float = 0.45
    size_inches: tuple = (13, 10)
    reading_format: str = "latex"
    preamble = Preamble.preamble
