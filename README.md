# 🚀 Bedrock-AI-Agent: End-to-End Retrieval-Augmented Generation (RAG) System using AWS Bedrock and Streamlit

![AI](https://img.shields.io/badge/AI-Bedrock%20%7C%20Streamlit%20%7C%20RAG-blueviolet) ![License](https://img.shields.io/badge/License-MIT-green)

**Author:** **Abhishek**  
📧 **Email:** [vvabhi2776@gmail.com](mailto:vvabhi2776@gmail.com)

---

## 📌 Project Overview
Welcome to **Bedrock-AI-Agent**, a state-of-the-art Retrieval-Augmented Generation (RAG) application meticulously built using Amazon's revolutionary **AWS Bedrock** models. This application allows seamless and intelligent querying of your personal or professional documents, delivering precise, context-rich answers.

Built specifically for professionals, AI enthusiasts, and developers, this project offers:

- **Advanced document retrieval and intelligent text generation**
- **Integration with Amazon Bedrock (Titan Embeddings & Titan Text Models)**
- **Interactive and professional frontend powered by Streamlit**
- **Highly modular, scalable, and production-ready architecture**

---

## 🎯 Why This Project?
This repository showcases the entire AI workflow from data ingestion, embedding creation, intelligent retrieval, and dynamic generation of high-quality answers using AWS Bedrock services. Perfect for AI practitioners and industry professionals to learn, build, and showcase a complete AI pipeline.

---

## 🌟 Key Features
- ✅ **AWS Bedrock Integration**: Leverages Titan Embeddings & Titan Text Lite models.
- ✅ **FAISS Vector Store**: For lightning-fast similarity searches.
- ✅ **Robust Document Handling**: Intelligent parsing and text splitting.
- ✅ **Streamlit Web Application**: User-friendly interface for real-time interactions.
- ✅ **Detailed Error Handling**: Ensures clear instructions and robust application stability.
- ✅ **Modular Codebase**: Easy to extend and maintain.

---

## 🛠 Tech Stack
| Technology                | Purpose                       |
|---------------------------|-------------------------------|
| Python 3.8                | Core programming language     |
| Streamlit                 | Web app framework             |
| AWS Bedrock               | Generative AI models          |
| LangChain                 | RAG & AI chaining             |
| FAISS                     | Vector similarity search      |
| boto3 & AWS CLI           | Cloud service integration     |
| pypdf                     | PDF handling                  |
| Visual Studio Code        | Development Environment       |

---

## 📁 Project Structure

bedrock-aiagent-ETE/ ├── pdf-data/ # Directory for PDF documents ├── faiss_index/ # Directory for storing FAISS indexes ├── main.py # Main Streamlit application ├── requirements.txt # Python dependencies └── README.md  

---

## 🚧 Project Workflow
- **Document Upload:** Place PDFs into the `pdf-data/` folder.
- **Text Processing:** PDF text extraction and chunking.
- **Embedding Generation:** Using Amazon Titan embeddings.
- **FAISS Storage:** Vectorized storage for rapid retrieval.
- **Query Handling:** Retrieve contextually relevant documents.
- **Response Generation:** Titan Lite generates insightful, detailed answers.
- **Frontend:** Streamlit provides interactive query and response interface.

---

## 🔑 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/abhishekyes/bedrock-aiagent-ETE.git
cd bedrock-aiagent-ETE
Step 2: Setup Python Environment
With Conda:


conda create --name bedrockproj python=3.8 -y
conda activate bedrockproj
Or with venv:
python3 -m venv bedrockproj
source bedrockproj/bin/activate
Step 3: Install Python Dependencies
Create a file requirements.txt with:

streamlit
boto3
langchain
faiss-cpu
pypdf
pandas
Then install:


pip install -r requirements.txt
Step 4: Install & Configure AWS CLI
Install AWS CLI (Mac): Official AWS CLI Installer
Then, configure AWS CLI:

aws configure
Provide your AWS credentials, default region (us-east-1), and output format (json).

🚀 Running the Application
1. Prepare PDFs
Place your PDFs inside pdf-data/ folder:

pdf-data/
├── document1.pdf
└── document2.pdf
2. Launch the Streamlit App
streamlit run main.py
3. Using the App
Click "Store Vector" to index PDFs.

Type your question and click "Send".

Receive detailed, context-aware answers instantly!

📌 Supported AWS Bedrock Models

Purpose	AWS Bedrock Model ID
Text Embedding	amazon.titan-embed-text-v1
Text Generation	amazon.titan-text-lite-v1
🛡 Error Handling & Security
PDF or FAISS Issues: Clear instructions to resolve errors.

AWS Authentication: Secure connection using AWS CLI & IAM.

Model Access Validation: Explicit model validation and error logging.

📊 Future Enhancements
 Dynamic PDF Upload Interface

 Conversation Memory (ChatGPT-like)

 Cloud-Based FAISS Storage (S3 integration)

 Multilingual Support

 Automatic PDF detection and indexing

🙌 Contributing
Your contributions are welcome and appreciated!

Fork the repo.

Create a new branch (git checkout -b feature/NewFeature).

Commit clearly (git commit -m "Implemented XYZ").

Push your changes (git push origin feature/NewFeature).

Open a Pull Request detailing your contributions.

📬 Contact & Collaboration
Author: Abhishek
📧 Email: vvabhi2776@gmail.com

Feel free to contact me for any collaboration, enhancements, or AI-related discussions!