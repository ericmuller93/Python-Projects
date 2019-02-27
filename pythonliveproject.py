The following is a code retrospective for a web scraper that I worked on with a team at The Tech Academy. A group 
of student programmers and myself used Pythons Django to create a website that brought all different kinds of 
information to the user that was logged in. For example,they could see the weather or upcoming events in their area
with just the click of a button. In this time I was really able to see how a development team works. I focused on 
two larger back end tickets for most of my time. You can see both of them below, The TechUpcomingScraper and 
NBAScraper. While I had very basic Django experience, I had not worked on an app like this. My team and I decided
to use the BeautifulSoup module to perform the webscraping. One of the biggest lessons I learned is that you can 
really learn anything with online resources and the help of your team members! Additionally I was able to work on
some front end design with CSS once a few of the pages took shape. 


Below is the TechUpcomingScraper. This method will go to bizzabo.com and pull up the next 5 upcoming tech events.
Then is displays these events with some of their basic details on the HTML page seen under the scraper. 

class TechUpcomingScraper:

    def __init__(self):

        #  creating a variable of our link
        self.page_link = 'https://blog.bizzabo.com/technology-events'

        #here we are getting the actual content from this page
        self.page_response = requests.get(self.page_link, timeout=5)

        # this will parse the content and put it in the content variable
        self.page_content = bs(self.page_response.content, "html.parser")

        #we create an empty array, then loop through the page to store the
        #h2 elements which are the event titles
        self.eventList = [] 
        for i in range(6,11):
            pageItems = self.page_content.find_all("tr")[i].text
            self.eventList.append(pageItems)
<!-- html for the tech upcoming scrapper page -->
{% extends 'base.html' %}

<!doctype html>
<html>
    <head>
        <title>{% block title %}| Upcoming Tech Events {% endblock %}</title>
    </head>
    <body>
        {% block content %}
        <h2>Upcoming Tech Events!</h2>
            <ol>
                {% for item in tech_event.eventList %}
                    <li>{{ item }}</li>
                {% endfor %}
            </ol>
        {% endblock %}
    </body>
</html>


This is the beginning of the NBAScraper. When the user creates their profile they select their favorite sports
teams. When the user navigates to the NBA page the method will use the SportsDB API to collect the upcoming events
for their favorite NBA. Their teams logo will also be displayed.

class NBAScraper:

    def __init__ (self, team):

            #  set the user's passed favorite team name to an attribute of the instance.
            self.team = team

            #  from the user's favorite NBA team name, retrieve the team's ID (used by TheSportsDB.com api)
            #  from the record stored in the BasketballTeam model.
            team_db_record = get_object_or_404(BasketballTeam, team_name=team)
            team_id = team_db_record.team_id

            # Retrieving the url for the team's logo from TheSportsDB.com api
            # Create the url where data on the user's favorite team can be found
            team_data_url = 'https://www.thesportsdb.com/api/v1/json/1/lookupteam.php?id=' + team_id
            # Open the url and save its content
            json_team_data = urllib.request.urlopen(team_data_url).read()
            # Convert the data from JSON to a python dictionary
            team_data = json.loads(json_team_data)
            # Access and save the relevant dictionary value
            self.team_logo_url = team_data['teams'][0]['strTeamBadge']

            #  concatenate the team ID with the appropriate url prefix from TheSportsDB.com api to form
            #  the query for the user's favorite mlb team and read the data.
            events_url = 'https://www.thesportsdb.com/api/v1/json/1/eventsnext.php?id=' + team_id
            converted_json_data = json.loads(urllib.request.urlopen(events_url).read())
            
            self.events = []
            for index in range(0,5):
                event_str = converted_json_data['events'][index]['strEvent']
                event_date = converted_json_data['events'][index]['dateEvent']
                # Creating a dictionary for each event, rather than a string, will give us more flexibility in the template, since we'll be able to easily access each event's individual attributes
                event = {
                'name': event_str,
                'date': event_date
                }
                self.events.append(event)
<!-- html for the NBA scraper -->
{% extends 'base.html' %}

{% block title %}| NBA{% endblock %}

{% block content %}

<p>Your favorite NBA team is the {{ nba.team }}</p>

<h2>Next 5 Events for the {{ nba.team }}</h2>
<table>
  <thead>
    <th>Date</th>
    <th>Event</th>
  </thead>
  <tbody>
      {{ nba.event }}
    {% for event in nba.events %}
      <tr>
        <!-- Note that event is a dictionary, and part of Django's template language is that the values of a dictionary are accessed with dot notation rather than bracket notation. -->
        <td>{{ event.date }}</td>
        <td>{{ event.name }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>

<img src={{ nba.team_logo_url }} alt="">
{% endblock %}