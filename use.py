import time
import datetime
import json
import sys


def is_date_time(date_time_str):
    try:
        time.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


def get_difference(query_stamp, now_stamp):
    cle = query_stamp - now_stamp
    d, h, m, s = 0, 0, 0, 0
    if cle > 0:
        d, r = divmod(cle, 3600 * 24)
        h, r = divmod(r, 3600)
        m, s = divmod(r, 60)
    elif cle < 0:
        d, r = divmod(abs(cle), 3600 * 24)
        h, r = divmod(r, 3600)
        m, s = divmod(r, 60)
    return f"当前时间差 {d} 天 {h} 小时 {m} 分 {s} 秒"


def get_time_stamp(query):
    now = time.time()
    query = query.strip()
    if query == 'now':
        results = [
            {
                'title': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)),
                'subtitle': '系统时间',
                'arg': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)),
                'icon': 'icon.png'
            },
            {
                'title': time.strftime('%Y%m%d%H%M%S', time.localtime(now)),
                'subtitle': '系统时间',
                'arg': time.strftime('%Y%m%d%H%M%S', time.localtime(now)),
                'icon': 'icon.png'
            },
            {
                'title': str(int(now*1000)),
                'subtitle': '毫秒时间毫秒戳',
                'arg': str(int(now*1000)),
                'icon': 'icon.png'
            },
            {
                'title': str(int(now)),
                'subtitle': '系统时间戳',
                'arg': str(int(now)),
                'icon': 'icon.png'
            }
        ]
        return results

    if query.isnumeric():
        query_stamp = int(query)
        if len(query) == 10:
            query_stamp = datetime.datetime.fromtimestamp(
                query_stamp).strftime('%Y-%m-%d %H:%M:%S')
        elif len(query) == 13:
            query_stamp = datetime.datetime.fromtimestamp(
                query_stamp / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        else:
            return
        results = [
            {
                'title': query_stamp,
                'subtitle': '目标时间',
                'arg': query_stamp,
                'icon': 'icon.png'
            }
        ]
        return results

    if is_date_time(query):
        query_stamp = time.mktime(time.strptime(query, '%Y-%m-%d %H:%M:%S'))
        results = [
            {
                'title': str(int(query_stamp)),
                'subtitle': '目标时间戳',
                'arg': str(int(query_stamp)),
                'icon': 'icon.png'
            },
            {
                'title': str(int(query_stamp*1000)),
                'subtitle': '目标时间毫秒戳',
                'arg': str(int(query_stamp*1000)),
                'icon': 'icon.png'
            }
        ]
        return results


query = sys.argv[1]

items = get_time_stamp(query)
if items != None:
    # 输出 JSON 数组
    result = {"items": items}
    print(json.dumps(result))
