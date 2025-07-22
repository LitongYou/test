from strata import StrataAgent, StrataExecutor, StrataPlanner, StrataRetriever, SelfLearner, SelfLearning, ToolManager, TextExtractor
from strata.utils import setup_config


args = setup_config()
software_name = args.software_name
package_name = args.package_name
demo_file_path = args.demo_file_path

strata_agent = StrataAgent(StrataPlanner, StrataRetriever, StrataExecutor, ToolManager, config=args)
self_learning = SelfLearning(strata_agent, SelfLearner, ToolManager, args, TextExtractor)

# Only one stage of course study
# self_learning.self_learning(software_name, package_name, demo_file_path)

# contiunous learning
self_learning.continuous_learning(software_name, package_name, demo_file_path)
