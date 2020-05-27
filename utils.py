from datetime import datetime


def normalize_data(data):
    return {k: v for k, v in data.items() if v is not None}


def get_formatted_date(date):
    return datetime.strftime(date, '%Y-%m-%d')


def get_today_date():
    return datetime.utcnow()
