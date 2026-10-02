# EZC Image Recognition Training Pipeline

The EZC backend now stores verified product-image samples and training-job metadata. This is the production contract for image recognition: product -> labeled images -> dataset version -> training job -> model version -> inference on device/server.

This archive deliberately does **not** pretend that a model has been trained. A real model needs a representative image dataset for each merchant/product and a selected model/runtime (for example TensorFlow Lite or ONNX). The API is ready to collect the dataset and track training jobs.

Recommended next production step: collect at least 20-50 varied, well-lit images per product, split train/validation/test, train an object/classification model, export a mobile runtime model, then add confidence thresholds and human confirmation before changing a cart.
