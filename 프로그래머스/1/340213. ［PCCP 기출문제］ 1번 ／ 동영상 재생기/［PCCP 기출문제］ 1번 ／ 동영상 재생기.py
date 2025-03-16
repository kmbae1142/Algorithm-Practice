def minute(time_list):
    temp_t = list(map(int, time_list.split(":")))
    return 60 * temp_t[0] + temp_t[1]

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_min = minute(video_len)
    pos_min = minute(pos)
    op_start_min = minute(op_start)
    op_end_min = minute(op_end)
    
    for command in commands:
        if command == "next":
            if pos_min + 10 >= video_min:
                pos_min = video_min
            elif op_start_min <= pos_min <= op_end_min:
                pos_min = op_end_min + 10
            else:
                pos_min = pos_min + 10

        elif command == "prev":
            if pos_min <= 10:
                pos_min = 0
            elif op_start_min <= pos_min <= op_end_min:
                pos_min = op_end_min
            else:
                pos_min = pos_min - 10
        
    if op_start_min <= pos_min <= op_end_min:
        pos_min = op_end_min
                
    h = str(pos_min // 60) if pos_min // 60 >= 10 else "0" + str(pos_min // 60)
    m = str(pos_min % 60) if pos_min % 60 >= 10 else "0" + str(pos_min % 60)
        
    answer = h + ":" + m
        
    return answer