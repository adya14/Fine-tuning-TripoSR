import os
import torch
from torch.utils.data import Dataset, DataLoader

class TensorDataset(Dataset):
    def __init__(self, vertices_dir, faces_dir):
        self.vertices_files = sorted([f for f in os.listdir(vertices_dir) if f.endswith('_vertices.pt')])
        self.faces_dir = faces_dir
        self.vertices_dir = vertices_dir

    def __len__(self):
        return len(self.vertices_files)

    def __getitem__(self, idx):
        vertices_path = os.path.join(self.vertices_dir, self.vertices_files[idx])
        faces_path = os.path.join(self.faces_dir, self.vertices_files[idx].replace('_vertices', '_faces'))
        
        vertices = torch.load(vertices_path)
        faces = torch.load(faces_path)
        
        return vertices, faces

# Directories containing your tensor files
train_vertices_dir = 'path/to/train/vertices'
train_faces_dir = 'path/to/train/faces'

val_vertices_dir = 'path/to/val/vertices'
val_faces_dir = 'path/to/val/faces'

test_vertices_dir = 'path/to/test/vertices'
test_faces_dir = 'path/to/test/faces'

# Create dataset instances
train_dataset = TensorDataset(train_vertices_dir, train_faces_dir)
val_dataset = TensorDataset(val_vertices_dir, val_faces_dir)
test_dataset = TensorDataset(test_vertices_dir, test_faces_dir)

# Create DataLoader instances
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
