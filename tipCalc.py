amount = raw_input("How much was the total bill? \n")
serv = raw_input("How good was the service? (good, fair, bad)")

if serv == 'good':
    tip = float(amount) * .2
elif serv == 'fair':
    tip = float(amount) * .15
elif serv == 'bad':
    tip = float(amount) * .1
else:
    print "invalid amount!"

total = float(tip) + float(amount)

print "Tip amount: %0.2f" % tip
print "Total amount: %0.2f" % total
