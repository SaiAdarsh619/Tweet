## Installation
 
1. **Clone the repository**
   ```bash
   git clone https://github.com/SaiAdarsh619/Tweet
   cd Tweet
   ```
 
2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
 
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
7. **Create media folder**
   ```bash
   mkdir media
   ```
   *Note: Django will automatically create subfolders like `media/photos/` when files are uploaded*
 
5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

 
6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```
   

   ## Running the Application
 
**Development server:**
```bash
python manage.py runserver
```
 
The application will be available at `http://localhost:8000`
