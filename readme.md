POST /likes/store: Store Like event

Required Input Fields: user_id, content_id
GET /likes/check: Check if user has liked a particular content

Required Input Fields: user_id, content_id
GET /likes/total: Total likes for a content

Required Input Fields: content_id
Output: Number of likes present for the given content.

To run the application using Docker Compose, make sure you have Docker and Docker Compose installed. Then, use the following commands in the root directory of the project:

CMD
docker-compose up --build