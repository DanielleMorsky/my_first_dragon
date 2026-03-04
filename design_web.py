import html


def full_html(specific_site_content):
    html_base_content = f"""
        <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            {specific_site_content}
        </body>
        </html>
        """
    return html_base_content


def home_screen():
    text = """
    <h2 style='text-align:center'>Welcome to animal viewing :)</h2>
    <br>
    <h3 style='text-align:center'>press here to get to status page</h3>
    """
    # <a href="url">link text</a>
    return full_html(text)
