def season_events(number_of_month):
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    season_descriptions = {
        "winter": "White snow fell outside the window",
        "spring": "Birds sang beautiful songs",
        "summer": "The sun shone brighter than ever",
        "autumn": "The harvest was incredible"
    }

    if not isinstance(number_of_month, int) or number_of_month < 1 or number_of_month > 12:
        print("You need to enter the real number of the month.")
        return

    month_name = month_names.get(number_of_month)
    if number_of_month in [1, 2, 12]:
        season = "winter"
    elif number_of_month in [3, 4, 5]:
        season = "spring"
    elif number_of_month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"

    print(f"You were born in {month_name}. {season_descriptions[season]}")

season_events(3)
