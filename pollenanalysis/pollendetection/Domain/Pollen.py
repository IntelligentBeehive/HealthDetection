import datetime


class Pollen:
    """Domain model Pollen"""

    def __init__(self, red, green, blue):
        self.name = 'unknown'

    @property
    def get_season(self):
        date = datetime.datetime.now()
        year_day = date.timetuple().tm_yday

        if year_day < 61:
            return {1, 'winter'}
        elif year_day < 173:
            return {2, 'spring'}
        elif year_day < 265:
            return {3, 'summer'}
        elif year_day < 356:
            return {4, 'autumn'}
        else:
            return {1, 'winter'}
