from datetime import datetime, timedelta
from ..models import CraftFair


current_time = datetime.now()


def get_fair_status(fair_dict):
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


def get_fair_details():
    four_days_ago = current_time + timedelta(days=-4)
    fair_q = CraftFair.objects.exclude(first_start_time__lt=four_days_ago).order_by(
        "first_start_time"
    )
    fair_dict = fair_q.values(
        "id",
        "first_start_time",
        "first_end_time",
        "second_end_time",
        "third_end_time",
    )
    fair_info = get_fair_status(fair_dict[0])
    if fair_info["end_time"] < current_time:
        fair = fair_q[1]
        fair_info = get_fair_status(fair_dict[1])
    else:
        fair = fair_q[0]
    return fair, fair_info


def sort_fairs():
    fairs_future = CraftFair.objects.exclude(
        first_start_time__lt=current_time
    ).order_by("first_start_time")
    fairs_past = CraftFair.objects.exclude(first_start_time__gt=current_time).order_by(
        "-first_start_time"
    )
    last_fair_dict = fairs_past.values(
        "id",
        "first_start_time",
        "first_end_time",
        "second_end_time",
        "third_end_time",
    )
    last_fair_info = get_fair_status(last_fair_dict[0])
    fair_in_progress = last_fair_info["in_progress"]
    return fairs_future, fairs_past, fair_in_progress
