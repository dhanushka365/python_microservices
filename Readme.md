#create a virtual enviroment
-[python -m venv  python_microservices-env]

#activate the created virtual enviroment
-[python_microservices-env\Scripts\activate.bat]

#see all the dependencies inside this virtual enviroment
-[pip list]

#install Flask
-[pip install Flask]

#create the requirements.txt file
-[pip freeze > requirements.txt]

#install the requirements from txt file
-[python -m pip install -r requirements.txt]

#start minikube cluster
-[strat minikube]
