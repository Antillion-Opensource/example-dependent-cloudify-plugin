import os

from cloudify import ctx
from cloudify.decorators import operation

@operation
def log_message(message, **kwargs):
    ctx.logger.info('Message: {}'.format(message))
