n = int(input())

cards = list(i for i in input().split() if i == '5')

five_cards = len(cards)
zero_cards = n - five_cards

'''
1) In case for a number to be divisible by 90, it should be divisible by 10 and 9
    1.1) For a number to be divisible by 10 its decimal digit should be 0
    1.2) For a number to be divisible by 9 sum of its digits must be divisible by 9

2) We counted the 5 numbered cards as 'five_cards'
    2.1) If all the input cards are 5 then solution doesn't exists as it won't follow (1.1)
        2.1.1) therefore; if five_cards == n or zero_cards == 0, code returns -1

3) Interestingly 0 is divisible by 9 and we cannot put leading zeroes in left of our number
    3.1) If we put zero its addition to sum remains 0 and the number is unchanged
    3.2) But we can put 5s in the left and zero in the right
    3.3) We should put 5s in a fashion so that the sum is divisible by 9
        3.3.1) fashion : sum += 45, atleast 9 5's in a single step
'''

if five_cards == n:
    print(-1)

else:
    while five_cards > -1:
        sum = 0
        max_five_cards = five_cards
        maximum = ''
        maximum += '5' * five_cards
        for i in maximum:
            sum += int(i)
        if sum % 9 == 0:
            break

        five_cards -= 1
    
    if max_five_cards == 0:
        print('0')
    else:
        print('5' * max_five_cards + '0' * zero_cards)
