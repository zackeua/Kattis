import sys
import decimal

data = decimal.Decimal(list(sys.stdin)[0])
#print((data*1000*5280/4854))
print((data*1000*5280/4854).to_integral_value())
