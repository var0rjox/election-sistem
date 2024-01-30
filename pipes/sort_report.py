"""
    {
        "Partido1": {
            "votes": 10,
            "percentage": 10,
        },
        "Partido2": {
            "votes": 20,
            "percentage": 20,
        },
    }
"""


def sort_report(details_report):
    sort_report = {}
    array_details = []

    for party in details_report:
        if details_report[party]["data"]:
            array_details.append(details_report[party])
        else:
            array_details.append(
                {
                    "votes": details_report[party]["votes"],
                    "percentage": details_report[party]["percentage"],
                    "name": party,
                }
            )

    array_details.sort(key=lambda x: x["votes"], reverse=True)

    for party in array_details:
        if not "data" in party:
            sort_report[party["name"]] = {
                "votes": party["votes"],
                "percentage": party["percentage"],
            }
        else:
            sort_report[party["data"].name] = {
                "votes": party["votes"],
                "percentage": party["percentage"],
            }

    return sort_report
