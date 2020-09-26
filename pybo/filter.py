import locale

locale.setlocale(locale.LC_CTYPE,'korean')  #srftime에 한글이 들어갈경우 깨져서 나오는 오류 해결(UnicodeEncodeError: 'locale' codec...)

def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)