# ------------------------------------------------------------------------------
#   file:       podunk/widget/formats.py
#   author:     Jim Storch
# ------------------------------------------------------------------------------

import locale
# ------------------------------------------------------------------Format Plain


def format_plain(value):
    """
    Returns value cast to a string.  This is the default for Field.
    """
    if value == None:
        retval = ''
    else:
        try:
            value1 = value.decode('utf-8')
        except:
            value1 = value
        # retval = value
        retval = u'%s' % value1
    return retval

# -----------------------------------------------------------Format Two Decimals


def format_two_decimals(value):
    """
    Returns value rounded to two decimal places.    
    """
    # foo = locale.setlocale(locale.LC_ALL,('English_United States'))
    if value == None or value == 0.0:
        retval = '  '
    else:
        retval = "{:,.2f}".format(float(value)) if value else '  '
    return retval


# ------------------------------------------------------------Format US Currency

def format_ph_currency(value):
    """
    Returns value in monetary format, 2 decimal places, comma separated
    every three digits with a leading dollar sign.
    """
    # foo = locale.setlocale(locale.LC_ALL,'English_United States')
    # locale.setlocale(locale.LC_ALL, 'de_DE')
    if value == None:
        retval = ''
    else:
        retval = 'P ' + locale.format("%.2f", float(value), True)
    return retval


def format_us_currency(value):
    """
    Returns value in monetary format, 2 decimal places, comma separated
    every three digits with a leading dollar sign.
    """
    # foo = locale.setlocale(locale.LC_ALL,'English_United States')
    # locale.setlocale(locale.LC_ALL, 'de_DE')
    if value == None:
        retval = ''
    else:
        retval = '$ ' + locale.format("%.2f", float(value), True)
    return retval


# ------------------------------------------------------------------Format Title

def format_title(value):
    """
    Returns A String In Title Case
    """
    if value == None:
        retval = ''
    else:
        retval = str(value).title()
    return retval

# ------------------------------------------------------------------Format DMYHM


def format_dmyhm(value):
    """
    Returns the date and time in the format DD/MM/YY HH:MM. 
    """
    if value == None:
        retval = ''
    else:
        retval = value.strftime('%m/%d/%y %H:%M')
    return retval


def format_time(value):
    """
    Returns the date and time in the format DD/MM/YY HH:MM. 
    """
    if value == None:
        retval = ''
    else:
        if isinstance(value, str):
            from datetime import datetime
            try:
                value = datetime.strptime(
                    value.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return ''
        elif not isinstance(value, datetime):
            return ''
        retval = value.strftime('%H:%M')
    return retval


def format_dmy(value):
    """
    Returns the date and time in the format DD/MM/YY HH:MM. 
    """
    if value == None:
        retval = ''
    else:
        retval = value.strftime('%m/%d/%Y')
    return retval

# ------------------------------------------------------------Format Report Date


def format_report_date(value):
    """
    Returns the date and time in the format 'Jul 03, 2008 - 09:11 AM'
    """
    if value == None:
        retval = ''
    else:
        retval = value.strftime('%b %d, %Y - %I:%M %p')
    return retval


def format_report_date_isoformat(value):
    """
    Returns the date and time in the ISO format.
    """
    if value == None:
        retval = ''
    else:
        retval = value.isoformat()
    return retval


def format_hex(value):
    """
    Returns value as hexadecimal string. 
    """
    if value == None:
        retval = ''
    else:
        retval = "%X" % value
