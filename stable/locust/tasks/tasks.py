from locust import HttpLocust, TaskSet, task
import json, requests

class ElbTasks(TaskSet):
  @task
  def task1(self):
    self.client.get("/dev")

class ElbWarmer(HttpLocust):
  task_set = ElbTasks
  min_wait = 1000
  max_wait = 3000