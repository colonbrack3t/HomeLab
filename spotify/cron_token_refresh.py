from django_cron import CronJobBase, Schedule
import requests
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 50 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print("getting token")
        x = requests.get('http://192.168.0.14:8000/spotify/login')
        open ("return", "w").write(x.text)
