import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://github.com/edoc99?tab=repositories')
soup = BeautifulSoup(page.content, 'html.parser')
repositories = soup.find(id='user-repositories-list')

projects = repositories.find_all(class_='col-10 col-lg-9 d-inline-block')

names = [project.find(itemprop='name codeRepository').get_text().replace("\n", "").replace(" ", "") for project in projects]

description = [project.find(itemprop='description').get_text().replace("\n", "") for project in projects]

programmingLanguage = [project.find(itemprop='programmingLanguage').get_text() for project in projects]
# print(names)
print(description)
# print(programmingLanguage)

gitrepo = pd.DataFrame(
    {
        'Names': names,
        'description': description,
        'ProgrammingLanguage': programmingLanguage,
    }
)

print(gitrepo)

gitrepo.to_csv('gitrepo.csv')