from datetime import datetime, timedelta
from ..models import CraftFair


def get_fair_status(fair_dict):
    output = {
        "number_of_days": 1,
        "start_time": fair_dict["first_start_time"],
        "end_time": None,
        "in_progress": False,
        "future_none": False,
    }

    if fair_dict["third_end_time"]:
        output["number_of_days"] = 3
        output["end_time"] = fair_dict["third_end_time"]
    elif fair_dict["second_end_time"]:
        output["number_of_days"] = 2
        output["end_time"] = fair_dict["second_end_time"]
    else:
        output["end_time"] = fair_dict["first_end_time"]

    if output["start_time"] < datetime.now() < output["end_time"]:
        output["in_progress"] = True

    return output

def create_unknown_future_fair():
    '''
    Deals with an edge case when there is no future fair
    '''
    output = {
        "number_of_days": 1,
        "start_time": datetime.now() + timedelta(days=365),
        "end_time": None,
        "in_progress": False,
        "future_none": True,
    }
    return output


def get_fair_details():
    four_days_ago = datetime.now() + timedelta(days=-4)
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

    try:
        fair_info = get_fair_status(fair_dict[0])
    except IndexError:
        fair_info = create_unknown_future_fair()
        fairs_past = CraftFair.objects.exclude(first_start_time__gt=datetime.now()).order_by(
        "-first_start_time"
        )
        return fairs_past[0], fair_info

    # case where fair is happening now show the next fair
    if fair_info["end_time"] < datetime.now():
        fair = fair_q[1]
        fair_info = get_fair_status(fair_dict[1])
    else:
        fair = fair_q[0]
        
    return fair, fair_info


def sort_fairs():
    fairs_future = CraftFair.objects.exclude(
        first_start_time__lt=datetime.now()
    ).order_by("first_start_time")
    fairs_past = CraftFair.objects.exclude(first_start_time__gt=datetime.now()).order_by(
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
