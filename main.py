from save import save_to_file
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs


so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()

jobs = so_jobs + indeed_jobs
# jobs = indeed_jobs
# print(jobs)

save_to_file(jobs)
