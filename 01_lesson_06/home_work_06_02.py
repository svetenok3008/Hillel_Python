user_num = int(input('Input number less or equal then 8640000: '))

seconds_tpl = divmod(user_num, 60)
minutes_tpl = divmod(seconds_tpl[0], 60)
hours_tpl = divmod(minutes_tpl[0], 24)

seconds = str(seconds_tpl[1]).zfill(2)
minutes = str(minutes_tpl[1]).zfill(2)
hours = str(hours_tpl[1]).zfill(2)
days = str(hours_tpl[0])

print("First method:")

days_dict = {
    '1':'день',
    '2':'дні',
    '3':'дні',
    '4':'дні',
    '5':'днів',
    '6':'днів',
    '7':'днів',
    '8':'днів',
    '9':'днів',
    '0':'днів'
}
print(days, days_dict[days[-1]] +",", hours + ":" + minutes + ":" + seconds)

print("Second method:")
if days[-1] == '1':
    word_days = 'день'
elif days[-1] in ('2','3','4'):
    word_days = 'дні'
elif days[-1] in ('5','6','7','8','9','0'):
    word_days = 'днів'

print(days, word_days +",", hours + ":" + minutes + ":" + seconds)