words1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
words3 = ['trillion', 'billion', 'million', 'thousand', 'hundred']

def stn(num):
    rem, say = num, ''
    for i, exp in enumerate([12, 9, 6, 3, 2]):
        q, rem = divmod(rem, 10**exp)
        if q > 0:
            if say: say += ', '
            say += stn(q) + ' ' + words3[i]
    if say and rem: say += ' and '
    if rem < 20:
        if rem: say += words1[rem]
    else: 
        q, rem = divmod(rem-20, 10)
        say += words2[q]
        if rem: say += '-' + stn(rem)
    return say

def say_the_number(num):
    if num == 0:
        return 'Zero.'
    say = stn(num)
    return say[0].upper() + say[1:] + '.'
