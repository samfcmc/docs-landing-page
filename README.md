# docs-landing-page

## Requirements
* python >= 2.7
* pip
* virtualenv

## Get it running
* Clone this rep
```
git clone git@github.com:samfcmc/docs-landing-page.git
```
* Navigate to the project's directory
```
cd docs-landing-page
```
* Create a new virtual environment
```
virtualenv env
```
* Activate the virtual environment that we just created
```
source env/bin/activate
```
* Install all the needed requirements
```
cd docs_landing_page
```
```
pip install -r requirements.txt
```
* Create a fenixedu.ini file
```
cp fenixedu.ini-sample fenixedu.ini
```
* Create a new external application using your FenixEdu instance
```
Login in Fenix -> Personal -> Manage Applications -> Create -> Fill all the needed data -> Create
```
* Edit fenixedu.ini file according to the application created in the previous step
* Edit <code> docs_landing_page/settings.py </code> file according to your needs (specially the database)
* Sync the database
```
python manage.py syncdb
```
* Run the application
```
python manage.py runserver
```
* Open your browser in http://localhost:8000/docs
