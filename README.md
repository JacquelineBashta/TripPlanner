# TripPlanner
App to allow collecting trip planning information in one structure form, and perform some consistency checks

## TODO
 
### Features
- [x] Scrolling option
- [x] removing row
- [x] add new block (weather,currency,simcard)
- [ ] entries format check
- [ ] Logical Entry consistency checks
    - [x] current entry to_location == previous entry from_location
    - [x] if current entry date to_date > previous from_date, check stay exist
    - [x] else if current entry date == previous -> check time difference > defined_time_frame (e.g. 2h)
    - [x] based on the transportaion change the TRANSITION_TIME
    - [ ] Change mean of transportation to dropdown -> default=None

- [x] Organize the buttons beautifully
- [ ] label summary to collect total time dates / days in each city / total cost


### GUI

