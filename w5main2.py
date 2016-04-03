userA=raw_input("userA input r,s,p:")
userB=raw_input("userB input r,s,p:")
if userA==userB:
    print "draw"
elif userA=='r':
    if userB=='s':
        print "userA win"
    elif userB=='p':
        print "userB win"
elif userA=='s':
    if userB=='r':
        print "userB win"
    elif userB=='p':
        print "userA win"
elif userA=='p':
    if userB=='r':
        print "userA win"
    elif userB=='s':
        print "userB win"
    