# 11 Transfer Learning(迁移学习)

- Motivation(动机)
  - Exploit(利用) a model trained on one task for a related task
  - Popular in deep learning as DNNs are data hungry and training cost is high
- Approaches 
  - Feature extraction (e.g. Word2Vec, ResNet-50 feature, I3D feature)
  - Train a model on a related task and reuse it
  - Fine-tuning from a pertained model (focus of this lecture)
- Related to
  - Semi-supervised learning
  - In the extreme(极端), zero-shot / few-shot learning
  - Multi-task learning, where some labeled data is available for each task