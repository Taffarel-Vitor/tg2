"""TurboGears2 helpers for setting up your application enviroment

The intention of this module is to provie some helpers that setup sane defaults 
for TG2 applications.  The gaoal is to make the config files smaller, simpler and easier to read. 
"""

from pylons import config
from routes import Mapper

def make_default_route_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    
    # This route connects your root controller
    map.connect('*url', controller='root', action='route')
    
    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE
    # map.connect(':controller/:action/:id')
    map.connect('*url', controller='template', action='view')

    return map