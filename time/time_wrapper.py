'''
This script provides:
    - basic time functions
    - datetime helper functions
    - stopwatch class

datetime doc:
    https://docs.python.org/ko/3/library/datetime.html#datetime-objects
datetime provide datetime operation(arithmetic ops, compare ops)
'''

import time
import datetime
from functools import wraps


def convert_sec(sec):
    '''
    Convert sec to h,m,s format
        
    sec: real number. second(s)

    return: h, m, s
    '''
    under_section = None
    # 소수점이 있으면
    if str(sec).find('.') != -1:
        under_section = str(sec).split('.')[1]
    
    s = int(sec)

    # h, m, s로
    h = s // (60*60)
    s = s - ((60*60) * h)
    m = s // 60
    s = s - (60*m)

    # 소수부분이 저장되어 있으면
    if under_section != None:
        s = float(str(s) + '.' + under_point)

    return h, m, s

def get_epoch_time():
    '''
    Return current epoch time
    return: epoch time
    '''
    return time.time()
get_timestamp = get_epoch_time

def get_current_datetime(timezone=None):
    '''
    Return current datetime obj with timezone
    timezone: optional. e.g. pytz.timezone('UTC')
    '''
    return datetime.datetime.now(timezone)

def to_epoch(datetime_obj):
    '''
    Convert datetime instance to epoch time(timestamp)
    datetime_obj: datetime.datetime instance
    '''
    return datetime_obj.timestamp()
to_timestamp = to_epoch

def get_datetime_str(datetime_obj):
    '''
    Return datetime string in ISO format
    datetime_obj: datetime.datetime instance
    '''
    return datetime_obj.isoformat()

wday = {
    'kor': ['월', '화', '수', '목', '금', '토', '일'],
    'eng': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
}
def get_wday_str(datetime_obj, lang='kor'):
    '''
    Return week of day string

    datetime_obj: datetime.datetime instance
    lang: 'kor' or 'eng'
    '''
    return wday[lang][datetime_obj.weekday()]

hour12 = {
    'kor': ['오전', '오후'],
    'eng': ['A.M.', 'P.M.'],
}
def convert_24_to_12(h24, lang='kor'):
    '''
    Convert 24-based hour to 12-based
    (0 <= am < 12, 12 <= pm < 24, Midnight: 12 am)

    h24: 24-based hour
    lang: 'kor' or 'eng'

    return: 12-based hour, am or pm string
    '''
    # 0 ~ 11
    if 0 <= h24 <= 11:
        ampm = 0
        # 0
        if h24 == 0:
            h12 = 12
        # 1 ~ 11
        else:
            h12 = h24
    # 12 ~ 23
    elif 12 <= h24 <= 24:
        ampm = 1
        # 12, 24
        if h24 == 12 or h24 == 24:
            h12 = 12
        # 13 ~ 23
        else:
            h12 = h24 - 12
        
    return h12, hour12[lang][ampm]

# decorator
def measure_func_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f'{func.__name__}: {execution_time} sec(s)')
        return r
    return wrapper


class Stopwatch:
    '''
    Stopwatch
    unit: second(s)
    public methods:
        start()
        pause()
        stop()
    '''
    COUNTING = 'counting'
    STOPPED = 'stopped'
    PAUSED = 'paused'

    def __init__(self):
        self.state = self.STOPPED
        self.start_time = None
        self.display = 0

    def start(self):
        '''
        Start timer
        '''
        if self.state in [self.STOPPED, self.PAUSED]:
            self.state = self.COUNTING
            self.start_time = time.time()
        elif self.state == self.COUNTING:
            pass
        else:
            raise Exception('[-] stopwatch.start() error!')
    
    def pause(self):
        '''
        Pause counting and return

        return: measured time(secs)
        '''
        if self.state == self.COUNTING:
            interval = time.time() - self.start_time
            self.display += interval
            self.start_time = None
            self.state = self.PAUSED
            return self.display
        elif self.state in [self.STOPPED, self.PAUSED]:
            return self.display
        else:
            raise Exception('[-] stopwatch.pause() error!')

    def stop(self):
        '''
        Stop timer and return

        return: measured time(secs)
        '''
        display = self.pause()
        self.display = 0
        self.state = self.STOPPED
        return display

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
