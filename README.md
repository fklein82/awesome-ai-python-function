# Image Classification Python Accelerator for Tanzu
This repository contains a Python accelerator for Tanzu that enables you to deploy a serverless image classification function as a TAP (Tanzu Application Platform) workload. The accelerator leverages the buildpacks provided by VMware's open-source Function Buildpacks for Knative project.

## Overview
The accelerator includes a Python script for image classification that uses the MobileNetV2 model and MLflow. It allows you to download an image from the internet, predict its contents, log the prediction and image in MLflow, and display the image with the prediction confidence. This serverless function can be easily integrated into your application or workflow.

## Getting Started
To get started with this accelerator, follow these steps:

Clone this repository to your local development environment:

```bash

git clone <repository-url>
cd python-accelerator-for-tanzu
``````
Inside the python-function directory, you will find the func.py file. This Python function is invoked by default and serves as the entry point for your serverless image classification logic.

```bash
python-function
    └── func.py // EDIT THIS FILE
```
You can customize the code inside this file to implement your specific image classification logic.

If you want to explore more code samples for serverless functions that can be deployed within Tanzu Application Platform, you can check out the samples folder.

## Deployment
For detailed instructions on how to build, deploy, and test your customized serverless image classification function using Tanzu Application Platform, please refer to the DEPLOYING.md file provided in this repository.

## Image Classification Function
The core functionality of this accelerator is the image classification function, which performs the following steps:

- Downloads an image from a specified URL.
- Predicts the content of the image using the MobileNetV2 model.
- Logs the prediction and image in MLflow for tracking.
- Displays the image with the prediction confidence.

This function can be integrated into various applications and workflows that require image analysis and classification.

## Deploying on VMware Tanzu Application Platform
To deploy this application on VMware Tanzu Application Platform, follow these steps:

Ensure you have the Tanzu CLI installed and configured with access to your Tanzu Application Platform instance.

Navigate to your project directory:

```bash
cd [your-repo-directory]
``````
Use the Tanzu CLI to deploy your application:

```bash
tanzu apps workload create -f config/workload.yaml
```

## Monitor the deployment status:

```bash
tanzu apps workload tail ai-video-recognition --timestamp --since 1h
```
Once deployed, access your application via the URL provided by Tanzu Application Platform. You can find the URL with the following command:

```bash
tanzu apps workload get ai-video-recognition
```

## Customization
This accelerator provides a foundation for deploying Python-based serverless functions within Tanzu Application Platform. You can customize it to suit your specific use cases and requirements. Whether you need to classify images, process data, or perform other tasks, this accelerator can serve as a starting point for building and deploying serverless functions on the platform.

## How to Contribute
Contributions to improve or enhance this AI python Accelerator are welcome. Feel free to open issues or submit pull requests with your suggestions or improvements.

## Please Note
The software is provided "as is", without warranties of any kind. As the creator, I am not liable for any claims, damages, or other liabilities that arise from the use of the work.
