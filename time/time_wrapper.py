'''
This script provides:
    - convert secs to h,m,s
    - stopwatch
    - datetime representation helper(Represent datetime in my format)
'''

import time
import datetime


def convert_sec(sec):
    '''
    Convert sec to h,m,s format
        
    sec: second(s).

    return: h, m, s
    '''
    under_point = None
    # 소수점이 있으면
    if str(sec).find('.') != -1:
        under_point = str(sec).split('.')[1]
    
    s = int(sec)

    # h, m, s로
    h = s // (60*60)
    s = s - ((60*60) * h)
    m = s // 60
    s = s - (60*m)

    # 소수점이 있으면
    if under_point != None:
        s = float(str(s) + '.' + under_point)

    return h, m, s


def get_epoch_time():
    '''
    Return current epoch time

    return: epoch time
    '''
    return time.time()


# TODO: schedule 모듈 사용
class StopWatch:
    '''
    Stopwatch

    unit: second(s)

    public methods:
        start()
        pause()
        restart()
        stop()
    '''
    COUNTING = 'counting'
    STOPPED = 'stopped'
    PAUSED = 'paused'

    def __init__(self):
        self.state = StopWatch.STOPPED

    def start(self):
        '''
        Start timer
        if failed, raise exception
        '''
        if self.state == self.STOPPED:
            self.base_time = 0
            self.start_time = time.time()
            self.state = StopWatch.COUNTING
        else:
            raise Exception('[-] stopwatch.start() error!')
    
    def pause(self):
        '''
        Pause counting
        '''
        if self.state == self.COUNTING:
            result = time.time() - self.start_time
            self.base_time += result
            self.start_time = None
            self.state = self.PAUSED
        else:
            raise Exception('[-] stopwatch.pause() error!')

    def restart(self):
        '''
        Restart paused timer
        '''
        if self.state == self.PAUSED:
            self.start_time = time.time()
            self.state = self.COUNTING
        else:
            raise Exception('[-] stopwatch.restart() error!')

    def stop(self):
        '''
        Stop timer and return

        return: measured time(secs)
        '''
        if self.state == self.COUNTING:
            result = self.base_time + (time.time() - self.start_time)
            self.base_time = 0
            self.start_time = None

        elif self.state == self.PAUSED:
            result = self.base_time
            self.base_time = 0

        else:
            raise Exception('[-] stopwatch.stop() error!')
        
        self.state = self.STOPPED
        return result

    def start_cpu_time(self):
        '''
        https://wikidocs.net/15636#timing
        Start CPU timer
        '''
        self.cpu_time = time.process_time()

    def stop_cpu_time(self):
        '''
        Stop CPU timer and return cpu time

        return: measured cpu time
        '''
        return time.process_time() - self.cpu_time


class Datetime:
    '''
    Datetime representation
    - Default timezone: local
    - 12-hour based time (0 <= am < 12, 12 <= pm < 24)
    - Support lang: eng(usa), kor
    - Midnight: 12 am
    
    readonly member:
        lang - language
        year - year
        mon - month
        day - day
        hour - hour(12-hour)
        hour_range - 'am' or 'pm'
        min - minutes
        weekday_n - day of the week(요일) number
        weekday - day of the week(요일)
    
    public methods:
        get_date_str(include_wday) - Return date string('yyyy-mm-dd www' or 'www, mm-dd-yyyy')
        get_time_str() - Return time string(** hh:mm:ss or hh:mm:ss **)
        get_datetime_str(iso) - Return datetime string
    '''
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6
    wday_representation = {
        'kor': {
            MON: '월',
            TUE: '화',
            WED: '수',
            THU: '목',
            FRI: '금',
            SAT: '토',
            SUN: '일',
        },
        'eng': {
            MON: 'Mon',
            TUE: 'Tue',
            WED: 'Wed',
            THU: 'Thu',
            FRI: 'Fri',
            SAT: 'Sat',
            SUN: 'Sun',
        },
    }
    hour_representation = {
        'kor': ['오전', '오후'],
        'eng': ['A.M.', 'P.M.'],
    }
    
    def __init__(self, lang='kor'):
        '''
        Initialize member var.
        
        lang: 'kor' or 'eng'. Default 'kor'.
        '''
        self.lang = lang
        # empty
        self.struct_time = None
        self.datetime = None

    @staticmethod
    def from_struct_time(st, lang='kor'):
        '''
        Create obj from st

        st: time.struct_time obj
        lang: 'kor' or 'eng'. Default 'kor'.
        '''
        m = Datetime(lang=lang)
        m.set_struct_time(st)
        return m

    @staticmethod
    def from_datetime(dt, lang='kor'):
        '''
        Create obj from dt

        dt: datetime.datetime obj
        lang: 'kor' or 'eng'. Default 'kor'.
        '''
        m = Datetime(lang=lang)
        m.set_datetime(dt)
        return m

    def set_struct_time(self, st):
        '''
        Set time.struct_time obj

        st: time.struct_time obj
        '''
        # Set fields with time.struct_time
        self.year = st.tm_year
        self.mon = st.tm_mon
        self.day = st.tm_mday
        self.hour, self.hour_range = self.convert_24_to_12(st.tm_hour, self.lang)
        self.min = st.tm_min
        self.sec = st.tm_sec
        self.weekday_n = st.tm_wday
        self.weekday = self.convert_weekday(st.tm_wday, self.lang)
        # Save st
        self.struct_time = st

    def get_struct_time(self):
        '''
        Return time.struct_time obj

        return: time.struct_time obj
        '''
        # 저장해둔게 있으면 바로 리턴
        if self.struct_time != None:
            return self.struct_time
        else:
            raise Exception('unavailable')

    def set_datetime(self, dt):
        '''
        Set datetime.datetime obj

        dt: datetime.datetime obj
        '''
        # Set fields with time.struct_time
        self.year = dt.year
        self.mon = dt.month
        self.day = dt.day
        self.hour, self.hour_range = self.convert_24_to_12(dt.hour, self.lang)
        self.min = dt.minute
        self.sec = dt.second
        self.weekday_n = dt.weekday()
        self.weekday = self.convert_weekday(self.weekday_n, self.lang)
        # Save st
        self.datetime = dt

    def get_datetime(self):
        '''
        Return datetime.datetime obj

        return: datetime.datetime obj
        '''
        if self.datetime != None:
            return self.datetime
        else:
            return\
            datetime.datetime(self.year, self.mon, self.day, self.convert_12_to_24(self.hour,self.hour_range,self.lang), self.min, self.sec)

    def convert_24_to_12(self, h24, lang):
        '''
        Convert 24-based hour to 12-based.

        h24: hour(24-based, [0,24))
        lang: 'kor' or 'eng'

        return: 12-based hour, hour_range(am or pm)
        '''
        # 0 ~ 11
        if 0 <= h24 <= 11:
            hour_range = self.hour_representation[lang][0]
            # 0
            if h24 == 0:
                hour = 12
            # 1 ~ 11
            else:
                hour = h24
        # 12 ~ 23
        elif 12 <= h24 <= 23:
            hour_range = self.hour_representation[lang][1]
            # 12
            if h24 == 12:
                hour = 12
            # 13 ~ 23
            else:
                hour = h24 - 12
        
        return hour, hour_range

    def convert_12_to_24(self, h12, hour_range, lang):
        '''
        Convert 12-based hour to 24-based.

        h12: hour(12-based, [0,12])
        hour_range: am or pm
        lang: 'kor' or 'eng'

        return: 24-based hour
        '''
        # am
        if hour_range == self.hour_representation[lang][0]:
            if h12 == 12:
                h24 = 0
            else:
                h24 = h12
        # pm
        elif hour_range == self.hour_representation[lang][1]:
            if h12 == 12:
                h24 = 12
            else:
                h24 = h12 + 12
        
        return h24

    def convert_weekday(self, n, lang):
        '''
        Convert weekday num to specified lang representation

        n: 0-based weekday(day of week) num
        lang: 'kor' or 'eng'

        return: weekday representation
        '''
        wday = self.wday_representation[lang][n]
        return wday

    def get_date_str(self, include_weekday=True):
        '''
        Return date string('YYYY-MM-DD w' or 'www, MM-DD-YYYY')

        include_weekday: whther include day of the week. default True.

        return: date string
        '''
        if self.lang == 'kor':
            date_str = f'{self.year}-{self.mon}-{self.day}'
            if include_weekday:
                date_str += ' ' + self.weekday
            return date_str
        
        elif self.lang == 'eng':
            date_str = f'{self.mon}-{self.day}-{self.year}'
            if include_weekday:
                date_str = self.weekday + ', ' + date_str
            return date_str

    def get_time_str(self):
        '''
        Return time string(** hh:mm:ss or hh:mm:ss **)

        return: time string
        '''
        time_str = f'{self.hour}:{self.min}:{self.sec}'
        if self.lang == 'kor':
            time_str = self.hour_range + ' ' + time_str
        elif self.lang == 'eng':
            time_str += ' ' + self.hour_range
        return time_str

    def get_datetime_str(self, iso=False):
        '''
        Return datetime string

        iso: whether using ISO format. default False

        return: datetime string
        '''
        if iso:
            # make offset string
            if time.timezone == 0:
                offset_str = 'Z'
            else:
                h, m, s = convert_sec(abs(time.timezone))
                offset_str = f'{h:0>2}:{m:0>2}'
                # 음수
                if time.timezone < 0:
                    offset_str = '+' + offset_str
                # 양수
                else:
                    offset_str = '-' + offset_str
            # make iso datetime string
            if self.lang == 'kor':
                datetime_str = self.get_date_str(False) + 'T' + self.get_time_str()[3:] + offset_str
            elif self.lang == 'eng':
                time_str = self.get_time_str().split()[0]
                datetime_str = self.get_date_str(False) + 'T' + time_str + offset_str
        
        # make full datetime string
        else:
            if self.lang == 'kor':
                datetime_str = self.get_date_str(True) + ' ' + self.get_time_str()
            elif self.lang == 'eng':
                datetime_str = self.get_time_str() + ', ' + self.get_date_str(True)
        
        return datetime_str
    

def test_StopWatch():
    w = StopWatch()
    w.start()
    time.sleep(1)
    w.pause()
    print(w.base_time)
    w.restart()
    time.sleep(3)
    print(w.stop())

def test_Datetime():
    m = Datetime.from_datetime(datetime.datetime.today(), lang='kor')
    print(m.year,m.mon,m.day,m.hour,m.hour_range,m.min,m.sec,m.weekday,
    sep=' ',end='\n\n')
    print(m.get_datetime_str())

if __name__ == '__main__':
    test_StopWatch()
    test_Datetime()
