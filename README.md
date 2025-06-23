Weather Forecast Data 
Project Goal
This script was developed to collect 5-day weather forecast data for Kaduna, Nigeria using the OpenWeatherMap API. The collected data is stored in a structured CSV file, allowing for easy access and analysis using tools such as Excel or Google Sheets. The objective is to demonstrate how external weather data can be retrieved and organized to support internal planning and analysis workflows.Workflow Overview
1. Connection to a Trusted Weather API
•	The script connects to the OpenWeatherMap API.
•	Kaduna’s location is defined using latitude (10.531850) and longitude (7.429470).
•	An API key is used to authenticate the request.
2. Fetching Weather Forecast
•	The API provides a 5-day weather forecast in 3-hour intervals.
•	The returned dataset includes parameters such as:
	temperature
	humidity
	wind speed
	pressure
	weather conditions (e.g., rain, clouds)
3. Processing the Data
•	The response is in JSON format, which is parsed into a tabular structure using pandas.
•	Each row represents the weather forecast at a specific timestamp.
4. Exporting to CSV
•	The final structured data is written to weather_data.csv.
•	The CSV format ensures easy access across platforms and compatibility with Excel, Google Sheets, and BI tools.

Sample Output Structure
The CSV file contains records like:
	temperature
	humidity
	wind speed
	pressure
•	Each row represents a 3-hour forecast window.
•	Columns may contain nested structures for richer data (e.g., main and weather fields).

Business & Analytical Value
•	Forecast-Driven Planning: Enables early awareness of weather conditions for agriculture, logistics, and field operations.
•	Data Accessibility: Output can be easily ingested into spreadsheets or data dashboards for trend analysis.
•	Automation Potential: Though currently manual, this script can be integrated into scheduled tasks for daily updates.
•	Multi-Location Scalability: By adjusting the coordinates, the script can support other regions beyond Kaduna.

Implementation Notes
•	API Key Security: The API key used must be kept private. It’s currently hard-coded, which is acceptable for a POC but should be environment-managed in production.
•	Data Structure Awareness: Some fields returned by OpenWeatherMap are nested or array-based. Further parsing may be required depending on analytical needs.
•	Location Specific: The current setup only supports Kaduna. A wrapper function can generalize this for multiple locations in the future.
•	No Error Recovery: The script assumes the API responds successfully. In production, error-handling logic should be added to capture timeouts, quota limits, or malformed responses.

Conclusion
This successfully demonstrates the ability to:
•	Programmatically access weather data from OpenWeatherMap
•	Convert and structure the data using Python
•	Export the result to a user-friendly CSV file
The output is primed for further processing, visualization, or integration into operational dashboards. With minimal extension, this workflow can be scaled and automated for broader use cases.

Link to the script 
