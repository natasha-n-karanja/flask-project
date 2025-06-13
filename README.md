# Library API with Flask

## Endpoints

### Books
- `GET /books`
- `POST /books` – Requires `{ "title": "string", "author_id": int }`
- `GET /books/<id>`
- `PUT /books/<id>`
- `DELETE /books/<id>`

### Authors
- `GET /authors`
- `POST /authors` – Requires `{ "name": "string" }`
- `GET /authors/<id>`
- `PUT /authors/<id>`
- `DELETE /authors/<id>`

## Setup
```bash
git clone <repo>
cd <repo>
pip install -r requirements.txt
python app.py

### How To Run It
1.Activate your virtual environment:
   source venv/bin/activate  # or venv\Scripts\activate on Windows

2.Install packages:
   pip install -r requirements.txt

3. Run the app:
   python app.py
