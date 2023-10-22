from datetime import datetime

def validateData(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def formatedData(data_str):
    formatedDate = datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    return formatedDate
