'''
This script provides stopwatch, current time check.

Defined vars: 
Defined funcs: 
Defined classes: StopWatch(), Now(lang)
'''


import time


class StopWatch:
    '''
    Measure interval time
    unit: second(s)
    '''
    def start(self):
        '''
        Start measure
        '''
        self.start_ = time.time()

    def end(self, acc=2):
        '''
        End measure and print spended time
        
        acc: ndigits to round. if -1, print all digits.
        '''
        self.interval = time.time() - self.start_
        if acc == -1:
            print('Spend time: ' + str(self.interval) + 's')
        else:
            interval = round(self.interval, acc)
            print('Spend time: ' + str(interval) + 's')


class Now:
    '''
    Object about now!
    based local time
    12-hour clock
    support lang: eng(usa), kor
    
    member:
        lang - language
        year - year
        mon - month
        day - day
        hour - hour
        hour_range - 'am' or 'pm'
        min - minutes
        wday - day of the week
        date - date string('yyyy-mm-dd www' or 'www, mm-dd-yyyy')
        time - time string(hh:mm:ss)
        struct_time - struct_time obj
    '''
    def __init__(self, lang='kor'):
        '''
        Initialize member var.
        
        lang: 'kor' or 'eng'. Default 'kor'.
        '''
        tm = time.localtime()
        self.year = tm.tm_year
        self.mon = tm.tm_mon
        self.day = tm.tm_mday
        # Set hour
        if tm.tm_hour > 12:
            self.hour = tm.tm_hour - 12
            self.hour_range = 'pm'
        else:
            self.hour = tm.tm_hour
            self.hour_range = 'am'
        self.min = tm.tm_min
        self.sec = tm.tm_sec
        # Set wday
        wday = tm.tm_wday
        if wday == 0:
            if lang == 'kor':
                self.wday = '월요일'
            elif lang == 'eng':
                self.wday = 'Monday'
        elif wday == 1:
            if lang == 'kor':
                self.wday = '화요일'
            elif lang == 'eng':
                self.wday = 'Tuesday'
        elif wday == 2:
            if lang == 'kor':
                self.wday = '수요일'
            elif lang == 'eng':
                self.wday = 'Wednesday'
        elif wday == 3:
            if lang == 'kor':
                self.wday = '목요일'
            elif lang == 'eng':
                self.wday = 'Thursday'
        elif wday == 4:
            if lang == 'kor':
                self.wday = '금요일'
            elif lang == 'eng':
                self.wday = 'Friday'
        elif wday == 5:
            if lang == 'kor':
                self.wday = '토요일'
            elif lang == 'eng':
                self.wday = 'Saturday'
        elif wday == 6:
            if lang == 'kor':
                self.wday = '일요일'
            elif lang == 'eng':
                self.wday = 'Sunday'
        # Set date
        if lang == 'kor':
            self.date = time.strftime('%Y-%m-%d ', tm) + self.wday
        elif lang == 'eng':
            self.date = time.strftime('%a, %m-%d-%Y', tm)
        self.time = time.strftime('%I:%M:%S %p', tm)
        self.struct_time = tm
        self.lang = lang

    def get_time_stamp(self):
        '''
        Return TimeStamp
        '''
        return time.time()

    def get_date_time(self):
        '''
        Return full date time string
        '''
        return self.date + ' ' + self.time


def test_StopWatch():
    w = StopWatch()
    w.start()
    time.sleep(1)
    w.end()


def test_Now():
    now = Now(lang='kor')
    print(now.year,now.mon,now.day,now.hour,now.hour_range,now.min,now.sec,now.wday,now.date,now.time,sep=' ',end='\n\n')
    print(now.get_date_time())
    print(now.get_time_stamp())


if __name__ == '__main__':
    test_Now()
