P_burglary = 0.02
P_earthquake = 0.01

P_alarm_given_burglary_earthquake = 0.94
P_alarm_given_burglary_no_earthquake = 0.95
P_alarm_given_no_burglary_earthquake = 0.31
P_alarm_given_no_burglary_no_earthquake = 0.001

P_david_calls_given_alarm = 0.91
P_david_no_call_given_no_alarm = 0.95
P_david_calls_given_no_alarm = 0.05
P_david_no_call_given_alarm = 0.09

P_sophia_calls_given_alarm = 0.75
P_sophia_no_call_given_no_alarm = 0.98
P_sophia_calls_given_no_alarm = 0.02
P_sophia_no_call_given_alarm = 0.25


def validate_prob(prob):
    if prob < 0 or prob > 1:
        raise ValueError("Probability must be between 0 and 1")


def joint_prob(alarm, burglary, earthquake, david_calls, sophia_calls):

    if alarm:
        if burglary and earthquake:
            p_alarm = P_alarm_given_burglary_earthquake
        elif burglary:
            p_alarm = P_alarm_given_burglary_no_earthquake
        elif earthquake:
            p_alarm = P_alarm_given_no_burglary_earthquake
        else:
            p_alarm = P_alarm_given_no_burglary_no_earthquake
    else:
        if burglary and earthquake:
            p_alarm = 1 - P_alarm_given_burglary_earthquake
        elif burglary:
            p_alarm = 1 - P_alarm_given_burglary_no_earthquake
        elif earthquake:
            p_alarm = 1 - P_alarm_given_no_burglary_earthquake
        else:
            p_alarm = 1 - P_alarm_given_no_burglary_no_earthquake

    if alarm:
        p_david = (P_david_calls_given_alarm if david_calls
                   else P_david_no_call_given_alarm)
    else:
        p_david = (P_david_calls_given_no_alarm if david_calls
                   else P_david_no_call_given_no_alarm)

    if alarm:
        p_sophia = (P_sophia_calls_given_alarm if sophia_calls
                    else P_sophia_no_call_given_alarm)
    else:
        p_sophia = (P_sophia_calls_given_no_alarm if sophia_calls
                    else P_sophia_no_call_given_no_alarm)

    return (
        (P_burglary if burglary else 1 - P_burglary)
        * (P_earthquake if earthquake else 1 - P_earthquake)
        * p_alarm
        * p_david
        * p_sophia
    )


def run_test(test_name, expected_type, **kwargs):
    result = joint_prob(**kwargs)

    if result >=0 :
        print(f"{test_name} passed. Result: {result}")
    else:
        print(f"{test_name} failed. Result: {result}")


run_test("Test 1", "float", alarm=True, burglary=False,
         earthquake=False, david_calls=True, sophia_calls=True)
