import requests
from bs4 import BeautifulSoup
import pyperclip
import webbrowser

def scrape_dictionary(keyword):
    url = f'https://de.thefreedictionary.com/{keyword}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant section on the page
    definition_section = soup.find("section", attrs={"data-src": "farlex_partner_3"})

    return definition_section

def generate_html(keyword):
    definition_section = scrape_dictionary(keyword)

    if definition_section:
        definition_html = definition_section.prettify()
    else:
        definition_html = '<p>Definition not found</p>'

    css_styles = '''
    <style>
    body {
        width: 450px;
        margin: 0 auto;
    }

    .illustration {
        font-style: italic;
        color: rgb(221, 148, 52);
    }

    .runseg {
        padding: 15px 0;
        border-bottom: 1px solid grey;
    }
    </style>
    '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dictionary Result</title>
        {css_styles}
    </head>
    <body>
        <h1>{keyword}</h1>
        {definition_html}
    </body>
    </html>
    '''


def main():
    keyword = pyperclip.paste()
    html_page = generate_html(keyword)

    # Writing the generated HTML page to a file
    with open('result.html', 'w', encoding="utf-8") as file:
        file.write(html_page)

    # Open the HTML page in the default web browser
    webbrowser.open('result.html')

if __name__ == '__main__':
    main()
