from word2number.base_converter import BaseConverter


class AmericanConverter(BaseConverter):
    def _string_preprocessing(self, number_sentence: str):
        number_sentence = number_sentence.replace('-', ' ')
        return number_sentence.strip().split()  # strip extra spaces and split sentence into words

    def _number_formation(self, number_words):
        numbers = []
        for number_word in number_words:
            numbers.append(self._number_system[number_word])
        if len(numbers) == 4:
            return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
        elif len(numbers) == 3:
            return numbers[0] * numbers[1] + numbers[2]
        elif len(numbers) == 2:
            if 100 in numbers:
                return numbers[0] * numbers[1]
            else:
                return numbers[0] + numbers[1]
        else:
            return numbers[0]

    def _get_decimal_sum(self, decimal_digit_words):
        decimal_number_str = []
        for dec_word in decimal_digit_words:
            if dec_word not in self._decimal_words:
                return 0
            else:
                decimal_number_str.append(self._number_system[dec_word])
        final_decimal_string = '0.' + ''.join(map(str, decimal_number_str))
        return float(final_decimal_string)


class RussianConverter(BaseConverter):
    def _string_preprocessing(self, number_sentence: str):
        return number_sentence.strip().split()

    def _number_formation(self, number_words):
        numbers = []
        for number_word in number_words:
            numbers.append(self._number_system[number_word])
        if len(numbers) == 4:
            return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
        elif len(numbers) == 3:
            return numbers[0] + numbers[1] + numbers[2]
        elif len(numbers) == 2:
            if 100 in numbers:
                return numbers[0] * numbers[1]
            else:
                return numbers[0] + numbers[1]
        elif len(numbers) == 1:
            return numbers[0]
        else:
            return 1

    def _get_decimal_sum(self, decimal_digit_words):
        raise NotImplemented


american_number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'point': '.'
}

russian_number_system = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 1000,
    'миллион': 1000000,
    'миллиард': 1000000000,
}

american_decimal_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
russian_decimal_words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']


american_converter = AmericanConverter(american_number_system, american_decimal_words, 'thousand', 'million', 'billion', 'point')
# IMPORTANT!
# If you are going to use russian converter, make sure you numbers are in their base forms. E.g: две -> два
russian_converter = RussianConverter(russian_number_system, russian_decimal_words, 'тысяча', 'миллион', 'миллиард', 'not_supported_yet')
