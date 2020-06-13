import os 
from core import action_hub, app
from api_types import ActionList

import logging
logger = logging.getLogger(__name__)
logger.info('Custom Action Hub started')

fast_hub_info = {
    'info': 'The following applications have been installed. Note that these are not used directly via this webpage. Actions are accessed via the Looker Action Hub.',
    'actions': [],
}

actions_list = []
available_actions = [module[:-3] for module in os.listdir('actions') if module[-3:] == '.py']
for action in available_actions:
    logger.info(f'Importing Action: {action}')
    definition = __import__('.'.join(['actions', action]), globals(), locals(), ['definition']).definition
    actions_list.append(definition)
    fast_hub_info['actions'].append(action)

@app.get('/')
def root():
    """Simple homepage with JSON response only."""
    return fast_hub_info

@app.post('/')
def list_actions():
    """Returns an ActionList with all actions available from this ActionHub"""

    return ActionList(integrations=actions_list)
