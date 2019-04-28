import datetime

class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_python(self, value):
        if 2010 <= int(value) <= datetime.datetime.now().year:
            return int(value)
        else:
            return None

    def to_url(self, value):
        return '{%04d}'.format(value)