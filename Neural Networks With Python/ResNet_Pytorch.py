#In order to use the following code you should install Pytorch with the following command:
#pip install torch torchvision
#For data preparation you need to split your dataset in the below pattern:
#dataset/
#   train/
#       fire/
#       not_fire/
#   val/
#       fire/
#       not_fire/
#Each subdirectory needs to contain the images with fire and not_fire.
'''
We are going to use the torchvision to load and transform the images. We can augment the images in order to let the model
generalize better and enchance its performance.
'''
import torch
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torchvision.models as models
import torch.nn as nn
#Define the tranformations for the training and validation sets
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0,456, 0,406], [0.229, 0.224, 0.225])
    ])
#Loading the datasets from ImageFolder
train_dataset = datasets.ImageFolder(root='dataset/train', transform = transform)
valid_dataset = datasets.ImageFolder(root='dataset/val', transform = transform)
#Creation of the data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False)#batch size to be tuned if needed
#Loading the pretrained ResNet model
model = models.resnet18(pretrained=True)
#Since the problem is binary classification we replace ResNet's final fully connected layer
num_features = model.fc.in_features
model.fc = nn.Linear(num_features = 2)#two classes fire and not_fire
#For better performance we need to use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
#define the metric of performance
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)#learning rate to be tuned if needed
#Training
epochs = 20
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    for inputs, labels in train_loader:
        inputs,labels = inputs.to(device), labels.to(device)
        #We set the parameter gradients to 0
        optimizer.zero_grad()
        #Forward pass of the information
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        #Backword Propagation and optimization of the parameters
        loss.backward()
        optimizer.step()
        #Tracking of loss and accuracy
        running_loss += loss.item() * imputs.size(0)
        _, predicted = torch.max(output,1)
        total += labels.size(0)
        correct += (predicted==labels).sum().item()
        epoch_loss = running_loss/len(train_loader.dataset)
        epoch_accuracy = correct/total
        print(f"Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_accuracy:.4f}")
#Validation dataset
model.eval()
val_loss = 0.0
val_correct = 0
val_total = 0
with torch.no_grad():
    for inputs, labels in val_loader:
            inputs,labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs,labels)
            val_loss += labels.size(0)
            val_correct += (predicted == labels).sum().item()
            val_epoch_loss = val_loss / len(val_loader.dataset)
            val_epoch_accuracy = val_correct / val_total
            print(f"Epoch {epoch+1}/{epochs}, Validation Loss: {val_epoch_loss:.4f}, Accuracy: {val_epoch_accuracy:.4f}"))
#After the training save the model
torch.save(model.state.dict(), 'resnet_fire_classifier.pth')

