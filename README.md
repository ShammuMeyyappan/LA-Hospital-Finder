**README**  
**Installation Requirements**  
pip install bs4  
pip install requests  
pip install csv  
Pip install matplotlib.pyplot   
Pip install pandas  
Pip install sklearn  
Pip install numpy   
Pip install pandas   
Pip install geopandas   
Pip install arcpy  
**Collecting and Cleaning**  
The data collected for the project was the list of services, insurance, and address texts on the hospital webpages. In order to collect the data from the websites, Beautiful Soup was used. A beautiful soup HTML parser was used to collect the data. Then, to gather the data, the project ran a for loop with the element service or insurance element. Depending on the loop, it required one or more for loops. Then a get\_text strip=true was used to remove everything except the text collected. Then the data was filtered using an index where everything below a keyword is kept. Followed by everything below, a target word is removed. This ensures that data is only kept was the services and insurance between the keyword and the target word. This data is then written to a CSV. The same is done for the street address, except this time it is written in the next column. In order to run this code need to hit run for each website.   
**Analysis and Visualization**  
	The first visualizations are bar charts that take all the CSVs that have been collected and cleaned. Then each list's rows is added up and stored in a variable. Each variable is then added to a list of lists. Then a separate list is used to store abbreviated hospital names. Then matplotlib is used to create a bar chart showing the number of insurance or services. Then simply run the script, and a bar chart will be generated.  
	Next are two scripts that allow the user to find out what hospitals offer which services or insurances are accepted by the hospital. First, the CSV is appended to a list. Then these lists are stored in lists of lists. A function then takes the list of lists and user input to find which hospitals offer the service or insurance. Then an if or else statement is run to either let the user know that service or insurance is offered, or let them know it is not offered or accepted there. The user will get an input after running the script, fill it, and then enter to see the results.   
	The next script allows the user to find the Correlation Coefficient Analysis and visualization of data as a scatter plot. First, insurance and services are summed up, and then stored to variables. Second, the variables are stored in lists, then made into a series. Third, the names of the hospitals are stored in a separate list. Fourth, a Correlation Coefficient takes the series created to run the analysis. Fifth, matplotlib is used to create a chart showing insurances as the x-axis and services as the y-axis. Then each hospital is displayed on the chart as a point. Simply hit run on the script and see the chart generated.   
	The next script converts the CSV's street data into Geocoded latitude and longitude points. This script takes all the CSVs that added address as the next column. These are brought over to ArcGIS Pro, where the geocode tool takes the address column in the CSV to geocode the addresses. These files are converted into feature layer points. Then, the Feature Layer to Shapefile tool converts the feature layers to shapefiles. Then shapefiles are saved to a folder. In order to run this Model Builder Script, a person needs access to ArcGIS Pro, and then run the script.   
	The final visualization was creating a map of the hospital locations. First a function is used to create a scale bar. Then all the shapefiles created by the previous script are read and stored to a variable. Then, scripts for each of these points are given a spatial reference. Then script gives each point a color. After that, the script adds an arrow and the people who created the map. Then a legend is created for each point, followed by a title, and showing the data. In order to see where each point is located. 

	  
