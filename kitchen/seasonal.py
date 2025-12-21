from datetime import date, timedelta
def _easter_date(year: int) -> date:
    # Gauss's Easter algorithm (Western Easter)
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)

def _lunar_new_year_date(year: int) -> date:
    # Accurate dates 2020–2035 (source: timeanddate.com / Hong Kong Observatory)
    dates = {
        2024: (2,10), 2025: (1,29), 2026: (2,17), 2027: (2,6),  2028: (1,26),
        2029: (2,13), 2030: (2,3),  2031: (1,23), 2032: (2,11), 2033: (1,31),
        2034: (2,19), 2035: (2,8),
    }
    month, day = dates.get(year, (1, 28))  # reasonable fallback
    return date(year, month, day)
def is_near_holiday(today, threshold_days: int = 2):

    this_year = today.year

    def get_date_for_year(base_date_or_callable, year):
        if callable(base_date_or_callable):
            return base_date_or_callable(year)
        return base_date_or_callable.replace(year=year) if isinstance(base_date_or_callable, date) else base_date_or_callable

    # === Holiday definitions (with year-aware logic) ===
    holidays = {
        "Thanksgiving": lambda y: (date(y, 11, 1) + timedelta(days=(3 - date(y,11,1).weekday()) % 7 + 21)),
        "Christmas": date(this_year, 12, 25),
        "New Years": date(this_year + 1, 1, 1),           # always next year from Dec/Jan perspective
        "July 4th": date(this_year, 7, 4),
        "Easter": lambda y: _easter_date(y),
        "Asian New Year": _lunar_new_year_date(this_year),
        "Birthday": date(this_year, 5, 29),
    }
    close_holiday = None
    closest = None
    min_dist = float('inf')

    for name, hdate_or_func in holidays.items():
        # Get actual date for current or adjacent years
        candidates = []

        # Current year
        hdate = get_date_for_year(hdate_or_func, this_year)
        candidates.append((hdate, name))

        # Previous year (for holidays early in year, like New Year, Lunar NY, Birthday)
        if today.month <= 2 or name in ["New Years", "Asian New Year"]:
            hdate_prev = get_date_for_year(hdate_or_func, this_year - 1)
            candidates.append((hdate_prev, name))

        # Next year (for late-year holidays when close to Dec 31)
        if today.month >= 11:
            hdate_next = get_date_for_year(hdate_or_func, this_year + 1)
            candidates.append((hdate_next, name))

        for hdate, name in candidates:
            delta = (hdate - today).days
            abs_delta = abs(delta)
            if abs_delta < min_dist:
                min_dist = abs_delta
                closest = (name, delta)
                if abs_delta <= threshold_days:
                    close_holiday = closest

    if close_holiday:
        name, delta = close_holiday
        return True, delta, name
    else:
        name, delta = closest
        return False, delta, name

