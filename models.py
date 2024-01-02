from sklearn.metrics import f1_score
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from tqdm import tqdm 

# Define your custom Model    
class yourModelName(nn.Module):
    

# Set the torch train & test
# torch train
def train_torch():
    def custom_train_torch(model, train_loader, epochs, cfg):
        """
        Train the network on the training set.
        Model must be the return value.
        """
        print("Starting training...")
            
        return model
    
    return custom_train_torch

# torch test
def test_torch():
    
    def custom_test_torch(model, test_loader, cfg):
        """
        Validate the network on the entire test set.
        Loss, accuracy values, and dictionary-type metrics variables are fixed as return values.
        """
        print("Starting evalutation...")
        
        
        
        # if you use metrics, you set metrics
        # type is dict
        # for example, Calculate F1 score
        # Add F1 score to metrics
        # metrics = {"f1_score": f1}
        
        # If you don't use it
        metrics=None    
        
        model.to("cpu")  # move model back to CPU
        return average_loss, accuracy, metrics
    
    return custom_test_torch
