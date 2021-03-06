#
# User defined tasks setup.
# Generated from buildmytask.
#

if sys.path[1] != '/Users/binchen/Dropbox/bc_python/casa_task':
  sys.path.insert(1, '/Users/binchen/Dropbox/bc_python/casa_task')
from odict import odict
if not globals().has_key('mytasks') :
  mytasks = odict()

mytasks['pimfit'] = 'Fit one or more elliptical Gaussian components on an image region(s)'
mytasks['ptclean'] = 'Parallelized clean in consecutive time steps'
mytasks['subvs'] = 'Vector-subtraction in UV using selected time ranges and spectral channels as background'
mytasks['subvs'] = 'Vector-subtraction in UV using selected time ranges and spectral channels as background'
mytasks['subvs'] = 'Vector-subtraction in UV using selected time ranges and spectral channels as background'

if not globals().has_key('task_location') :
  task_location = odict()

task_location['pimfit'] = '/Users/binchen/Dropbox/bc_python/casa_task'
task_location['ptclean'] = '/Users/binchen/Dropbox/bc_python/casa_task'
task_location['subvs'] = '/Users/binchen/Dropbox/bc_python/casa_task'
task_location['subvs'] = '/Users/binchen/Dropbox/bc_python/casa_task'
task_location['subvs'] = '/Users/binchen/Dropbox/bc_python/casa_task'
import inspect
myglobals = sys._getframe(len(inspect.stack())-1).f_globals
tasksum = myglobals['tasksum'] 
for key in mytasks.keys() :
  tasksum[key] = mytasks[key]

from pimfit_cli import  pimfit_cli as pimfit
from ptclean_cli import  ptclean_cli as ptclean
from subvs_cli import  subvs_cli as subvs
from subvs_cli import  subvs_cli as subvs
from subvs_cli import  subvs_cli as subvs
