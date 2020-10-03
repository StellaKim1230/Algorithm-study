def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    # 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
    # 처음차가 마지막차가 될수 없으니 n-1을 해준다.
    lastTime = (540) + (n-1)*t

    for i in range(n):
        # timetable이 m보다 작을경우 마지막차에 타면 된다.
        if len(timetable) < m: return '%02d:%02d'%(lastTime//60,lastTime%60)

        # timetable이 m과 크거나 같을경우 timetable의 마지막 사람의 1분보다 먼저 도착하면 된다.
        if len(timetable) >= m:
            lastTime = timetable[len(timetable) - 1] -1
            return '%02d:%02d'%(lastTime//60,lastTime%60)

        # 나머지조건 (?)
        # n: 1, t: 1, m: 1, timetable:['23:59']
    return answer