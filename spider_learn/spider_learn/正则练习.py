from locust import HttpLocust,task,TaskSet
#
# class BestTest(TaskSet):
#     def __index__(self):
#         self.clent.get('/')
#
# class BestTestIndexUser(HttpLocust):
#     task_set = BestTest
class UserBehavior(TaskSet):
    @task(3)
    def index(self):
        self.client.get('/movie')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000