user_num = int(input('Input number less or equal then 8640000: '))

seconds_tpl = divmod(user_num, 60)
minutes_tpl = divmod(seconds_tpl[0], 60)
hours_tpl = divmod(minutes_tpl[0], 24)

seconds = str(seconds_tpl[1]).zfill(2)
minutes = str(minutes_tpl[1]).zfill(2)
hours = str(hours_tpl[1]).zfill(2)
days = str(hours_tpl[0])

if days[-1] in ('5', '6', '7', '8', '9', '0') or (len(days) == 2 and days[0] == '1'):
    word_days = 'днів'
elif days[-1] == '1':
    word_days = 'день'
elif days[-1] in ('2', '3', '4'):
    word_days = 'дні'

print(days, word_days + ",", hours + ":" + minutes + ":" + seconds)
