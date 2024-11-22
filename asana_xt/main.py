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
import os
import argparse
import json
from asana_xt.api import AsanaAPI


def load_profile(json_file, profile_name):
    """Load profile details from the JSON file based on the profile name."""
    with open(json_file, "r") as f:
        data = json.load(f)

    profile = next((profile for profile in data["profiles"] if profile["profile_name"] == profile_name), None)
    if not profile:
        raise ValueError(f"Profile '{profile_name}' not found in {json_file}.")

    return profile


def get_notes_content(notes):
    """Fetch notes content from file or URL and ensure it is wrapped in <body> tags."""
    if os.path.isfile(notes):
        with open(notes, "r") as file:
            content = file.read()
    else:
        content = notes

    # Ensure the content is wrapped in <body> tags if not already wrapped
    if not content.strip().startswith("<body>"):
        content = f"<body>{content}</body>"

    return content


def create_ticket(project_name, assignee_name, subject, notes):
    token = os.getenv("ASANA_API_TOKEN")
    if not token:
        raise ValueError("ASANA_API_TOKEN environment variable is not set.")

    asana_api = AsanaAPI(token)

    # Fetch workspaces
    workspaces = asana_api.fetch_workspaces()
    if not workspaces.get("data"):
        raise ValueError("No workspaces found.")

    workspace = workspaces["data"][0]
    workspace_gid = workspace["gid"]

    # Fetch users
    users = asana_api.fetch_users()
    user_details = next((user for user in users["data"] if user["name"] == assignee_name), None)
    if not user_details:
        raise ValueError(f"User '{assignee_name}' not found.")

    user_gid = user_details["gid"]

    # Fetch projects
    projects = asana_api.fetch_projects()
    project_details = next((project for project in projects["data"] if project["name"] == project_name), None)
    if not project_details:
        raise ValueError(f"Project '{project_name}' not found.")

    project_gid = project_details["gid"]

    # Create a task
    response = asana_api.create_task(
        subject=subject,
        notes=notes,
        assignee_user_gid=user_gid,
        project_gid=project_gid,
        workspace_gid=workspace_gid
    )
    return response.text


def main():
    parser = argparse.ArgumentParser(description="Create an Asana ticket based on profile details.")
    parser.add_argument("--profile", required=True, help="Profile name from the JSON file.")
    parser.add_argument("--config", default="asana_xt.json", help="Path to the JSON configuration file.")

    args = parser.parse_args()
    try:

        profile = load_profile(args.config, args.profile)

        subject = profile["subject"]
        notes = get_notes_content(profile["notes"])
        project_name = profile["project_name"]
        assignee_name = profile["assignee_name"]

        response = create_ticket(project_name, assignee_name, subject, notes)
        print(f"Task created successfully: {response}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
