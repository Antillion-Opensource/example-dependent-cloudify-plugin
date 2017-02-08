import os

from cloudify import ctx
from cloudify.decorators import operation

from ant_dummy import noop as dummy_noop # __DEPDENDENCY__ from dummy-cloudify-plugin

@operation
def log_message(message, **kwargs):
   dummy_noop.log_message('Message _from_ ANT DEPENDS: {}'.format(message))
   ctx.logger.info('ANT DEPENDS message: {}'.format(message))
