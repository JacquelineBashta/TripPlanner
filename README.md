# TripPlanner
App to allow collecting trip planning information in one structure form, and perform some consistency checks

## TODO
 
### Features
- [x] Scrolling option
- [x] removing row
- [x] add new block (weather,currency,simcard)
- [ ] entries format check
    - [ ] Change mean of transportation to dropdown -> default=None

- [x] Logical Entry consistency checks
    - [x] current entry to_location == previous entry from_location
    - [x] check that  to_datetime > from_datetime of same entry
    - [x] if current entry date to_date > previous from_date, check stay exist
    - [x] else if current entry date == previous -> check time difference > defined_time_frame (e.g. 2h)
    - [x] based on the transportaion change the TRANSITION_TIME

- [x] label summary to collect total time dates / days in each city / total cost
- [ ] Support save/load different trip files
- [ ] Add "comment" feature per Frame , using separate window

### GUI
- [x] Organize the buttons beautifully
- [ ] Add label to each entry
- [ ] Add frame/boarder for each block
- [ ] Clean up frames arrangement
- [ ] Wrap up text entries
