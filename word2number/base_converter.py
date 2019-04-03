from __future__ import print_function


class BaseConverter:
    def __init__(self, number_system: dict, decimal_words: list, thousand: str, million: str, billion: str, point: str):
        self._number_system = number_system
        self._decimal_words = decimal_words
        self._thousand = thousand
        self._million = million
        self._billion = billion
        self._point = point

    def _prepare_data(self, split_words):
        clean_numbers = []
        clean_decimal_numbers = []

        # removing and, & etc.
        for word in split_words:
            if word in self._number_system:
                clean_numbers.append(word)

        # Error message if the user enters invalid input!
        if not clean_numbers:
            raise ValueError(
                "No valid number words found! Please enter a valid number word "
                "(eg. two million twenty three thousand and forty nine)"
            )

            # Error if user enters million,billion, thousand or decimal point twice
        if clean_numbers.count(self._thousand) > 1 or clean_numbers.count(self._million) > 1 or \
                clean_numbers.count(self._billion) > 1 or clean_numbers.count(self._point) > 1:
            raise ValueError(
                "Redundant number word! Please enter a valid number word "
                "(eg. two million twenty three thousand and forty nine)"
            )

        # separate decimal part of number (if exists)
        if clean_numbers.count(self._point) == 1:
            clean_decimal_numbers = clean_numbers[clean_numbers.index(self._point) + 1:]
            clean_numbers = clean_numbers[:clean_numbers.index(self._point)]

        return clean_numbers, clean_decimal_numbers

    def _process_billions(self, billion_index: int, clean_numbers: list):
        """
        Calculates billion part.
        :param billion_index: index of `self._billion`
        :param clean_numbers: list of split words
        :return: calculated billion part
        """
        if billion_index > -1:
            billion_multiplier = self._number_formation(clean_numbers[0:billion_index])
            return billion_multiplier * 1000000000
        return 0

    def _process_millions(self, billion_index: int, million_index: int, clean_numbers: list):
        """
        Calculates million part.
        :param billion_index: index of `self._billion`
        :param million_index: index of `self._million`
        :param clean_numbers: list of split words
        :return: calculated million part
        """
        if million_index > -1:
            if billion_index > -1:
                million_multiplier = self._number_formation(clean_numbers[billion_index + 1:million_index])
            else:
                million_multiplier = self._number_formation(clean_numbers[0:million_index])
            return million_multiplier * 1000000
        return 0

    def _process_thousands(self, billion_index: int, million_index: int, thousand_index: int, clean_numbers: list):
        """
        Calculates thousand part.
        :param billion_index: index of `self._billion`
        :param million_index: index of `self._million`
        :param thousand_index: index of `self._thousand`
        :param clean_numbers: list of split words
        :return: calculated thousand part
        """
        if thousand_index > -1:
            if million_index > -1:
                thousand_multiplier = self._number_formation(clean_numbers[million_index + 1:thousand_index])
            elif billion_index > -1 and million_index == -1:
                thousand_multiplier = self._number_formation(clean_numbers[billion_index + 1:thousand_index])
            else:
                thousand_multiplier = self._number_formation(clean_numbers[0:thousand_index])
            return thousand_multiplier * 1000
        return 0

    def _process_hundreds(self, billion_index: int, million_index: int, thousand_index: int, clean_numbers: list):
        """
        Calculates hundred part.
        :param billion_index: index of `self._billion`
        :param million_index: index of `self._million`
        :param thousand_index: index of `self._thousand`
        :param clean_numbers: list of split words
        :return: calculated hundred part
        """
        if thousand_index > -1 and thousand_index != len(clean_numbers) - 1:
            return self._number_formation(clean_numbers[thousand_index + 1:])
        elif million_index > -1 and million_index != len(clean_numbers) - 1:
            return self._number_formation(clean_numbers[million_index + 1:])
        elif billion_index > -1 and billion_index != len(clean_numbers) - 1:
            return self._number_formation(clean_numbers[billion_index + 1:])
        elif thousand_index == -1 and million_index == -1 and billion_index == -1:
            return self._number_formation(clean_numbers)
        else:
            return 0

    def word_to_num(self, number_sentence: str):
        """
        Function to return integer for an input `number_sentence` string
        :param number_sentence
        :return converted value as number
        :rtype: int or double or None
        """
        if number_sentence.isdigit():  # return the number if user enters a number string
            return int(number_sentence)

        split_words = self._string_preprocessing(number_sentence)

        clean_numbers, clean_decimal_numbers = self._prepare_data(split_words)

        thousand_index = clean_numbers.index(self._thousand) if self._thousand in clean_numbers else -1
        million_index = clean_numbers.index(self._million) if self._million in clean_numbers else -1
        billion_index = clean_numbers.index(self._billion) if self._billion in clean_numbers else -1

        if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or \
                (million_index > -1 and million_index < billion_index):
            raise ValueError(
                "Malformed number! Please enter a valid number word "
                "(eg. two million twenty three thousand and forty nine)"
            )

        total_sum = 0  # storing the number to be returned

        if clean_numbers:
            # hack for now, better way TODO
            if len(clean_numbers) == 1:
                total_sum += self._number_system[clean_numbers[0]]
            else:
                total_sum += self._process_billions(billion_index, clean_numbers)
                total_sum += self._process_millions(billion_index, million_index, clean_numbers)
                total_sum += self._process_thousands(billion_index, million_index, thousand_index, clean_numbers)
                total_sum += self._process_hundreds(billion_index, million_index, thousand_index, clean_numbers)

        # adding decimal part to total_sum (if exists)
        if clean_decimal_numbers:
            total_sum += self._get_decimal_sum(clean_decimal_numbers)

        return total_sum

    def _string_preprocessing(self, number_sentence: str):
        """
        Cleans and splits inputted string according to a particular rules.
        :param number_sentence: inputted string
        :return: list of tokens
        """
        raise NotImplemented

    def _get_decimal_sum(self, decimal_digit_words: list):
        """
        Function to convert post decimal digit words to numerial digits
        :param decimal_digit_words: list of strings
        :return decimal part
        :rtype: float
        """
        raise NotImplemented

    def _number_formation(self, number_words: list):
        """
        Function to form numeric multipliers for million, billion, thousand etc.

        :param number_words: list of strings
        :return multiplyer
        :rtype integer
        """
        raise NotImplemented
