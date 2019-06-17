

To Run
----------

Navigate to the root directory of the repo and run "python TestCases.py -v"

Python3
Chrome only.

I know how to make the tests run on any *given* system (for example, I have built a framework to run headless on a remote Linux server and headed on a local Windows OS), but I don't know how to ensure the tests run on an *arbitrary* system. I looked into it for a bit, but I have to move on (sys.platform doesn't work; I'm using cygwin on my Windows box, and sys.platform == 'cygwin'). Without knowing the specifics of the given system I can't ensure my tests run. To facilitate running the tests on an arbitrary system, I have provided chromedrivers for Windows, Mac, and Linux in the /resources directory, and you can alter config.py to point the script at the correct driver. This solution is verified on Windows and Mac, but I don't have a Linux machine at home.

SearchFunctionality.testLocationAndRewards can be altered to test different locations and rewards. Directions in file.

Notes
----------

- It is best practice to avoid time.sleep(), but due to time constraints and unavailability of dev resources I will use them to avoid some test stability problems (e.g., TestCases.py line 57) with the understanding that this is sub-obtimal; in these cases the line will be commented.

- Search.testTypeInput should fail; this seems to be a defect.

Things I did not do that I would have done given more time
----------------------------------------------------------

- Set up test suites with a kickoff file, processing command-line args to test run options (which suite, headed/headless, etc.)

- Headless mode. Pretty simple (import selenium...Options, set options -headless -disable-gpu, if memory serves), but had to move on

- Test cases for date, guest, and room number; the least complex way I noticed to confirm this works is by clicking on a representative sample of listings, which is out-of-scope for this assignment.

- More coverage. That being said, the framework I built makes test-writing pretty easy once the elements have been fleshed out in the pages/ file. It's for this reason I chose to focus more on the framework, and less on the coverage. Building the framework is the bulk of the work, but there is time left for little else.

- More thorough checking. For example, I only checked the search page is in the correct city in one place. Of course I would have like to speak to the project owner and ask for a full list of UI functional requirements for this, but I had neither the luxury nor the time.

- Random combination testing. I would have liked to set up a test where a random element is chosen from each field and a search conducted, then to run that test n times per suite.
