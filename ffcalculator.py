def calculate_future_value(x, y, n):
    """
    计算n年后的总收益值
    :param x: 年回报率 (百分比形式，例如5%表示为0.05)
    :param y: 每年投入金额
    :param n: 投资年数
    :return: 第n年的当年收益，n年的累计净收益值，n年后的总金额
    """
    total_value = 0
    nth_year_return = 0
    for year in range(1, n + 1):
        total_value = (total_value + y) * (1 + x)
        if year == n:
            nth_year_return = total_value - (total_value / (1 + x))
    total_return=total_value-n*y
    return nth_year_return,total_return,total_value

# 示例参数
annual_return_rate = 0.07  # 年回报率5%
annual_investment = 1  # 每年投入金额10000
years = 10  # 投资10年

nth_year_return,total_return,total_value = calculate_future_value(annual_return_rate, annual_investment, years)

print(f"第{years}年的收益值是: {nth_year_return:.2f}")
print(f"{years}年累计净收益值是: {total_return:.2f}")
print(f"{years}年后的总金额是: {total_value:.2f}")

