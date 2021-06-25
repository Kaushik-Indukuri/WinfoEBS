import click
import pyjab


@click.command()
def ebs():
    jabdriver = JABDriver("")
    login_btn = jabdriver.find_element_by_name("Login")
    login_btn.click()
    click.echo('task finished')

