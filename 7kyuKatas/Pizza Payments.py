def michael_pays(costs):
    if costs < 5: return float("{:.2f}".format(costs))
    else:
        if costs/3 <= 10: return float("{:.2f}".format(costs*(2/3)))
        else: return float("{:.2f}".format(costs-10))
