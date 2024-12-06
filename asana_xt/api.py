# Copyright 2024 Virgilio "Jan" So
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import uuid
import requests


class AsanaAPI:
    BASE_URL = "https://app.asana.com/api/1.0"

    def __init__(self, token):
        self.headers = {
            "accept": "application/json",
            "authorization": f"Bearer {token}",
            "content-type": "application/json"
        }

    def fetch_workspaces(self):
        """
        Fetches the list of workspaces available in the Asana account.

        Returns:
            dict: JSON response containing workspaces data, or None if an error occurs.
        """
        response = requests.get(f"{self.BASE_URL}/workspaces", headers=self.headers)
        return response.json()

    def fetch_users(self):
        """
        Fetches the list of users available in the Asana account.

        Returns:
            dict: JSON response containing users data, or None if an error occurs.
        """
        response = requests.get(f"{self.BASE_URL}/users", headers=self.headers)
        return response.json()

    def fetch_projects(self):
        """
        Fetches the list of projects available in the Asana account.

        Returns:
            dict: JSON response containing projects data, or None if an error occurs.
        """
        response = requests.get(f"{self.BASE_URL}/projects", headers=self.headers)
        return response.json()

    def create_task(self, subject, notes, assignee_user_gid, project_gid, workspace_gid):
        """
        Creates a new task in the Asana account.

        Args:
            subject (str): Subject of the task.
            notes (str): Notes of the task.
            assignee_user_gid (str): GID of the user to assign the task to.
            project_gid (str): GID of the project to add the task to.
            workspace_gid (str): GID of the workspace of the project.

        Returns:
            requests.Response: Response from the API.
        """
        gid = str(uuid.uuid4())
        task_data = {
            "data": {
                "external": {"gid": gid, "data": "TODO1"},
                "name": subject,
                "resource_subtype": "default_task",
                "approval_status": "pending",
                "assignee_status": "upcoming",
                "completed": False,
                "html_notes": (
                   notes
                ),
                "liked": True,
                "notes": "TODO2.",
                "assignee": assignee_user_gid,
                "projects": [project_gid],
                "workspace": workspace_gid
            }
        }
        response = requests.post(f"{self.BASE_URL}/tasks", headers=self.headers, json=task_data)
        return response
