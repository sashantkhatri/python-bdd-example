This is the example of bdd with allure report. We have focused on Allure reporting part in this example using behave framework using python.


1. Install virtualenv package to create virtualenv
    
    python3 -m pip install virtualenv

2. Create virtual environment 

    python3 -m virtualenv behave-env

3. Activate virtual env

    source behave-env/bin/activate

4. Install all the requirements

    pip install -r requirements.txt

5. Run behave test

   behave -f allure_behave.formatter:AllureFormatter -o Testresult ./features/
 
6. Generate Allure report

    allure generate Testresult/ -o Testreport/ --clean

7. Open allure report
    
    allure open Testreport
