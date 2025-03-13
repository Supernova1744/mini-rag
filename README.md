# Mini-RAG Application

This Mini-RAG (Retrieval-Augmented Generation) application provides an API for uploading and processing text and PDF documents. The system supports storing processed data in MongoDB and runs using FastAPI.

## Important
This code is an implementation of the mini-RAG course from [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/playlist?list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj) with the official repository on [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/bakrianoo/mini-rag/)

## Features

- Upload `.txt` or `.pdf` files under a specific project.
- Process uploaded files by dividing them into chunks.
- Store processed chunks in MongoDB.
- Supports optional resetting of processed data.

---

## API Endpoints

### 1. Upload a File
**Endpoint:**  
`POST /api/v1/data/upload/{project_id}`  

**Description:**  
Uploads a `.txt` or `.pdf` file associated with a specific `project_id`.

**Request:**  
- Multipart form-data:
  - `file` (required): A `.txt` or `.pdf` file.

**Response:**  
```json
{
    "signal": "file_upload_success",
    "file_id": "FILE_ID.EXT"
}
```

---

### 2. Process a File
**Endpoint:**  
`POST /api/v1/data/process/{project_id}`  

**Description:**  
Processes an uploaded file, dividing it into chunks, and stores the chunks in MongoDB.

**Request Body (JSON):**
```json
{
    "file_id": "FILE_ID.EXT",
    "chunk_size": 500,
    "overlap_size": 50,
    "do_reset": 1
}
```
- `file_id` (Optional string): The ID of the uploaded file.
- `chunk_size` (Optional int): The number of characters per chunk.
- `overlap_size` (Optional int): The number of overlapping characters between chunks.
- `do_reset` (Optional int 0 or 1): If `1`, resets previous processed data for the project.

**Response:**  
```json
{
    "signal": "processing_success",
    "inserted_chunks": 2241,
    "processed_file": 10
}
```

---

## Running the Application

### 1. Clone the repository:

   ```bash
   git clone https://github.com/Supernova1744/mini-rag.git
   cd mini-rag
   ```

### 2. Using Docker Compose

A `docker-compose.yml` file is provided under `docker/docker-compose.yml` to set up MongoDB.

To start MongoDB using Docker Compose, run:

```sh
cd docker
cp .env.example .env
```
update `.env` with your credintials
```
docker-compose -f docker-compose.yml up -d
```

This will start a MongoDB service in the background.

### 3. Running the FastAPI Server

Ensure you have Python 3.8+ installed, then install dependencies:

```sh
cd ../src
pip install -r requirements.txt
```

Run the FastAPI application:

```sh
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

The API will be available at `http://localhost:5000`.

---

## Database Configuration

The application connects to MongoDB using the following default configuration:

- **Host:** `localhost`
- **Port:** `27017`
- **Database Name:** `mini-rag`

Ensure MongoDB is running before using the application.

---

## Testing the API

You can use tools like **Postman** or **cURL** to test the API.

For example, to upload a file using cURL:

```sh
curl -X POST -F "file=@file_path.txt" http://localhost:5000/api/v1/data/upload/123
```

To process the file:

```sh
curl -X "POST" "http://localhost:5000/api/v1/data/process/123" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"file_id\": \"file_id.txt\", \"chunk_size\": 500, \"overlap_size\": 50, \"do_reset\": 1}"
```

---

## License

This project is open-source and available under the MIT License.
