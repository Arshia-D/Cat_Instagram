from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def index_page(self):
        self.client.get("/")
