
# docker container with cups, and small script for scanner server
for pixma mp240


# start cups
```
docker run -e CUPS_USER_ADMIN=admin -e CUPS_USER_PASSWORD=secr3t -p 6631:631/tcp -p 3000:3000/tcp print_service
```
