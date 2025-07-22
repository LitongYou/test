from strata import StrataAgent
from strata import ToolManager
from strata import StrataExecutor, StrataPlanner, StrataRetriever
from strata.utils import setup_config, setup_pre_run

args = setup_config()
if not args.query:
    args.query = "Copy any text file located in the working_dir/document directory that contains the word 'agent' to a new folder named 'agents' "
task = setup_pre_run(args)
agent = StrataAgent(StrataPlanner, StrataRetriever, StrataExecutor, ToolManager, config=args)
agent.run(task=task)
