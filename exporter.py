import csv


def save_to_file(jobs):

    file = open("jobs-exported.csv", mode="w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    # print(jobs)

    for job in jobs:
        writer.writerow(job.values())
        # print(job.values())

    return
