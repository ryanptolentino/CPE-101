def float_default(string, default):
    try:
        return float(string)
    except ValueError:
        return default


