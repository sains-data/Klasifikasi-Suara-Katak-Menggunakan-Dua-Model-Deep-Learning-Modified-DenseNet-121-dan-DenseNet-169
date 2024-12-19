import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision

class ModifiedDenseNet169(nn.Module):
    def __init__(self, num_classes, dropout_prob=0.5):
        super(ModifiedDenseNet169, self).__init__()
        self.densenet169 = torchvision.models.densenet169(pretrained=True)  # Mengganti DenseNet-121 dengan DenseNet-169
        self.features = self.densenet169.features
        self.batch_norm1 = nn.BatchNorm2d(1664)  # Batch normalization setelah feature extraction (output dari DenseNet-169 adalah 1664)
        self.dropout1 = nn.Dropout(p=dropout_prob)  # Dropout tambahan setelah batch normalization
        self.dropout2 = nn.Dropout(p=dropout_prob)  # Dropout tambahan sebelum classifier
        self.classifier = nn.Linear(self.densenet169.classifier.in_features, num_classes)

    def forward(self, x):
        # Feature extraction
        x = self.features(x)
        # Batch normalization setelah feature extraction
        x = self.batch_norm1(x)
        # Aktivasikan ReLU
        x = F.relu(x, inplace=True)
        # Menambahkan adaptive pooling dan flatten
        x = F.adaptive_avg_pool2d(x, (1, 1)).view(x.size(0), -1)  # Flatten features
        # Dropout tambahan
        x = self.dropout1(x)  # Apply first Dropout
        # Classifier layer
        x = self.classifier(x)
        # Dropout sebelum klasifikasi akhir
        x = self.dropout2(x)  # Apply second Dropout

        return x
