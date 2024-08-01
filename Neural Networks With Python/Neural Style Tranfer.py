import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt

# Load an image and convert it to tensor
def image_loader(image_path, max_size=512, shape=None):
    image = Image.open(image_path)
    if max_size is not None:
        size = max(max_size, *image.size)
        image = transforms.Resize(size)(image)
    if shape is not None:
        image = transforms.Resize(shape)(image)
    image = transforms.ToTensor()(image).unsqueeze(0)
    return image.to(device)

# Convert tensor to image
def tensor_to_image(tensor):
    image = tensor.cpu().clone().detach().squeeze(0)
    image = transforms.ToPILImage()(image)
    return image

# Define the content and style loss functions
class ContentLoss(nn.Module):
    def __init__(self, target):
        super(ContentLoss, self).__init__()
        self.target = target.detach()

    def forward(self, x):
        loss = nn.functional.mse_loss(x, self.target)
        return loss

class StyleLoss(nn.Module):
    def __init__(self, target):
        super(StyleLoss, self).__init__()
        self.target = self.gram_matrix(target).detach()

    def gram_matrix(self, x):
        b, c, h, w = x.size()
        features = x.view(c, h * w)
        G = torch.mm(features, features.t())
        return G.div(c * h * w)

    def forward(self, x):
        G = self.gram_matrix(x)
        loss = nn.functional.mse_loss(G, self.target)
        return loss

# Define a function to load the VGG model
def get_model():
    vgg = models.vgg19(pretrained=True).features.eval()
    return vgg.to(device)

# Define the neural style transfer function
def run_style_transfer(cnn, normalization_mean, normalization_std,
                       content_img, style_img, input_img, num_steps=500,
                       style_weight=1000000, content_weight=1):
    
    # Define the model and the losses
    model = nn.Sequential().to(device)
    model.add_module("normalization", nn.Identity())
    
    content_loss = ContentLoss(get_features(content_img, cnn, normalization_mean, normalization_std))
    model.add_module("content_loss", content_loss)
    
    style_losses = []
    style_features = get_features(style_img, cnn, normalization_mean, normalization_std)
    for sf in style_features:
        style_loss = StyleLoss(sf)
        style_losses.append(style_loss)
        model.add_module(f"style_loss_{len(style_losses)}", style_loss)
    
    # Set the input image as a parameter
    input_img = torch.nn.Parameter(input_img.data)
    
    optimizer = optim.LBFGS([input_img])

    # Optimization loop
    for i in range(num_steps):
        def closure():
            input_img.data.clamp_(0, 1)
            optimizer.zero_grad()
            model(input_img)
            loss = 0
            loss += content_weight * content_loss(input_img)
            for sl in style_losses:
                loss += style_weight * sl(input_img)
            loss.backward()
            if i % 50 == 0:
                print(f"Step {i}, Loss: {loss.item()}")
            return loss
        
        optimizer.step(closure)
    
    input_img.data.clamp_(0, 1)
    return input_img

# Get features from the VGG model
def get_features(image, model, normalization_mean, normalization_std):
    layers = {
        '0': 'conv1_1',
        '5': 'conv2_1',
        '10': 'conv3_1',
        '19': 'conv4_1',
        '21': 'conv4_2',
        '28': 'conv5_1',
    }
    
    x = image.clone()
    features = []
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features.append(x)
    
    return features

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load images
content_img = image_loader("path_to_your_content_image.jpg", shape=(256, 256))
style_img = image_loader("path_to_your_style_image.jpg", shape=(256, 256))
input_img = content_img.clone()

# Define normalization parameters
normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

# Get model
cnn = get_model()

# Perform style transfer
output = run_style_transfer(cnn, normalization_mean, normalization_std, content_img, style_img, input_img)

# Display result
plt.imshow(tensor_to_image(output))
plt.show()
