!pip install -r ../src/requirements.txt

import logging 
logging.getLogger("py4j.java_gateway").setLevel(logging.ERROR)

from kedro.framework.session import KedroSession
from kedro.extras.extensions.ipython import reload_kedro


from kedro.framework.startup import bootstrap_project
from pathlib import Path

bootstrap_project("/Workspace/Repos/sukanya_patra@mckinsey.com/databricks_iris/")
reload_kedro("../")
with KedroSession.create(project_path='..') as session:
    session.run()