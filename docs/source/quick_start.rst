Quick Start
============

The `quick_start.py` script is a simple way to start using STRATA AGENT. Here's a breakdown of what the script does and how to run it:

1. **Importing Modules:**

   The script begins by importing necessary modules from the `strata` package:

   .. code-block:: python

       from strata import StrataAgent
       from strata import ToolManager
       from strata import StrataExecutor, StrataPlanner, StrataRetriever
       from strata.utils import setup_config, setup_pre_run

2. **Setting Up Configuration:**

   Next, the script sets up the configuration for running a task:

   .. code-block:: python

       args = setup_config()
       args.query = "Create a new folder named 'test_strata'"

   This sets a query for the STRATA AGENT to execute, which in this case is creating a new folder named 'test_strata'.

3. **Preparing and Running the Task:**

   After configuring the task, the script prepares it for execution and runs it:

   .. code-block:: python

       task = setup_pre_run(args)
       agent = StrataAgent(StrataPlanner, StrataRetriever, StrataExecutor, ToolManager, config=args)
       agent.run(task)

   This initializes the STRATA AGENT with specified planners, retrievers, and executors, then executes the task.

Running the Script
------------------

To run the `quick_start.py` script, simply execute the following command in your terminal:

.. code-block:: bash

    python quick_start.py

Ensure that you are in the same directory as the `quick_start.py` file or provide the full path to the file.

Congratulations! You have now successfully run a task with STRATA~