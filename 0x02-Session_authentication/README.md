# Curriculum: Session Authentication Project

This repository contains the implementation for the Session Authentication project as part of the curriculum. In this project, we implement a Session Authentication mechanism from scratch, exploring concepts like cookies, session management, and user authentication.

## Project Overview

The goal of this project is to implement a Session Authentication mechanism without using any external modules or frameworks. We'll explore the concepts of cookies, user sessions, and authentication using Python and Flask.

### Learning Objectives

By completing this project, you will be able to:

- Understand what authentication means in web applications.
- Implement session authentication using cookies.
- Explore the role of cookies in maintaining user sessions.
- Build a basic authentication system without relying on external modules.
- Create routes and views to handle session-based authentication.

## Project Structure

The project is divided into several tasks, each building on the previous ones to create a complete session authentication system. Here's an overview of the tasks:

1. **Session Authentication Introduction**: Understanding the project context and learning objectives.

2. **Empty Session Auth Class**: Creating the foundation for the SessionAuth class without any functionality.

3. **User ID for Session ID**: Implementing methods to associate user IDs with session IDs and retrieve user IDs based on session IDs.

4. **Session Cookie**: Adding a method to retrieve a cookie value from a request to handle session IDs.

5. **Before Request**: Updating the `@app.before_request` method to ensure authentication for specific routes.

6. **Use Session ID for Identifying a User**: Implementing a method to retrieve a User instance based on a session ID.

7. **New View for Session Authentication**: Creating a new Flask view to handle session authentication routes.

## Usage

To run the project, you can follow these steps:

1. Set up the necessary environment variables, such as `API_HOST`, `API_PORT`, `AUTH_TYPE`, and `SESSION_NAME`.

2. Run the main application script, usually named `main.py`, to start the server.

3. Use tools like `curl` to interact with the API endpoints and test the functionality.
Happy coding!

