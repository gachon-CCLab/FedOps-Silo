# FedOps Custom Silo Setting

This guide provides step-by-step instructions on executing FedOps Silo, a Federated Learning Lifecycle Management Operations framework.

## Baseline
 
```shell
- Baseline
   - client_main.py
   - client_manager_main.py
   - server_main.py
   - models.py
   - data_preparation.py
   - requirementst.txt (server requirement)
   - conf
      -  config.yaml
```

## Steps

1. ***Start by fork the FedOps-Silo.***

2. ***Customize the FedOps example code.***
   - In accordance with the baseline form, write the code with reference to the example and store it in the your own git remote storage.


   - Data & Model:
      - Prepare your data in `data_preparation.py` and define your model in `models.py`.
      - Enter your data and model in `conf/config.yaml`

   - Client:
     - Configure settings in `conf/config.yaml` for task ID, data, and WandB information.
     - Implement data_preparation.py for data handling.
     - Build `models.py` for local model specifications.
     - Register data and model, and run the client using `client_main.py`.

   - Server:
     - Configure settings in `conf/config.yaml` for FL/Aggregation hyperparameters and data information.
     - Implement `models.py` to initialize the global model.
     - Register data (for evaluating the global model) and initialize the global model in `server_main.py`.
     <br></br>

3. ***Create FL task on FedOps web interface.***
   - Use the FedOps web interface to create your FL task. 
   - Specify the Git repository address for your FL server code.
   - Refer [FedOps Silo Guide](https://gachon-cclab.github.io/docs/user-guide/silo-guide/)
   <br></br>


4. ***Run the clients.***
   - Run `client_main.py` and `client_manager_main.py`
   - Or choose either [Docker or shell(localhost)](https://github.com/gachon-CCLab/FedOps/tree/main/silo/examples/torch/docker-mnist) to run the clients.
   <br></br>

5. ***Initiate the FL task.***
   - Select the desired clients on the FedOps web interface and initiate the FL task by clicking the "FL start" button.
   <br></br>

6. ***Monitor and manage the FL task***
   - Monitor the performance of local and global models, 
   and manage/download the global model as the FL task administrator through the FedOps web interface.
   <br></br>

7. ***Monitor data and local model performance*** 
   - Monitor the health of data and local model performance as the device administrator through the designated WandB.
   <br></br>

## Support
***For any questions or issues, please contact the FedOps support team at gyom1204@gachon.ac.kr***
