import ast
f1 = open("codeex1.txt", "r")
code1 = f1.read()
print(type(code1))
code = """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age_change(self):
        if self.age > 20:
            return self.age + 5
        else:
            return self.age

    def send_messages(self, messages):
        for message in messages:
            print(message)
"""
code = """
import logging
from typing import Optional

from sentry.auth import access
from sentry.models.group import Group
from sentry.services.hybrid_cloud.user.model import RpcUser
from sentry.services.hybrid_cloud.user.service import user_service
from sentry.silo import SiloMode
from sentry.tasks.base import instrumented_task
from sentry.utils.email import send_messages

logger = logging.getLogger(__name__)


def _get_user_from_email(group: Group, email: str) -> Optional[RpcUser]:
    for user in user_service.get_many_by_email(emails=[email]):
        # Make sure that the user actually has access to this project
        context = access.from_user(user=user, organization=group.organization)
        if not any(context.has_team_access(t) for t in group.project.teams.all()):
            logger.warning("User %r does not have access to group %r", user, group)
            continue

        return user
    return None


@instrumented_task(
    name="sentry.tasks.email.process_inbound_email",
    queue="email",
    default_retry_delay=60 * 5,
    max_retries=None,
    silo_mode=SiloMode.REGION,
)
def process_inbound_email(mailfrom: str, group_id: int, payload: str):
    # TODO(hybridcloud) Once we aren't invoking this with celery
    # detach  this from celery and have a basic function instead.
    from sentry.models.group import Group
    from sentry.web.forms import NewNoteForm

    try:
        group = Group.objects.select_related("project").get(pk=group_id)
    except Group.DoesNotExist:
        logger.warning("Group does not exist: %d", group_id)
        return

    user = _get_user_from_email(group, mailfrom)
    if user is None:
        logger.warning("Inbound email from unknown address: %s", mailfrom)
        return

    form = NewNoteForm({"text": payload})
    if form.is_valid():
        form.save(group, user)


@instrumented_task(
    name="sentry.tasks.email.send_email",
    queue="email",
    default_retry_delay=60 * 5,
    max_retries=None,
)
def send_email(message):
    # HACK(django18) Django 1.8 assumes that message objects have a reply_to attribute
    # When a message is enqueued by django 1.6 we need to patch that property on
    # so that the message can be converted to a stdlib one.
    #
    # See
    # https://github.com/django/django/blob/c686dd8e6bb3817bcf04b8f13c025b4d3c3dc6dc/django/core/mail/message.py#L273-L274
    if not hasattr(message, "reply_to"):
        message.reply_to = []

    send_messages([message])
"""
# tree = ast.parse(code)

# for node in ast.walk(tree):
#     if isinstance(node, ast.FunctionDef) and node.name == "send_email":
#         print(ast.get_source_segment(code, node))


tree = ast.parse(code)
target_name = "send_email"

for node in ast.walk(tree):
    if (
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and
        (node.name == target_name or
         (isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == target_name) or
         (isinstance(node, ast.Attribute) and hasattr(node.value, 'id') and node.value.id == target_name)
        )
    ):
        print(ast.get_source_segment(code, node))
