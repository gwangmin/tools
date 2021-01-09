'''
This script provides stopwatch, current time check.
Defined vars: 
Defined funcs: convert_sec(sec), get_current_timestamp()
Defined classes: StopWatch(), Now(lang)
'''


import time
import datetime


def convert_sec(sec):
    '''
    Convert sec to h,m,s format
        
    sec: second(s).
    '''
    sec = float(sec)
    sec_point = str(sec).split('.')[1]
    s = int(sec)

    m = int(s/60)
    h = int(m/60)
    s = int(s%60)
    m = int(m%60)
        
    s = str(s) + '.' + sec_point
    s = float(s)

    return h,m,s


def get_current_timestamp():
    '''
    Return current timestamp
    '''
    return time.time()


class StopWatch:
    '''
    Measure interval time
    unit: second(s)
    '''
    COUNTING = 'counting'
    STOPPED = 'stopped'
    PAUSED = 'paused'

    def __init__(self):
        self.state = StopWatch.STOPPED

    def start(self):
        '''
        Start measure
        If complete successfully, return 0. but not, return 'error'
        '''
        if self.state in [StopWatch.STOPPED, StopWatch.PAUSED]:
            self.start_ = time.time()
            self.state = StopWatch.COUNTING
            return 0
        else:
            return 'error'
    
    def pause(self):
        '''
        '''
        pass

    def stop(self, acc=2):
        '''
        Stop measure and return (measured sec, h:m:s format string).
        
        acc: ndigits to round. if -1, no round.

        Return: interval time, if success. but not, 'error'
        '''
        if self.state in [StopWatch.COUNTING, StopWatch.PAUSED]:
            self.interval = time.time() - self.start_
            if acc == -1:
                interval = self.interval
            else:
                interval = round(self.interval, acc)
            self.state = StopWatch.STOPPED
            return interval
        else:
            return 'error'


class Now:
    '''
    Current datetime
    based local time
    12-hour clock
    support lang: eng(usa), kor
    midnight: am 0
    
    member:
        lang - language
        year - year
        mon - month
        day - day
        hour - hour(12-hour)
        hour_range - 'am' or 'pm'
        min - minutes
        wday - day of the week(요일)
        struct_time - time.struct_time obj
        get_date_str(include_wday) - Return date string('yyyy-mm-dd www' or 'www, mm-dd-yyyy')
        get_time_str() - Return time string(hh:mm:ss)
        get_datetime_str(iso) - Return datetime string
    '''
    def __init__(self, lang='kor'):
        '''
        Initialize member var.
        
        lang: 'kor' or 'eng'. Default 'kor'.
        '''
        self.lang = lang
        tm = time.localtime()
        self.struct_time = tm

        self.year = tm.tm_year
        self.mon = tm.tm_mon
        self.day = tm.tm_mday
        self.set_hour_and_hour_range()
        self.min = tm.tm_min
        self.sec = tm.tm_sec
        self.set_wday()

    def set_hour_and_hour_range(self):
        '''
        Set hour, hour_range(am or pm)
        '''
        tm = self.struct_time
        h24 = tm.tm_hour # [0, 23]
        if (h24 == 0) or (h24 == 24):
            # 0, 24
            self.hour_range = 'am'
            self.hour = 0
        elif 0 < h24 <= 11:
            # 1 ~ 11
            self.hour_range = 'am'
            self.hour = h24
        elif h24 == 12:
            # 12
            if tm.tm_min == 0:
                self.hour_range = 'am'
            else:
                self.hour_range = 'pm'
            self.hour = h24
        elif 12 < h24 < 24:
            # 13 ~ 23
            self.hour_range = 'pm'
            self.hour = h24 - 12

    def set_wday(self):
        '''
        Set wday(day of the week, 요일)
        '''
        lang = self.lang
        tm = self.struct_time
        wday = tm.tm_wday
        if wday == 0:
            if lang == 'kor': self.wday = '월요일'
            elif lang == 'eng': self.wday = 'Monday'
        elif wday == 1:
            if lang == 'kor': self.wday = '화요일'
            elif lang == 'eng': self.wday = 'Tuesday'
        elif wday == 2:
            if lang == 'kor': self.wday = '수요일'
            elif lang == 'eng': self.wday = 'Wednesday'
        elif wday == 3:
            if lang == 'kor': self.wday = '목요일'
            elif lang == 'eng': self.wday = 'Thursday'
        elif wday == 4:
            if lang == 'kor': self.wday = '금요일'
            elif lang == 'eng': self.wday = 'Friday'
        elif wday == 5:
            if lang == 'kor': self.wday = '토요일'
            elif lang == 'eng': self.wday = 'Saturday'
        elif wday == 6:
            if lang == 'kor': self.wday = '일요일'
            elif lang == 'eng': self.wday = 'Sunday'

    def get_timestamp(self):
        '''
        Return TimeStamp
        '''
        return time.time()

    def get_date_str(self, include_wday=True):
        '''
        Return date string('yyyy-mm-dd www' or 'www, mm-dd-yyyy')

        include_wday: whther include day of the week. default True
        '''
        lang = self.lang
        tm = self.struct_time
        if lang == 'kor':
            if include_wday:
                self.date = time.strftime(r'%Y-%m-%d ', tm) + self.wday
            else:
                self.date = time.strftime(r'%Y-%m-%d', tm)
        elif lang == 'eng':
            if include_wday:
                self.date = time.strftime(r'%a, %m-%d-%Y', tm)
            else:
                self.date = time.strftime(r'%m-%d-%Y', tm)

    def get_time_str(self):
        '''
        Return time string(hh:mm:ss)
        '''
        tm = self.struct_time
        return time.strftime(r'%I:%M:%S %p', tm)

    def get_datetime_str(self, iso=False):
        '''
        Return datetime string

        iso: whether using ISO format. default False
        '''
        if iso:
            h, m, s = convert_sec(abs(time.timezone))
            if time.timezone > 0:
                offset = f'-{h:0>2}:{m:0>2}'
            else:
                offset = f'+{h:0>2}:{m:0>2}'
            return self.get_date_str(False) + 'T' + self.get_time_str() + offset
        else:
            return self.get_date_str(True) + ' ' + self.get_time_str()
    

def test_StopWatch():
    w = StopWatch()
    w.start()
    time.sleep(1)
    w.stop()


def test_Now():
    now = Now(lang='kor')
    print(now.year,now.mon,now.day,now.hour,now.hour_range,now.min,now.sec,now.wday,
    now.get_date_str(),now.get_time_str,sep=' ',end='\n\n')
    print(now.get_datetime_str())
    print(now.get_timestamp())


if __name__ == '__main__':
    test_Now()
