def get_fair_info(fair_dict, current_time):
    output = {
        "number_of_days": 1,
        "start_time": fair_dict["first_start_time"],
        "end_time": None,
        "in_progress": False,
    }

    if fair_dict["third_end_time"]:
        output["number_of_days"] = 3
        output["end_time"] = fair_dict["third_end_time"]
    elif fair_dict["second_end_time"]:
        output["number_of_days"] = 2
        output["end_time"] = fair_dict["second_end_time"]
    else:
        output["end_time"] = fair_dict["first_end_time"]

    if output["start_time"] < current_time < output["end_time"]:
        output["in_progress"] = True

    return output
