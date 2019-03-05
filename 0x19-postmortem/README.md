### 0x19. Postmortem


#### Issue Summary:
Issue Start Time: 03/01/2019 12:00AM PST\\
Issue End Time: 03/01/2019 1:30PM PST\\
Issue Impact: 50% of web server requests resulted in error messages\\
Root Cause: mis-configured web server not allowing enough concurrent connections\\

#### Timeline:
Issue detection: First report of website outage by user at 03/01/2019 8:35AM PST\\
Misleading Investigation: Level 1 support verified that website was running by going to the website.  Since only roughly 50% of the requests resulted in error.  Level 1 supoort initially did not detect that there were issues with the server and closed the report as no action needed.  At 03/01/2019 10:00AM PST, more users started reporting website outage and Level 1 support were able to duplicate the outage spordically, after re-starting the web server and issue still occuring, at 03/01/2019 the issue was escalated to Level 2 Devops support team.\\ 
Incident Resolution: After Level 1 team escalated to Level 2 team, Level 2 support team ran some tests and realized the web server was configured incorrectly.  Configuration file was updated and server was back to normal on 03/01/2019 at 1:30 PM\\

#### Root cause and resolution:
Issue Resolution: Level 2 Devops support team was initially not able to see any issues while looking at the error and decided to stress test the web server.  During stress testing of the web server it was discovered that when there are over 1000 concurrent request to the web server, roughly half of the requests would fail.  After further checking, it was discovered that the server configuration for file limit was set incorrectly and the value was set too low.  This causes "too many open files" error when there is a heavy load on the server. \\
The server configuration file was updated to allow 5000 concurrent requests and stressed testedto ensure that no more issues were found when there is a heave load on the server\\

#### Correct and preventative measures:
Improvements: To prevent this from happening again, all future server testing must include stress testing to minimize outages during heavy loads on the servers.\\
Prior to any major sales events, all server configuration must be double checked and stress tested to make sure it can handle the expected loads.\\ 


