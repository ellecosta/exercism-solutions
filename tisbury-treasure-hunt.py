"""Tisbury Treasure Hunt"""

def get_coordinate(record):
    """Extract coordinates"""
    return record[1]

def convert_coordinate(coordinate):
    """Format coordinates"""
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Match coordinates"""
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    return False
    
def create_record(azara_record, rui_record):
    """Combine matched records"""
    if tuple(azara_record[1]) == rui_record[1]:
        return azara_record + rui_record
    return 'not a match'

def clean_up(combined_record_group):
    """Combine matched records"""
    report = ""
    for index, item in enumerate(combined_record_group):
        report += f'{combined_record_group[index][:1] + combined_record_group[index][2:]}\n'
    return report
