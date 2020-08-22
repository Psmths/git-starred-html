import requests
from requests.exceptions import HTTPError
import json
from tabulate import tabulate

# Function to get the raw JSON response from github API
def get_json_content(username):
    url = 'https://api.github.com/users/' + username + '/starred'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return response.json()

# Extracts user-specified fields and returns as a list of dicts, per repo
# fields will eventually become columns with rows being starred repos
def extract_fields(json_response, fields):
    starred_list = []
    for repo in json_response:
        repo_dict = {}
        for field in fields:
            repo_dict[field] = repo[field]

        starred_list.append(repo_dict)
    return starred_list

# Use tabulate to generate an HTML list
def gen_html_table(attribute_list):
    return(tabulate(attribute_list, headers="keys", tablefmt='html'))


def main():
    username = 'username'
    fields = ['name', 'description', 'html_url']
    json_resp = get_json_content(username)
    print(gen_html_table(extract_fields(json_resp, fields)))


if __name__ == "__main__":
    main()
