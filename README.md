# Keeggo Challenge Project

This is the thecnical challenge for join Keeggo company as Dev.

**NOTE 1:** some print in some methods are just to see the execution flow because of we are in homolog environment. in the production, they will be removed .

**NOTE 2:** For testing this app, make some changes.
Go to file 'stark_bank_sdk.py' and set:

     SLEEP_HOURS = 1 (means 1 minutes)
     if round == 3: (...)

**NOTE 3:**

     THERE ARE TWO STRATEGIES TO GET AND VALIDATE A CPF FOR EACH INVOICE IN THIS APP.
     NOTE 3.1: YOU NEED TO CHOICE ONE OF THEM TO USE ON SCRIPT -> starkbank_module.py and stark_banck_sdk.py .


     STRATEGY 1: Make request to API (gerador braleiro) once and generate CPFs and store them in a file. For this point, the method create_invoices read that file, bring all CPFs and make a random choice for each invoice, then make validation of it. This is the BEST one considering the running time.
          - STEP 1: call method 'gerador_braleiro_api_tofile' belong to this class in 'stark_bank_sdk.py' file. This one will genarate 100 of CPFs and store them in a file called 'CPF_file.text' in utils folder. This action is perfomed only once
          - STEP 2: In the method create_invoices call 'self.random_cpf()'. Uncomment that line
          - STEP 3: read the 'NOTE 3.2' below

          ---------------------------------------------------------------------
          NOTE 3.2: UNCOMMENT THOSE 3 INSTRUCTIONS BELOW TO APPLY STRATEGY 1
                    to genarate and valid CPF.
          ---------------------------------------------------------------------

          payer_cpf_index = randint(0, len(cpf_list) - 1)  # UNCOMMENT THIS
          payer_cpf = cpf_list.pop(payer_cpf_index)        # UNCOMMENT THIS
          if not self.validate_invoice(payer_cpf):         # UNCOMMENT THIS
               continue


     STRATEGY 2: For each invoice make a resquest to API and bring one cpf, then make validation on it .

     # payer_cpf = self.gerador_braleiro_api('cpf')        # UNCOMMENT THIS FOR STRATEGY 2
     # if not self.validate_invoice(payer_cpf):            # UNCOMMENT THIS FOR STRATEGY 2
     #     continue

### ABOUT TESTS

I made tests to measure these two strategies.

**TESTS INFO:**

  - ROUND: 3 ( FOR BOTH STRATEGIES )
  - INVOICES: 5
  - TOTAL TIME (STRATEGY 1) : 260.651
  - TOTAL TIME (STRATEGY 2) : 271.616
  - MEAN TIME (STRATEGY 1) : 86.88
  - MEAN TIME (STRATEGY 2) : 90.54
  - DIFFERENCE TIME: 3.65

**Basing on that result, we can  conclude that the STRATEGY 1 is the BEST ONE.**

## STEPS TO RUN THIS APP LOCALY

### 0 | Clone the remote repository to start testing

     git clone https://github.com/idelfrides/keego_challenge

### 1 | Create your virtualenv like

     virtualenv [your_venv_name]

### 2 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish

### 3 | Install requirements

     pip install -r requirements.txt

### 4 | Now you can run the application

     python start_game_module.py
