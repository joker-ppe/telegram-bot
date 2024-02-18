from enum import Enum
import re

class TypeAction(Enum):
    OS_CONG_TY = 1
    OS_SUPER = 2
    OS_MASTER = 3
    OS_AGENT = 4
    OS_MEMBER = 5
    DOANH_THU_CONG_TY = 6
    THAU_NGOAI = 7
    SUPER = 8
    MASTER = 9
    AGENT = 10
    MEMBER = 11

def detect_os_cong_ty(text):
    words = ['os công ty', 'outstanding công ty', 'os cong ty', 'os cty']
    return detect_action(text, words)

def detect_os_super(text):
    words = ['os cổ đông', 'os co dong', 'os cd', 'os super']
    return detect_action(text, words)

def detect_os_master(text):
    words = ['os tổng đại lý', 'os tong dai ly', 'os tong dl', 'os master']
    return detect_action(text, words)

def detect_os_agent(text):
    words = ['os đại lý', 'os dai ly', 'os dly', 'os agent']
    return detect_action(text, words)

def detect_os_member(text):
    words = ['os hội viên', 'os hoi vien', 'os hv', 'os member']
    return detect_action(text, words)

def detect_doanh_thu_cong_ty(text):
    words = ['doanh thu công ty', 'doanh thu cty', 'doanh thu cong ty']
    return detect_action(text, words)

def detect_thau_ngoai(text):
    words = ['thầu ngoài', 'thau ngoai', 'tn']
    return detect_action(text, words)

def detect_super(text):
    words = ['cổ đông', 'co dong', 'cd', 'super']
    return detect_action(text, words)

def detect_master(text):
    words = ['tổng đại lý' , 'tong dai ly', 'tong dl', 'master']
    return detect_action(text, words)

def detect_agent(text):
    words = ['đại lý', 'dai ly', 'dl', 'dly', 'agent']
    return detect_action(text, words)

def detect_member(text):
    words = ['hội viên', 'hoi vien', 'hv', 'member']
    return detect_action(text, words)

def detect_member_info(text):
    words = ['thông tin', 'thong tin', 'ttin', 'info', 'infor']
    return detect_action(text, words)

def detect_member_info_tet(text):
    words = ['thông tin tết', 'thong tin tet', 'ttin tet', 'info tết', 'infor tết']
    return detect_action(text, words)

def detect_member_info_last_week(text):
    words = ['thông tin tuần trước', 'thong tin tuan truoc', 'ttin tuan truoc', 'info last week', 'infor last week', 'info tuan truoc', 'infor tuan truoc', 'info tuần trước', 'infor tuần trước']
    return detect_action(text, words)

def detect_member_info_os_number(text):
    words = ['os số', 'os so', 'os number',]
    return detect_action(text, words)

def detect_member_info_os_bet(text):
    words = ['os phiếu cược', 'os phieu cuoc', 'os cuoc', 'os cược', 'os bet',]
    return detect_action(text, words)

def detect_report_number(text):
    words = ['báo cáo số', 'bao cao so']
    return detect_action(text, words)

def detect_report_xsmb(text):
    words = ['xổ số miền bắc', 'xo so mien bac', 'xsmb']
    return detect_action(text, words)

def detect_guide(text):
    words = ['cú pháp', 'cu phap', 'hướng dẫn', 'huong dan']
    return detect_action(text, words)

def detect_report_super(text):
    words = ['report', 'báo cáo', 'bao cao']
    return detect_action(text, words)

def detect_report_super_tet(text):
    words = ['report tết', 'báo cáo tết', 'bao cao tet']
    return detect_action(text, words)

def detect_member_inactive(text):
    words = ['member ko cược', 'member không cược']
    return detect_action(text, words)

def detect_guide_report_list(text):
    words = ['report list']
    return detect_action(text, words)
#////////////////////////////////////////////////////////////////
def detect_yesterday(text):
    words = ['hôm qua', 'hom qua', 'hqua', 'hqa']
    return detect_action(text, words)
def detect_today(text):
    words = ['hôm nay', 'hom nay', 'hnay']
    return detect_action(text, words)
def detect_this_week(text):
    words = ['tuần này', 'tuan nay']
    return detect_action(text, words)
def detect_last_week(text):
    words = ['tuần trước', 'tuan truoc']
    return detect_action(text, words)

def detect_action(text, words):
    for word in words:
        if word_in_text(word.lower(), text.lower()):
            print('detect word: ' + word)
            return True
    return False


def word_in_text(word, text):
    # This regular expression pattern looks for the whole word
    pattern = r'\b' + re.escape(word) + r'\b'
    return bool(re.search(pattern, text.replace('.',''), re.IGNORECASE))