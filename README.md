
# Django Project Setup

This is a Django project that contains a news application with functionality for creating and managing newspapers, topics, and users (redactors).

## Table of Contents
- [Setting Up Your Environment](#setting-up-your-environment)
- [Installing Dependencies](#installing-dependencies)
- [Models](#models)
- [Views](#views)
- [URLs](#urls)

## Setting Up Your Environment

Follow these steps to set up a virtual environment (venv) and activate it:

1. **Create a Virtual Environment**  
   In your terminal, navigate to the directory where you want to create the project and run the following command:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**  
   To activate the virtual environment, run the following command:

   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   Install the required dependencies listed in the `requirements.txt` file by running:
   ```bash
   pip install -r requirements.txt
   ```

## Installing Dependencies

Once the virtual environment is activated, you can install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the following:
- Django
- Django Resized (for image resizing)
- Other dependencies defined in the `requirements.txt`

## Dropbox
Follow the link there you will find instructions on how to get the data specified in the .env.template after you get it create the .env file and fill it in according to the provided sample
https://django-storages.readthedocs.io/en/latest/backends/dropbox.html

## Models

### Redactor Model
The `Redactor` model extends Django’s `AbstractUser` and includes the following fields:
- `years_of_expirience`: The years of experience the redactor has.
- `photo`: A profile picture, resized to `WEBP` format with 75% quality.

### Newspaper Model
The `Newspaper` model contains information about the newspaper:
- `title`: The title of the newspaper.
- `content`: The content of the newspaper.
- `published_date`: The date the newspaper was published.
- `topics`: A many-to-many relationship with the `Topic` model.
- `publishers`: A many-to-many relationship with the user model (redactors).
- `photo`: An image related to the newspaper, resized to `WEBP` format.

### Topic Model
The `Topic` model represents a news topic and contains the following field:
- `name`: The name of the topic.

## Views

### Redactor Views
- **RedactorListView**: Displays a list of all redactors.
- **RedactorRegisterView**: Handles the registration process for new redactors.
- **RedactorUpdateView**: Allows a logged-in redactor to update their profile details.

### Newspaper Views
- **NewspaperListView**: Displays a list of newspapers, with filtering options for topics.
- **NewspaperDetailView**: Displays a detailed view of a single newspaper.
- **NewspaperCreateView**: Allows a logged-in redactor to create a new newspaper.
- **NewspaperUpdateView**: Allows a logged-in redactor to update an existing newspaper.
- **NewspaperDeleteView**: Allows a logged-in redactor to delete a newspaper.

### Topic Views
- **TopicListView**: Displays a list of all topics.
- **TopicCreateView**: Allows a logged-in redactor to create a new topic.
- **TopicUpdateView**: Allows a logged-in redactor to update an existing topic.
- **TopicDeleteView**: Allows a logged-in redactor to delete a topic.

## URLs

### Redactor URLs
- **/redactors/**: List of redactors.
- **/redactors/signup/**: Redactor registration page.
- **/redactors/{id}/update/**: Redactor profile update page.

### Newspaper URLs
- **/**: List of newspapers.
- **/create/**: Newspaper creation page.
- **/{id}/**: Newspaper detail page.
- **/{id}/update/**: Newspaper update page.
- **/{id}/delete/**: Newspaper deletion page.

### Topic URLs
- **/topics/**: List of topics.
- **/topics/create/**: Topic creation page.
- **/topics/{id}/update/**: Topic update page.
- **/topics/{id}/delete/**: Topic deletion page.

