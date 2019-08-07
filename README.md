# forageConversionTool
Range branch tool for processing forage clipping data - standardizing species names and reformatting for analysis


	# install:

		# if you don't already, install python 3:
		brew install python


		# check the version, we are hoping for 3.6/3.7:
		python --version


		# clone the repo, then navagate into it (cd forageConversionTool):
		git clone https://github.com/bcgov/forageConversionTool.git && cd forageConversionTool
		

		# make a virtualenv to store packages related to the project and activate it in your shell:
		python3 -m venv env && source env/bin/activate
		
		
		# install the requisite packages for the project, if you are new to python note that you do this every time you start a shell and work on the project
		pip install -r requirements.txt 


		# if you're lucky you can just run paste this line and it will all work:
		git clone https://github.com/bcgov/forageConversionTool.git && cd forageConversionTool && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt 




	# running tests:

		pytest tests.py


	# running the tool:

		python forageConversionTool.py
