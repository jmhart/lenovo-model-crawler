from Models import Models
from api import get_model_name

models = Models()
model_ids = models.model_ids

model_names = []
for model_id in model_ids:
    model_names.append((model_id, get_model_name(model_id)))

models.write_model_names(model_names)
