# Serverless Image Resizer

A cloud-based image upload and auto-resize application built using AWS and GitHub Actions CI/CD.

## Live Demo
http://axshlin-image-resizer-site-08.s3-website-us-east-1.amazonaws.com

## Features
- Upload images from a web interface
- Store original images in Amazon S3
- Automatically resize images using AWS Lambda
- Save resized images in a separate S3 folder
- Serverless architecture
- Frontend auto deployment with GitHub Actions CI/CD

## Tech Stack
- HTML
- CSS
- JavaScript
- Python
- AWS S3
- AWS Lambda
- API Gateway
- IAM
- GitHub Actions

## Project Structure
image-resizer-project/
├── frontend/
│   └── index.html
├── lambda-upload/
│   └── lambda_function.py
├── lambda-resize/
│   └── lambda_function.py
├── .github/
│   └── workflows/
│       └── deploy.yml
├── README.md
└── .gitignore

## How It Works
1. User uploads image from frontend.
2. API Gateway sends request to Lambda upload function.
3. Image is stored in S3 bucket under original/.
4. S3 trigger invokes resize Lambda.
5. Image is resized using Pillow.
6. Resized image is stored in resized/.

## CI/CD Pipeline
- GitHub Actions detects push to main branch
- Automatically syncs frontend files to Amazon S3
- Live website updates without manual deployment

## Author
Axshlin Sharmil S