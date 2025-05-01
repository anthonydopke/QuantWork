import QuantLib as ql

# Set evaluation date
calendar = ql.UnitedStates()
today = ql.Date.todaysDate()
ql.Settings.instance().evaluationDate = today

# Define market quotes (example rates)
depo_rate = ql.SimpleQuote(0.01)
swap_rate = ql.SimpleQuote(0.015)

# Build helpers
helpers = [
    ql.DepositRateHelper(ql.QuoteHandle(depo_rate), ql.Period("3M"), 2, calendar, ql.ModifiedFollowing, False, ql.Actual360()),
    ql.SwapRateHelper(ql.QuoteHandle(swap_rate), ql.Period("5Y"), calendar, ql.Annual, ql.Unadjusted, ql.Thirty360(), ql.Euribor6M())
]

# Construct the curve
curve = ql.PiecewiseLogCubicDiscount(today, helpers, ql.Actual365Fixed())

# Access pillar dates and corresponding zero rates
pillars = curve.dates()
print("Pillar Dates and Zero Rates:")
for date in pillars:
    t = ql.Actual365Fixed().yearFraction(today, date)
    zero_rate = curve.zeroRate(t, ql.Compounded, ql.Annual).rate()
    print(f"{date} -> {zero_rate:.6%}")
