import re

import requests
from bs4 import BeautifulSoup
import json


# Create an empty list to store the package data
packages = []

# Load the requirements file
with open('requirements.txt', 'r') as f:
    lines = f.readlines()

# For each line in the requirements file...
i = 0

for line in lines:
    try:
        i += 1
        name, version = line.strip().split('==')

        # url = f'https://pypi.org/project/{name}/{version}/'
        # version may outdated
        url = f'https://pypi.org/project/{name}/'
        # Fetch the PyPI page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # summary
        summary = soup.find('p', {'class': 'package-description__summary'})
        try:
            summary = summary.text.strip()
        except AttributeError:
            summary = ''

        # Extract the project links
        project_links_div = soup.find('div', {'class': 'vertical-tabs__tabs'})
        try:
            project_links_div = project_links_div.find_next_sibling('div')
            links_list = project_links_div.find_all('li')
            project_links = {}
            for link in links_list:
                link_name = link.text.strip()
                link_a_tag = link.find('a')
                if link_a_tag and 'href' in link_a_tag.attrs:
                    link_url = link_a_tag['href']
                    project_links[link_name] = link_url
        except AttributeError:
            print(url)
            project_links = {}

        # Extract the project description
        description = soup.find('div', {'id': 'description'})
        try:
            description = description.text.strip()
        except AttributeError:
            description = ''

        license_info = ""
        license_pattern = re.compile(r'OSI Approved :: (.*) License')
        for key in project_links.keys():
            match = license_pattern.match(key)
            if match:
                license_info = match.group(1)
                break

        # Add the data to the packages list
        packages.append({
            'name': name,
            'version': version,
            'summary': summary,
            'description': description,
            'license': license_info,
            'project_links': project_links,
        })
        print(f"{i} {line} finished")
    except Exception:
        print(f"{i} {line} failed, skips")


# Save the packages data to a JSON file
with open('packages.json', 'w') as f:
    json.dump(packages, f, indent=4)
