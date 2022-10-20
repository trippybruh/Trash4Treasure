# Trash4Treasure About #

Free forniture user friendly exchange platform, optimized for web and mobile device use. This project aims to reduce waste and trash produciton in favor of a more circular kind of economy, where goods are not thrown away but instead picked up for free by someone who maybe interested in them. 

It takes time and effort to dispose of an old couch or wardrobe trough conventional ways, and at the same time there are people looking exactly for what you are trying to waste, wouldn't it be easier if the two of you can share a common place where to find each other and resolve your mutual problem?

# Trash4Treasure Developers Guide #
The app is being developed as a Django project, which is a Python framework optimized to build and deploy any web service.

therefore you need it to run this code: https://www.python.org/downloads/

Remember to check the "add python to PATH" box during python installation setup!

Once installed you may proceed to open your pc command prompt, type there "python --version" to verify python file path has been added to the "PATH" enviroment variable of your device. 

If that s not the case take a look here: https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows

Proceed by installing python "virtualenv" library which will help isolate this project simulating cloud computing conditions where it should run, you can do that typing "pip install virtualenv". Now navigate in the command prompt with "cd C:/filepath/..." to the folder where you want this virtual enviroment to be created and once inside type "python -m venv T4Tproject (or any name you wish)".

This will create another instance of python softwares completely separeted from your pc installed python softwares, to activate this virtual shell, navigate with the command prompt inside the "Scripts" folder and simply type "activate.bat".

Now if your prompt look like "(T4Tproject) C:/filepath/.../T4Tproject", run "python -m pip install django".

Now you are ready to use "T4T" folder on this repository, just copy it in the "Scripts" folder inside your virtual enviroment. At this point to test the code move the command prompt inside the copied "T4T" folder and run the following command "python manage.py runserver".

Then open on your browser the provided link to navigate T4T webpages.


