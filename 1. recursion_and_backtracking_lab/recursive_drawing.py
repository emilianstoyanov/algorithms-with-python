def drawing(n):
    if n == 0:
        return
    print("*" * n)
    drawing(n - 1)
    print("#" * n)


# 5
n = int(input())
drawing(n)

""" 

*****
****
***
**
*
#
##
###
####
#####

"""
