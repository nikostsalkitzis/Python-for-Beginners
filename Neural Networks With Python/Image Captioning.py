import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the image
def load_image(image_path, transform):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension
    return image

# Define a CNN encoder using ResNet
class CNNEncoder(nn.Module):
    def __init__(self):
        super(CNNEncoder, self).__init__()
        resnet = models.resnet50(pretrained=True)
        self.resnet = nn.Sequential(*list(resnet.children())[:-2])  # Remove the classification layer

    def forward(self, images):
        features = self.resnet(images)
        return features

# Define an RNN decoder
class RNNDecoder(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_layers):
        super(RNNDecoder, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.rnn = nn.LSTM(embed_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, features, captions):
        embeddings = self.embedding(captions)
        inputs = torch.cat((features.unsqueeze(1), embeddings), dim=1)
        outputs, _ = self.rnn(inputs)
        outputs = self.fc(outputs)
        return outputs

# Example transform for image preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Define parameters
vocab_size = 10000  # Example vocabulary size
embed_size = 256
hidden_size = 512
num_layers = 1
max_caption_length = 20

# Initialize models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
encoder = CNNEncoder().to(device)
decoder = RNNDecoder(vocab_size, embed_size, hidden_size, num_layers).to(device)

# Dummy input
image_path = 'path_to_your_image.jpg'
image = load_image(image_path, transform).to(device)
caption_input = torch.zeros((1, max_caption_length), dtype=torch.long).to(device)  # Dummy caption input

# Forward pass through encoder and decoder
features = encoder(image).view(-1, 2048)  # Flatten feature map
caption_output = decoder(features, caption_input)

print("Caption Output Shape:", caption_output.shape)
