from django import template

register = template.Library()


@register.simple_tag
def get_user_task_count(office, user):
    return office.get_open_user_tasks_count(user)