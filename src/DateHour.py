
class DateHour:
    def __init__ (self,data):
        assert(all(k in data for k in ['year','month','day','hours','minutes']))
        self.data = {k: str(v) if v != str else v for k,v in data.items() if k in ['year','month','day','hours','minutes']}
    def __str__(self):
        return str(self.data)
    def from_datetime(datetime):
        return DateHour({'year': str(datetime.year), 'month': str(datetime.month),'day': str(datetime.day), 'hours': str(datetime.hour), 'minutes': str(datetime.minute)})
    def to_dict(self):
        return self.data
    def matches(self,time_to_compare):
        for criteria in ['year','month','day','hours','minutes']:
            if self.data[criteria] != time_to_compare.data[criteria] and self.data[criteria] != '*' and time_to_compare.data[criteria] != '*':
                return False
        return True