# PDF Document Processing System

A Docker-based application that extracts and analyzes relevant sections from PDF documents using semantic similarity and machine learning techniques.

## 🎯 Overview

This system processes PDF documents to identify and extract sections most relevant to a given persona and job description. It uses sentence transformers for semantic analysis and PyMuPDF for document parsing.

## 🏗️ Architecture

```
├── main.py              # Main application entry point
├── app/
│   ├── extractor.py     # PDF text extraction and chunking
│   ├── heading_extractor.py  # Document outline and heading detection
│   ├── scorer.py        # Semantic similarity scoring
│   ├── selector.py      # Relevant section selection
│   └── __init__.py      # Package initialization
├── input/
│   ├── documents/       # PDF files to process
│   ├── persona.txt      # User persona description
│   └── job.txt          # Job/task description
└── output/
    └── challenge1b_output.json  # Processing results
```

## 🚀 Quick Start

### Prerequisites
- Docker installed on your system
- PDF documents to process

### 1. Clone and Setup
```bash
git clone <repository-url>
cd pdf-processor
```

### 2. Prepare Input Files

Create the input directory structure:
```bash
mkdir -p input/documents output
```

Add your configuration files:
```bash
# Create persona description
echo "I am a software engineer with expertise in system architecture and API design." > input/persona.txt

# Create job description  
echo "Extract technical documentation and implementation details for system integration." > input/job.txt
```

Add your PDF documents:
```bash
cp /path/to/your/documents/*.pdf input/documents/
```

### 3. Build and Run

Build the Docker image:
```bash
docker build -t pdf-processor .
```

Run the processing:
```bash
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-processor
```

## 📋 Input Requirements

### Required Files
- **PDF Documents**: Place in `input/documents/` directory
- **persona.txt**: Description of the user persona (optional, uses default if missing)
- **job.txt**: Description of the task/job requirements (optional, uses default if missing)

### Input Structure
```
input/
├── documents/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
├── persona.txt
└── job.txt
```

### Sample persona.txt
```
I am a senior data scientist with 5 years of experience in machine learning and statistical analysis. I specialize in Python, R, and deep learning frameworks. My focus areas include predictive modeling, natural language processing, and big data analytics.
```

### Sample job.txt
```
Extract sections related to data analysis methodologies, statistical techniques, machine learning algorithms, and data preprocessing steps that would be relevant for implementing a recommendation system.
```

## 📤 Output

The system generates `output/challenge1b_output.json` with the following structure:

```json
{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "User persona description...",
    "job_to_be_done": "Job description...",
    "processing_timestamp": "2025-07-28T10:30:00.000Z",
    "total_sections_found": 25,
    "total_documents_processed": 3
  },
  "extracted_sections": [
    {
      "document": "document1.pdf",
      "section_title": "Introduction to Machine Learning",
      "importance_rank": 1,
      "page_number": 5
    }
  ],
  "subsection_analysis": [
    {
      "document": "document1.pdf", 
      "refined_text": "Full text content of the section...",
      "page_number": 5
    }
  ]
}
```

## 🔧 Technical Details

### Key Components

- **Sentence Transformers**: Uses `all-MiniLM-L6-v2` model (~90MB) for semantic similarity
- **PyMuPDF**: PDF parsing and text extraction
- **Scikit-learn**: Cosine similarity calculations
- **Heading Detection**: Font-size based heading hierarchy extraction

### Processing Pipeline

1. **Document Parsing**: Extract text and identify document structure
2. **Chunking**: Divide documents into logical sections based on headings
3. **Embedding**: Generate semantic embeddings for query and document chunks
4. **Scoring**: Calculate cosine similarity between query and chunks
5. **Selection**: Rank and select top-k most relevant sections
6. **Output**: Generate structured JSON results

### Docker Specifications

- **Platform**: AMD64 (x86_64) compatible
- **Base Image**: Python 3.9 slim
- **Model Size**: ~90MB (under 200MB requirement)
- **Dependencies**: CPU-only, no GPU required
- **Offline Operation**: All models cached during build

## 🛠️ Development

### Running Locally (Without Docker)

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python main.py
```

### Interactive Debugging

Run container in interactive mode:
```bash
docker run -it -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-processor bash
```

### Customization

Modify processing parameters in `selector.py`:
```python
def select_relevant_sections(pdf_chunks, persona, job, top_k=5):
    # Adjust top_k to change number of sections returned
```

## 📊 Performance

- **Model Loading**: ~2-3 seconds
- **Document Processing**: ~1-2 seconds per MB of PDF content
- **Memory Usage**: ~500MB peak (including model)
- **Scalability**: Processes multiple documents in batch

## 🐛 Troubleshooting

### Common Issues

**File Not Found Errors**:
```bash
# Check file permissions
chmod 644 input/persona.txt input/job.txt
chmod -R 755 input/

# Verify file paths
ls -la input/
```

**Docker Build Issues**:
```bash
# Clear Docker cache
docker system prune -a

# Rebuild from scratch
docker build --no-cache -t pdf-processor .
```

**Empty Output**:
- Ensure PDF files contain extractable text (not just images)
- Check that persona.txt and job.txt contain relevant content
- Verify PDF files are not password protected

### Debug Mode

Enable verbose output by running interactively:
```bash
docker run -it -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-processor bash
python main.py
```

## 📝 Requirements

### System Requirements
- Docker Engine 20.10+
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

### Input Constraints
- PDF files must contain extractable text
- Maximum recommended file size: 100MB per PDF
- Supported formats: PDF only

## 🚀 Advanced Usage

### Batch Processing Multiple Directories
```bash
for dir in dataset1 dataset2 dataset3; do
    docker run -v $(pwd)/$dir/input:/app/input -v $(pwd)/$dir/output:/app/output pdf-processor
done
```

### Custom Model Configuration
To use a different sentence transformer model, modify `scorer.py`:
```python
model = SentenceTransformer("your-model-name")
```

### Integration with CI/CD
```yaml
# Example GitHub Actions workflow
- name: Process Documents
  run: |
    docker build -t pdf-processor .
    docker run -v $GITHUB_WORKSPACE/input:/app/input -v $GITHUB_WORKSPACE/output:/app/output pdf-processor
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review Docker logs for detailed error messages

---

**Built with ❤️ using Python, Docker, and Machine Learning**
