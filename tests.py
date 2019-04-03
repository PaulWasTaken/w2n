import pytest


from word2number.converters import american_converter, russian_converter


@pytest.mark.parametrize('test_input,expected', [
    ('two million three thousand nine hundred and eighty four', 2003984),
    ('nineteen', 19),
    ('two thousand and nineteen', 2019),
    ('two million three thousand and nineteen', 2003019),
    ('three billion', 3000000000),
    ('three million', 3000000),
    ('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine', 123456789),
    ('eleven', 11),
    ('nineteen billion and nineteen', 19000000019),
    ('one hundred and forty two', 142),
    ('112', 112),
    ('11211234', 11211234),
    ('five', 5),
    ('two million twenty three thousand and forty nine', 2023049),
    ('two point three', 2.3),
    ('two million twenty three thousand and forty nine point two three six nine', 2023049.2369),
    ('one billion two million twenty three thousand and forty nine point two three six nine', 1002023049.2369),
    ('point one', 0.1),
    ('point', 0),
    ('point nineteen', 0),
    ('one hundred thirty-five', 135),
    ('hundred', 100),
    ('thousand', 1000),
    ('million', 1000000),
    ('billion', 1000000000),
    ('nine point nine nine nine', 9.999),
    ('seventh point nineteen', 0)
])
def test_positives_usa(test_input, expected):
    assert american_converter.word_to_num(test_input) == expected


@pytest.mark.parametrize('test_input', [
    '112-',
    '-',
    'on',
    'million million',
    'three million million',
    'million four million',
    'thousand million',
    'one billion point two million twenty three thousand and forty nine point two three six nine'
])
def test_negative_usa(test_input):
    with pytest.raises(ValueError):
        american_converter.word_to_num(test_input)


@pytest.mark.parametrize('test_input,expected', [
    ('два миллион три тысяча девятьсот восемьдесят четыре', 2003984),
    ('девятнадцать', 19),
    ('два тысяча девятнадцать', 2019),
    ('два миллион три тысяча девятнадцать', 2003019),
    ('три миллиард', 3000000000),
    ('три миллион', 3000000),
    ('сто двадцать три миллион четыреста пятьдесят шесть тысяча семьсот восемьдесят девять', 123456789),
    ('одиннадцать', 11),
    ('девятнадцать миллиард девятнадцать', 19000000019),
    ('сто сорок два', 142),
    ('112', 112),
    ('11211234', 11211234),
    ('пять', 5),
    ('два миллион двадцать три тысяча сорок девять', 2023049),
    ('сто тридцать пять', 135),
    ('сто', 100),
    ('тысяча', 1000),
    ('миллион', 1000000),
    ('миллиард', 1000000000),
    ('ноль', 0)
])
def test_positives_rus(test_input, expected):
    assert russian_converter.word_to_num(test_input) == expected


@pytest.mark.parametrize('test_input', [
    'случайное предложение',
    'миллион миллион',
    'тысяча миллион',
    'миллион четыре миллион',
    'три миллион миллион'
])
def test_negative_usa(test_input):
    with pytest.raises(ValueError):
        russian_converter.word_to_num(test_input)
