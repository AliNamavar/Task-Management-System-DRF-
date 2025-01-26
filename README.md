# Task Management System (DRF)

A comprehensive **Task Management System** built using Django Rest Framework (DRF). This project demonstrates advanced API development techniques, showcasing best practices for building secure, scalable, and user-friendly RESTful services.

## Features

- **Flexible API Implementation**:
  - View-based APIs (APIView) for custom handling.
  - Mixins for CRUD operations with minimal code.
  - Generic views for quick development and readability.
  - Viewsets with Routers for automated URL management.

- **Advanced Authentication**:
  - JWT-based authentication for secure and scalable token management.
  - Demonstrated use of TokenAuthentication (commented for reference).

- **Custom Validations**:
  - Serializer validations for data integrity, including custom rules like priority range validation.

- **Pagination**:
  - Custom pagination for efficient data handling in large lists.

- **Permissions and Security**:
  - Role-based permissions and access control to secure API endpoints.

- **Comprehensive Documentation**:
  - Auto-generated API documentation with **DRF Spectacular**.
  - Interactive API testing interface using Swagger UI.

- **Optimized Database Queries**:
  - Query optimization to ensure fast and efficient data retrieval.

- **Testing and Debugging**:
  - API testing with Postman for robust and reliable endpoint validation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/TaskManagementSystem.git
   cd TaskManagementSystem
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/`.

## API Endpoints

- **Authentication**:
  - `POST /api/token/`: Obtain a JWT token.
  - `POST /api/token/refresh/`: Refresh the JWT token.

- **Tasks**:
  - `GET /tasks/`: Retrieve a list of tasks.
  - `POST /tasks/`: Create a new task.
  - `GET /tasks/<id>/`: Retrieve a specific task.
  - `PUT /tasks/<id>/`: Update a task.
  - `DELETE /tasks/<id>/`: Delete a task.

- **Users**:
  - `GET /users/`: Retrieve a list of users.

## Technologies Used

- **Backend**: Django, Django Rest Framework
- **Database**: SQLite (default, easily configurable for PostgreSQL)
- **Authentication**: JWT, TokenAuthentication
- **Documentation**: DRF Spectacular, Swagger UI
- **Testing**: Postman
- **Version Control**: Git, GitHub

## Screenshots

![Swagger UI](/img/Screenshot%20from%202025-01-26%2018-24-17.png)
*Interactive API documentation with Swagger UI.*


## How to Contribute

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

**Ali Namavar**  
📧 [alinamavar315@gmail.com](mailto:alinamavar315@gmail.com)  
📍 Mashhad, Iran  
[GitHub Profile](https://github.com/AliNamavar)
