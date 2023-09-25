#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            numerator = my_list_1[i]
            denominator = my_list_2[i]

            if not(isinstance(numerator, (int, float)) and isinstance(denominator, (int, float))):
                raise TypeError("wrong type")

            if denominator == 0:
                raise ZeroDivisionError("division by zero")

            division_result = numerator / denominator
            result.append(division_result)

        except IndexError:
            print("out of range")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except ZeroDivisionError:
            print("division by zero")
            result.append(0)

        finally:
            pass
    return (result)
