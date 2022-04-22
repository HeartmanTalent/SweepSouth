#  SWEEP SOUTH
we download pull data from <https://www.arbeitnow.com/api/job-board-api>

##  Running

to run the application build and run using the folling commands

`docker-compose build` &&
`docker-compose up`

backend: http://localhost:8000/api
frontend : http://localhost:3000/
## Architectural Decisions

Decided to pull the data whine the app is initialized just after applying migrations, to avoid delays once the app is up. 

All the data can be  somplified into 3 main Classes, Job, JobType and Tag.

Linker tables were used since I normalised the many to many relation between Job and Tags and JobType. 

I used Bulk creation to improve the system performance by reducing trips to the database.

When retrieving the data, the description had HTML template tags so, I had to remove those using regex

Tags and JobType had to be lowercased so to reduce duplication, we also had to loop through them to avoid duplication when creating them.

The order of bulk creation has been chosen to avoid linking non-existent objects.

