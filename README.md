# remove_background
Project created with ML libraries that help users remove the background of their pictures.

# Feb 28,2026
As of today, I have a backend that is listening to the petitions from the frontend the problem that I have is the fact that is not showing up the results in the same frontend, I remember that I had alredy fixed this, but I don't remember how, probably it was in ChatGPT.

I will try to solve this, and later start again with deploying to google cloud.
So is solved, I was making a mistake by trying to access the project directly from the 'index.html' file and that triggers some security issues on the browser side, so the correct approach is by using the localhost:8000 endpoint.

Now lets get back to get this thing up and running in google cloud.

Here is a brief summary by chatgpt of the project:

# Background Remover – Current Project State

## Overview

Background Remover is a minimal full-stack web application that allows users to upload an image, remove its background using an AI model, and download the processed result.

The project was built to gain hands-on experience with:

- FastAPI backend development
- File uploads and binary responses
- Frontend–backend communication using Fetch API
- Static file serving
- Docker containerization
- Deployment to Google Cloud Run

---

## Architecture

### Backend

**Framework:** FastAPI  
**Server:** Uvicorn  
**Image Processing:** rembg  
**Image Handling:** Pillow (PIL)

#### Main Endpoint

`POST /remove-bg`

- Accepts an uploaded image file
- Processes it with `rembg`
- Converts output to PNG format
- Returns binary image response with:
  - `media_type="image/png"`

#### Health Check

`GET /health`

Returns:

```json
{ "status": "ok" }
