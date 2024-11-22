# Portfolio Website by alona_s

This project represents my portfolio website as a Python Developer.

---


## Getting Started

### For Local Usage

1. Clone the repository and navigate to the directory:
```bash
git clone https://github.com/alonasorochynska/portfolio-website.git
cd portfolio-website
```

2. Create and activate a virtual environment:
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate
# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages and import migrations:
```bash
pip install -r requirements.txt
python manage.py migrate
```

4. IMPORTANT: Create the superuser before starting server. Without this, the site will throw error:
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open the website:
Open the website at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

7. Log in with the superuser credentials and fill out your profile:
Use following link to log in [http://localhost:8000/admin/](http://localhost:8000/admin/).


### For Docker Containers with App and Database

1. Clone the dockerization Branch:
```bash
git clone --branch dockerization https://github.com/alonasorochynska/portfolio-website.git
cd portfolio-website
```

2. Prepare the environment variables:

Rename `.env.sample` to `.env` and update the environment variables as needed.

3. Build and run the Docker containers:

```bash
docker-compose up --build
```

4. IMPORTANT: Create the superuser from inside the Docker container. Without this, the site will throw error:

```bash
# List all running containers
docker ps

# Access the container shell
docker exec -it <name_of_website_container> sh

# Create the superuser
python manage.py createsuperuser
```
5. Open the website:

Open the website at [http://localhost:8000/](http://localhost:8000/).

6. Log in with the superuser credentials and fill out your profile:
Use following link to log in [http://localhost:8000/admin/](http://localhost:8000/admin/)


---


## Admin Panel Guide (Profile Management)

### Website Content Management

1. **Users**:
- `FIRST NAME` and `ABOUT` sections will be displayed on the home page.

2. **Skills**:
- `NAME`: Skill names will be displayed.
- `DESCRIPTION`: Used for sorting skills by colors. Supported values: "a", "b", "c", "d". Skills without a description 
will have the same color.
- `ORDER`: Determines the size of the bubble. Example values:
  - 5 (small bubble)
  - 50 (large bubble)
  
After creating a skill, you can change its `ORDER` in the list of skills. Don't forget to click "Save" after making
changes.

3. **Education**:

- Fill out all fields, and after creation, you can reorder items by dragging the `ORDER` fields with your mouse.
- <i>Don't forget to click `Save` after making changes</i>.

4. **Projects**:

- Add project details, including links to GitHub repositories or deployed examples.

5. **Experience**:

- Fill out your work experience details.

6. **Languages**:

- Add languages you speak.

7. **Private**:

- This section is under development.

### Customization

- Place your avatar image (1x1 JPEG) in `static/Assets/me.jpeg`.
- Update your LinkedIn and GitHub links in `templates/includes/footer.html`.

---

# Conclusion
This project is designed to showcase a developer's skills, experience, and portfolio in a professional manner. 
Contributions and feedback are welcome. Feel free to fork this repository and customize it to your needs.
