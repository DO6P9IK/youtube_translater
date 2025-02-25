


def convert_time_to_seconds(time_str):
    """Преобразует время в формате 'hh:mm:ss.ms' в секунды."""
    hours, minutes, seconds = time_str.split(':')
    seconds, milliseconds = seconds.split('.')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000


pars_subtitle = []

with open('THIS is Why List Comprehension is SO Efficient! [U88M8YbAzQk].ru.vtt', 'r', encoding='utf-8') as file:
    for _ in range(4):
        file.readline().strip() 

    work_to_line = [el for el in file.readline().strip().replace(' --> ', ' ').split()][:2]
    el = list(map(convert_time_to_seconds, work_to_line))

    for _ in range(4):
        file.readline().strip()

    text = file.readline().strip()
    pars_subtitle.append({'start': el[0], 'end': el[1], 'text': text})
    
    count = 0
    for line in file:
        if count == 2:
            work_to_line = [el for el in line.strip().replace(' --> ', ' ').split()][:2]
            time_phrase = list(map(convert_time_to_seconds, work_to_line))
        if count == 7:
            pars_subtitle.append({'start': time_phrase[0], 'end': time_phrase[1], 'text': line.strip()})
            count = -1
        count += 1

print(pars_subtitle)
